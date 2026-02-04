"""import pandas as pd

# 1. Hum khud ka ek data banate hain (Jaise Amazon ka data ho)
data = {
    'Mobile Name': ['iPhone 15', 'Samsung S23', 'Redmi Note 12', 'OnePlus 11', 'Pixel 7'],
    'Price': [80000, 75000, 15000, 55000, 50000],
    'Rating': [4.8, 4.7, 4.1, 4.5, 4.6]
}

# 2. Ise Pandas ke "DataFrame" (Table) mein badalte hain
df = pd.DataFrame(data)

print("--- Sabhi Mobiles ka Data ---")
print(df)

# 3. Filter lagate hain: Sirf wo mobiles jo 50,000 se saste hain
saste_mobiles = df[df['Price'] <= 50000]

print("\n--- 50,000 se saste aur best mobiles ---")
print(saste_mobiles)

# 4. Excel file banana (Earning ke liye ye zaroori hai)
# df.to_csv('amazon_data.csv', index=False)
# print("\nEk file 'amazon_data.csv' ban gayi hai!")
import pandas as pd
import os

data = {
    'Mobile Name': ['iPhone 15', 'Samsung S23', 'Redmi Note 12', 'OnePlus 11', 'Pixel 7'],
    'Price': [80000, 75000, 15000, 55000, 50000],
    'Rating': [4.8, 4.7, 4.1, 4.5, 4.6]
}

df = pd.DataFrame(data)

try:
    # Hum file ko save karne ki koshish kar rahe hain
    filename = "amazon_data.csv"
    df.to_csv(filename, index=False)
    
    # Ye line check karegi ki file bani ya nahi
    if os.path.exists(filename):
        print(f"✅ Mubarak ho! '{filename}' kamyabi se ban gayi hai.")
        print(f"File ka rasta: {os.path.abspath(filename)}")
    else:
        print("❌ File nahi ban saki.")
        
except Exception as e:
    print(f"❌ Error aaya: {e}")"""

import google.generativeai as genai

# 1. Configuration
genai.configure(api_key= os.getenv("GEMINI_API_KEY"))

# 2. Model (Wahi naam jo aapne list mein dekha)
# Note: Agar list mein 'models/gemini-1.5-flash' hai, toh pura likhein
model = genai.GenerativeModel('gemini-2.5-flash-lite-preview-09-2025') 

try:
    print("AI ab jawab dene wala hai...")
    # 3. Test Question
    response = model.generate_content("Kya aap mere liye Amazon ka data analyze kar sakte hain?")
    
    print("\n--- GOOGLE AI KA JAWAB ---")
    print(response.text)
    print("--------------------------")
    
except Exception as e:

    print(f"Abhi bhi issue hai: {e}")
