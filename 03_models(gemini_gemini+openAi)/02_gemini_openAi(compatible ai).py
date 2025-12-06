# here i am using gemini through openAi

from openai import OpenAI


client = OpenAI(
    api_key="AIzaSyBGhh-VPMXGVbnNpclYU9LF-gxwBUCzEm4",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "hey there, my name is asad.. for now you call me sir Asad",
        },
    ],
)

print(response.choices[0].message)
