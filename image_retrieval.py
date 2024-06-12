# Import necessary libraries
import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from langchain_core.documents import Document
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from PIL import Image
import io
import time



# Load environment variables from .env file
load_dotenv()
gemini_key = os.getenv('Google_gemini_key')

# Configure the generative AI model
genai.configure(api_key=gemini_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize embeddings model
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Function to load and process images
def load_and_process_image(image_path, target_size=(256, 256)):
    with open(image_path, 'rb') as img_file:
        img = Image.open(io.BytesIO(img_file.read()))
        resized_img = img.resize(target_size, Image.LANCZOS)
        return resized_img

# Function to generate image description
def generate_image_description(image):

    prompt="""Write a short, detailled description of the attached image. 
    desribe it as you are describing your own photo, please do not exceed two phrases"""

    response = model.generate_content([prompt, image], stream=True)
    response.resolve()
    return response.text

# Function to create a document from image description
def create_document_from_image(image_path):
    image = load_and_process_image(image_path)
    description = generate_image_description(image)
    document = Document(
        page_content=description,
        metadata={"source": os.path.basename(image_path)}
    )
    return document


# Create vector store and retriever
def create_retriever(documents):
    vectorstore = FAISS.from_documents(documents, embeddings)
    retriever = vectorstore.as_retriever()
    return retriever


# Load images from albums and generate descriptions
def load_images_from_albums(album_paths):
    documents = []
    status_placeholder = st.empty()
    for album_path in album_paths:
        for image_name in os.listdir(album_path):
            image_path = os.path.join(album_path, image_name)
            if os.path.isfile(image_path):
                print(f"Loading {image_path}")
                # st.write(f"Processing {image_name}...")
                status_placeholder.text(f"Processing {image_name}...")
                document = create_document_from_image(image_path)
                documents.append(document)
                time.sleep(1)  # To avoid rate limits
                status_placeholder.text("")
    return documents


# Function to retrieve an image based on search query
def retrieve_image(query, retriever):
    docs = retriever.invoke(query)
    return docs


# Streamlit application

st.markdown("""
    <style>
    .stApp {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    .stImage img {
        margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🖼️ PhotoFinder Pro: Your Personal Image Retrieval Assistant 📸")
st.write("Search 🔍 and retrieve your photos 🖼️ easily. ✨")


# Define album paths
album_paths = ["./album"]  # Update with actual album paths

# Load documents
if st.button("Load Images"):
    if not 'retriever' in st.session_state:
        with st.spinner("Loading images and generating descriptions..."):
            documents = load_images_from_albums(album_paths)
            retriever = create_retriever(documents)
            st.session_state['retriever'] = retriever
        st.success("Images loaded successfully!")

if 'retriever' in st.session_state:
    query = st.text_input("Enter your search query:")
    query_prompt = f"Given the following query from the user, enrich it to enhance retrieval, add more context, and act as if you are the user describing his image to look for it. Return a detailed image description in no more than two sentences. \n Query : {query}"
    if query:
        response = model.generate_content(query_prompt)
        # st.write(response.text)
        docs = retrieve_image(response.text, st.session_state['retriever'])
        result = docs[0].metadata['source'] if docs else None
        if result:
            st.image(os.path.join("album", result))  # Adjust path as necessary
            # for doc in docs:
            #     st.write(f"Retrieved image: {doc.metadata['source']}")
            #     st.write(f"desc: {doc.page_content}")
        else:
            st.write("No matching image found.")