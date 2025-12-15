from google import genai

client = genai.Client(api_key="AIzaSyByPw4rnM-Bu1dDPhOJF-ft0qkOQI4mjKc")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello!"
)

print(response.text)
