import os
import json
from collections import deque

base_dir = os.path.dirname(__file__)
HISTORY_FILE = os.path.join(base_dir, 'exports', 'conversation_history.json')

def load_conversation_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {} 

def save_conversation_history(history):
    try:
        with open(HISTORY_FILE, 'w') as file:
            json.dump(history, file, indent=4)
    except Exception as e:
        print(f"Error saving conversation history: {e}")

full_conversation_history = load_conversation_history()

conversation_history = {}

def get_conversation_history(user_id):
    return conversation_history.get(user_id, [])

def add_to_conversation_history(user_id, user_message, assistant_message):
    if user_id not in conversation_history:
        conversation_history[user_id] = deque(maxlen=3)
    
    conversation_history[user_id].append({
        'user': user_message,
        'assistant': assistant_message
    })
    
    if user_id not in full_conversation_history:
        full_conversation_history[user_id] = []
    
    full_conversation_history[user_id].append({
        'user': user_message,
        'assistant': assistant_message
    })
    
    save_conversation_history(full_conversation_history)