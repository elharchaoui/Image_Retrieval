Sure, here is a `README.md` file for your application:

```markdown
# PhotoFinder Pro: Your Personal Image Retrieval Assistant 📸

## Overview
PhotoFinder Pro is a powerful application that helps you easily find your photos by searching through your albums with natural language queries. With advanced AI capabilities, PhotoFinder Pro generates descriptions for your images and allows you to retrieve them effortlessly.

## Features
- **AI-powered Image Description:** Automatically generate descriptions for your photos using state-of-the-art AI models.
- **Natural Language Search:** Search for your images using simple, natural language queries.
- **Real-time Processing:** View the progress of image processing in real-time.
- **User-friendly Interface:** Easy-to-use interface built with Streamlit.

## Installation

### Prerequisites
- Python 3.9 or higher
- Streamlit
- Pillow
- google-api-python-client
- langchain-core
- langchain-community
- python-dotenv

### Setup

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:elharchaoui/Image_Retrieval.git
   cd Image_Retrieval
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   Create a `.env` file in the project root directory and add your Google API key:
   ```env
   Google_gemini_key=YOUR_GOOGLE_API_KEY
   ```

## Usage

1. **Organize Your Images:**
   Ensure your images are organized in album folders (e.g., `album1`, `album2`, etc.).

2. **Run the Application:**
   ```bash
   streamlit run image_retrieval.py
   ```

3. **Load Images:**
   Click the "Load Images" button to start loading and processing images from the specified album paths.

4. **Search for Images:**
   Enter a natural language query in the text input to search for images. The application will display the retrieved image based on the query.

## Example

Here's an example of how to use PhotoFinder Pro:

1. Organize your images in folders named `album1`, `album2`, etc.
2. Run the application using `streamlit run image_retrieval.py`.
3. Click "Load Images" to process the images.
4. Enter a query like "when I was in the kitchen" to retrieve images matching the description.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://developers.google.com/ai)
- [Langchain Core](https://github.com/langchain-ai/langchain)
- [Pillow](https://python-pillow.org/)

## Contact

For any inquiries or issues, please contact [med.el.harchaoui@gmail.com](mailto:med.el.harchaoui@gmail.com).
Website : https://mohamedelharchaoui.com/

