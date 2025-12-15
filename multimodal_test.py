from google import genai
from google.genai.types import Part
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv("GEMINI_API_KEY.env")

# Get API key from environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment file")

# Initialize client
client = genai.Client(api_key=api_key)

# Function to load an image
def load_image(path):
    with open(path, "rb") as f:
        return f.read()

# Ask the model to describe image
def analyze_image(image_path):
    image_bytes = load_image(image_path)

    # Create an image part using Part.from_bytes
    image_part = Part.from_bytes(
        data=image_bytes,
        mime_type="image/jpeg"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            "Describe this image in detail.",
            image_part
        ]
    )

    return response.text

if __name__ == "__main__":
    image_path = "test_image.jpg"   # Your image file
    result = analyze_image(image_path)
    print("\nAnalyzing image...\n")
    print(result)
    print("\n-------------------------\n")
