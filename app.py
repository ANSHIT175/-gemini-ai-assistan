import google.generativeai as genai

# Paste your Gemini API key here
genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

print("=== AI Question Answering Assistant using Gemini API ===")

while True:
    user_input = input("\nAsk a question (type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Exiting application.")
        break

    response = model.generate_content(user_input)
    print("\nAI Response:\n", response.text)
