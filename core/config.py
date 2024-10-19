import os
import google.generativeai as genai
genai.configure(api_key=os.environ["AI_API_KEY"])

bearerToken = "your_bearer token"
company_name="your company name"
agent_name="bot agent name"
