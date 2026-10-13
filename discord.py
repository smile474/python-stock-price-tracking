import requests

def send_message(price, webhook_url):
    content = f"MSFT price = {price}"
    data = {
        "content":content
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print("Failed:", response.status_code, response.text)