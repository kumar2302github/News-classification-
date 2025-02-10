import streamlit as st
from transformers import pipeline
from io import StringIO
from PIL import Image
import pytesseract
from streamlit_extras.add_vertical_space import add_vertical_space
import ollama

# ---------------------------------------------------------------------------
# Set up Tesseract command if needed
# ---------------------------------------------------------------------------
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\kumar\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------

@st.cache_resource
def classification_model():
    """
    Loads the text-classification model.
    Replace "test/checkpoint-12000" with your model's identifier or path.
    """
    try:
        classifier = pipeline("text-classification", model="test/checkpoint-12000")
        return classifier
    except Exception as e:
        st.error(f"Error loading classification model: {e}")
        return None

def classify_text(text):
    """
    Classify the input text and return the label and confidence score.
    """
    classifier = classification_model()
    if classifier is None:
        return None, None
    output = classifier(text)
    label = output[0]["label"]
    score = output[0]["score"]
    return label, score

def extract_text_from_image(image):
    """
    Extract text from an image using pytesseract.
    'image' should be a PIL Image.
    """
    try:
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        st.error(f"Error extracting text from image: {e}")
        return ""

def summarize_text(text, category):
    """
    Summarize the provided text using Ollama.
    The summarization prompt includes the category information.
    """
    prompt = f"You are a highly trained professional news anchor in the field of {category}. Summarize the following news in less than 80 words: {text}"
    try:
        summary = ollama.chat(model="deepseek-r1:8b", messages=[{"role": "user", "content": prompt}])
        return summary["message"]["content"]  # Extract model's response
    except Exception as e:
        st.error(f"Error during summarization: {e}")
        return "Could not generate summary."

def process_text_input(text):
    """
    Process text by classifying and summarizing it.
    Returns classification label, confidence score, and summary.
    """
    category, conf = classify_text(text)
    summary = summarize_text(text, category)
    return category, conf, summary

def process_image_input(image):
    """
    Process an image:
      1. Extract text using OCR.
      2. Classify the extracted text.
      3. Summarize the extracted text.
    Returns the extracted text, classification label, confidence score, and summary.
    """
    extracted_text = extract_text_from_image(image)
    category, conf = classify_text(extracted_text)
    summary = summarize_text(extracted_text, category)
    return extracted_text, category, conf, summary

# ---------------------------------------------------------------------------
# Streamlit UI
# ---------------------------------------------------------------------------

def main():
    st.title("News Classification & Summarization")

    # Sidebar: Choose input type and upload file
    with st.sidebar:
        st.title('News Classifier')
        add_vertical_space(2)
        input_type = st.radio("Select input type", ("Text", "Image"))
        add_vertical_space(2)
        
        if input_type == "Text":
            uploaded_text_file = st.file_uploader("Upload a text file", type="txt")
        else:
            uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    # Process Text Input
    if input_type == "Text" and 'uploaded_text_file' in locals() and uploaded_text_file is not None:
        stringio = StringIO(uploaded_text_file.getvalue().decode("utf-8"))
        text_data = stringio.read()
        st.subheader("Text Content:")
        st.text(text_data)
        
        if st.button("Process Text"):
            st.info("Processing the text...")
            category, conf, summary = process_text_input(text_data)
            if category is not None:
                st.success("Processing complete!")
                st.write(f"**Category:** {category} (Confidence: {conf:.2f})")
                st.write("**Original News Text:**")
                st.write(text_data)
                st.write("**Summary:**")
                st.write(summary)
            else:
                st.error("Classification failed.")

    # Process Image Input
    if input_type == "Image" and 'uploaded_image' in locals() and uploaded_image is not None:
        try:
            image = Image.open(uploaded_image)
        except Exception as e:
            st.error(f"Error opening image: {e}")
            return
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        if st.button("Process Image"):
            st.info("Processing the image...")
            extracted_text, category, conf, summary = process_image_input(image)
            st.success("Processing complete!")
            st.subheader("Extracted Text:")
            st.text(extracted_text)
            if category is not None:
                st.write(f"**Category:** {category} (Confidence: {conf:.2f})")
                st.write("**Original News Text:**")
                st.write(extracted_text)
                st.write("**Summary:**")
                st.write(summary)
            else:
                st.error("Classification failed.")

if __name__ == "__main__":
    main()
