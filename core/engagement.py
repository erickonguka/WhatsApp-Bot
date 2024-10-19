import os
from config import genai, agent_name, company_name, currency
from conversation import get_conversation_history, add_to_conversation_history

base_dir = os.path.dirname(__file__)

#link to your training data/info about your company
training_data = os.path.join(base_dir, 'imports', 'training_data.txt') 

#link to whatsapp formatting options
formatting = os.path.join(base_dir, 'imports', 'formatting.txt')    

def getTxt(path):
    try:
        with open(path, "r") as file:
             result = file.read()
             return result
        
    except Exception as e:
        print(f"Error reading data file: {e}")
        return "Sorry, something went wrong while accessing the data."

def engage_user(user_name, message, user_id):
    
    user_history = get_conversation_history(user_id)
    history_context = "\n".join([f"User: {msg['user']}\n{agent_name}: {msg['assistant']}" for msg in user_history])

    # You could also modify further here for clear prompting
    full_message = f"""
    You are {agent_name}, professional sales agent for {company_name}. Engage with {user_name}:

    Do:
    - Be interactive, direct, and insightful
    - Use concise, direct simple language
    - Follow pricing table for project budget estimation
    - Currency {currency} also known as bob
    - Close sales with:
      1. Formatted project summary
      2. Clear requirements
      3. Effective contact us call to action, (emails, phone, website)

    Avoid:
    - Long introductions or redundancy
    - Long texts
    - Selling unavailable services
    - Repeating replies or processes
    - Overpushing the client
    - Excessive client name mentions

    User query: {message}

    Here's the Conversation history:
    {history_context}

    {company_name} info:
    {getTxt(training_data)}

    \n\n{getTxt(formatting)}
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    try:
        response = model.generate_content(full_message)
        add_to_conversation_history(user_id, message, response.text)
        return response.text
    except Exception as e:
        print(f"Error engaging user: {e}")
        return "Sorry, something went wrong. Please try again."
