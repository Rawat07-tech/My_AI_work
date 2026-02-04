import google.generativeai as genai

# 1. API Key Setup
# Ise kisi ko mat dikhana!
MY_KEY = "AIzaSyDcsmFm8DNTW5B66prWYdTyZAnVPAcYTXE" 
genai.configure(api_key=MY_KEY)

# 2. Model Selection (2026 ka sabse fast model)
model = genai.GenerativeModel('gemini-pro')

try:
    print("AI ko message bhej raha hoon...")
    
    # 3. Simple Sawal
    response = model.generate_content("Main ek 23 saal ka Python developer hoon. Kya hum aaj ek project shuru karein?")
    
    print("\n" + "="*20)
    print("AI KA JAWAB:")
    print(response.text)
    print("="*20 + "\n")
    
except Exception as e:
    print("\nAbhi bhi ek masla aa raha hai:")
    # Agar model nahi mila toh ye batayega
    print(f"Details: {e}")
    print("\nMashwara: Agar 'Model not found' likha hai, toh 'gemini-1.5-flash' ki jagah 'gemini-pro' likh kar dekhein.")