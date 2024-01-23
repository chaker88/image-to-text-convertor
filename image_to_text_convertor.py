import streamlit as st
from PIL import Image
import pytesseract

# Set the path to the Tesseract executable (update with your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image):
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(image)
    return text

def main():
    st.title("Image Text Extraction with Tesseract OCR")

    uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg"])

    if uploaded_file is not None:
        # Display the selected image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform OCR on the image
        result_text = extract_text_from_image(image)

        # Display the extracted text
        st.subheader("Extracted Text:")
        st.text(result_text)

if __name__ == "__main__":
    main()
