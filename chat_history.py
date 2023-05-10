import os
import json

def save_chat_history(friend_name, chat_history):
    os.makedirs('chat_histories', exist_ok=True)
    with open(f"chat_histories/{friend_name}.json", "w", encoding="utf-8") as f:
        json.dump(chat_history, f)

def load_chat_history(friend_name):
    try:
        with open(f"chat_histories/{friend_name}.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
