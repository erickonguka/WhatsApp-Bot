import os
import google.generativeai as genai

# Gemini API KEY
genai.configure(api_key=os.environ["AI_API_KEY"])

# Facebook/WhatsApp Access Bearer Token
bearerToken = "your_bearer token"

# Fill here too
company_name="your company name"
agent_name="bot agent name"
currency="your currency"

# Use a more robust data storing mechanism like a database
base_dir = os.path.dirname(__file__)

# path to your training data/info about your company
training_data = os.path.join(base_dir, 'imports', 'training_data.txt') 

# path to whatsapp formatting options
formatting = os.path.join(base_dir, 'imports', 'formatting.txt')   
