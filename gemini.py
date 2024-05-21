
import google.generativeai as genai
my_api_key_gemini = "GEMINI-API-KEY"
genai.configure(api_key=my_api_key_gemini)
model = genai.GenerativeModel('gemini-pro')

generation_config = {
  "max_output_tokens": 500,
}

question ="Hello what you can do "
response = model.generate_content(question, generation_config=generation_config)

if response.text:
    print(response.text)
else:
    print("Sorry, but I think Gemini didn't want to answer that!")