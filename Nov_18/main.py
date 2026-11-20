from google import genai
client=genai.client(api_key="YOUR_API_KEY")
with open("sample text.txt", "r") as file:
    content = file.read()

your_content = input("Enter your content: ")
response=client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=f"summarize this text in simple words:{your_content} \n\n {content}"
)