import os
from dotenv import load_dotenv

load_dotenv(override=True)

api_key=os.getenv("API_KEY")
print(api_key)