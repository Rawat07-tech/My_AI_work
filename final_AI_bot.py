import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# 1. AI Setup (Apni Key aur Model Name check kar lein)
genai.configure(api_key= os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash-lite-preview-09-2025') # Ya jo aapka stable chala tha

# 2. Web Scraping Part
url = "https://en.wikipedia.org/wiki/Cyber_Security"
print("🌐 Internet se data nikal raha hoon...")

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Poore text ko ek saath jama karna
paragraphs = soup.find_all('p')
raw_text = ""
for p in paragraphs[1:5]: # Sirf shuru ke 4-5 paragraphs uthate hain
    raw_text += p.text

# 3. AI Analysis Part
print("🧠 AI ab is data ko samajh raha hai...")
# Is prompt se AI ek security expert ki tarah sochega
prompt = f"""
Niche diye gaye Cyber Security text ko analyze karo aur mujhe ye batao:
1. Ismein kaunse main threats (khatre) bataye gaye hain?
2. Ek aam insaan isse kaise bach sakta hai?
Jawab bullet points mein dein.
Text: {raw_text}
"""

try:
    ai_response = model.generate_content(prompt)
    print("\n" + "="*30)
    print("AI SUMMARY OF WIKIPEDIA:")
    print(ai_response.text)
    print("="*30)
except Exception as e:

    print(f"AI Error: {e}")
