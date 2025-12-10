import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load the variables
load_dotenv(override=True)

# 2. Setup the client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

print("⏳ Sending request to AI...")

try:
    response = client.chat.completions.create(
        model="mistralai/devstral-2512:free",  
        messages=[
            {"role": "user", "content": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"}
        ]
    )

    # 3. Check the result
    content = response.choices[0].message.content
    finish_reason = response.choices[0].finish_reason

    if not content:
        print("⚠️  Warning: AI returned empty text.")
        print(f"Reason it stopped: {finish_reason}")
    else:
        print("--------------------------------")
        print("✅ AI Answer:")
        print(content)
        print("--------------------------------")

except Exception as e:
    print(f"❌ Connection Error: {e}")