from google import genai
import sys
import os
from google.genai import types


# Add the project root to the Python path to make config.py importable
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import GEMINI_API_KEY

sys_instruct="You only deal with questions in context of programming, AI and software engineering.  For other category of questions, reply politely that you are not aware of the context."
name = input("Enter your query: ")
client = genai.Client(api_key=GEMINI_API_KEY)
response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents=[name], 
    config=types.GenerateContentConfig(
        system_instruction=sys_instruct),
)
print(response.text)
