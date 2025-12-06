from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyBGhh-VPMXGVbnNpclYU9LF-gxwBUCzEm4")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="hey there! my name is Asad. do you know the president of the 'US'"
)
print(response.text)
