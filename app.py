import streamlit as st
from google import genai
from google.genai.types import Part
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
try:
    env_path = Path(__file__).parent / "GEMINI_API_KEY.env"
except NameError:
    # Fallback if __file__ is not available
    env_path = Path("GEMINI_API_KEY.env")
load_dotenv(env_path)

# Get API key from environment
api_key = os.getenv("GEMINI_API_KEY")

st.title("Multimodal AI App")

# Check API key and initialize client
if not api_key:
    st.error("GEMINI_API_KEY not found in environment file. Please check your GEMINI_API_KEY.env file.")
    st.stop()

client = genai.Client(api_key=api_key)

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# FEATURE A: Image Description
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    
    # Read image bytes once and store in session state to avoid re-reading
    if 'image_bytes' not in st.session_state or st.session_state.get('uploaded_file_name') != uploaded_file.name:
        st.session_state.image_bytes = uploaded_file.read()
        st.session_state.uploaded_file_name = uploaded_file.name
    
    if st.button("Describe Image"):
        # Create image part using Part.from_bytes
        image_part = Part.from_bytes(
            data=st.session_state.image_bytes,
            mime_type=uploaded_file.type
        )
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    "Describe this image in detail.",
                    image_part
                ]
            )
            response_text = response.text
            st.subheader("Description")
            st.write(response_text)
            
            # Add to history
            st.session_state.history.append({
                "user": "Describe this image in detail.",
                "response": response_text
            })
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")

    # FEATURE B: Ask Questions About Image
    st.subheader("Ask a question about the image")
    user_question = st.text_input("Enter your question")

    if st.button("Ask AI"):
        if user_question:
            # Create image part using Part.from_bytes
            image_part = Part.from_bytes(
                data=st.session_state.image_bytes,
                mime_type=uploaded_file.type
            )
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[
                        user_question,
                        image_part
                    ]
                )
                response_text = response.text
                st.subheader("Answer")
                st.write(response_text)
                
                # Add to history
                st.session_state.history.append({
                    "user": user_question,
                    "response": response_text
                })
            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")
        else:
            st.warning("Please enter a question.")


# FEATURE C: Text-to-Image (Note: Gemini models don't generate images, only analyze them)
st.header("Text Analysis")
st.info("Note: Gemini models analyze images but don't generate them. Use this for text-only queries.")

prompt = st.text_input("Enter a text prompt")

if st.button("Analyze Text"):
    if prompt:
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[prompt]
            )
            response_text = response.text
            st.subheader("Response")
            st.write(response_text)
            
            # Add to history
            st.session_state.history.append({
                "user": prompt,
                "response": response_text
            })
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
    else:
        st.warning("Please enter a prompt.")

# Display chat history
if st.session_state.history:
    st.header("Chat History")
    for h in st.session_state.history:
        st.write(f"**You:** {h['user']}")
        st.write(f"**AI:** {h['response']}")
        st.write("---")
    
    # Clear history button
    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()
