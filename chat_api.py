import requests

def get_ai_response(message):
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + message
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("content")
    return "Error: 无法获取回复"
