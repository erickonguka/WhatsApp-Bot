from config import bearerToken
import requests

def send_message(user_id, message):
    try:
        url = "https://graph.facebook.com/v20.0/448573481671182/messages"
        headers = {
            "Authorization": "Bearer " + bearerToken,
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": user_id,
            "type": "text",
            "text": {
                "body": message 
            }
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print(f"Message sent to {user_id}")
        else:
            print(f"Failed to send message to {user_id}: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error sending message to {user_id}: {e}")
