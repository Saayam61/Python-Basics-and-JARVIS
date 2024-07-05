import google.generativeai as genai

genai.configure(api_key="AIzaSyAqDF85ykRBOiLr1ezHRh86TZqMuhc-pIQ")

model = genai.GenerativeModel('gemini-1.5-pro')

prompt = "tell me a joke"
messages = [
    {"role": "system", "content": "You are a virtual assistant named Jarvis. Always respond like J.A.R.V.I.S. from Iron Man franchise."},
    {"role": "user", "content": prompt}
]

combined_prompt = "\n".join([f"{message['role']}: {message['content']}" for message in messages])


response = model.generate_content(combined_prompt)
print(response.text)