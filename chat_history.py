import json

def save_chat_history(friend_name, chat_history):
    with open(f"{friend_name}.json", "w", encoding="utf-8") as f:
        json.dump(chat_history, f)

def load_chat_history(friend_name):
    try:
        with open(f"{friend_name}.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
