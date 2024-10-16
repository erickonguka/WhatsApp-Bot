from flask import Flask, request, jsonify
import os
import sys

current_dir = os.path.dirname(__file__)
core = os.path.join(current_dir, 'core')
sys.path.append(core)

from core import engage_user, load_user_data, save_user_data, send_message

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        hub_mode = request.args.get('hub.mode')
        hub_challenge = request.args.get('hub.challenge')
        hub_verify_token = request.args.get('hub.verify_token')
        if hub_mode == 'subscribe' and hub_verify_token == 'pass':
            return hub_challenge, 200
        else:
            return "Verification token mismatch", 403
    elif request.method == 'POST':
        try:
            data = request.get_json()
            if 'messages' in data['entry'][0]['changes'][0]['value']:
                messages = data['entry'][0]['changes'][0]['value']['messages']
                user_data = load_user_data()

                for message in messages:
                    user_id = message['from']
                    user_name = data['entry'][0]['changes'][0]['value']['contacts'][0].get('profile', {}).get('name', 'User')
                    user_data[user_id] = {'name': user_name}
                    save_user_data(user_data)

                    if 'text' in message:
                        user_message = message['text']['body']
                        response_message = engage_user(user_name, user_message, user_id)
                    else:
                        response_message = "Currently, I only support text messages. Please send a text message."

                    send_message(user_id, response_message)

            return jsonify({'status': 'success'}), 200
        except Exception as e:
            print(f"Error in webhook processing: {e}")
            return jsonify({'status': 'error', 'message': str(e)}), 500
        
if __name__ == '__main__':
    app.run(port=8000)
