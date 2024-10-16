import json
import os

base_dir = os.path.dirname(__file__)
USER_DATA_FILE = os.path.join(base_dir, 'exports', 'user_data.json')

def load_user_data():
    try:
        if os.stat(USER_DATA_FILE).st_size == 0:
            return {}
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}

def save_user_data(data):
    try:
        with open(USER_DATA_FILE, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        print(f"Error saving user data: {e}")
