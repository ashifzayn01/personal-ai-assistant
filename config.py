from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

if API_KEY is None:
    raise ValueError("OPENAI_API_KEY not found in .env")

client = OpenAI(api_key=API_KEY) #openai models use kar sakte ho jo api key k sath authenticate kar sakte ho


#In short:

# .env file se API key load hoti hai.

# Agar key nahi mili toh error aata hai.

# Agar mili toh client object ban jaata hai jo OpenAI API ke saath connect karta hai.