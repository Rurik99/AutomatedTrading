import requests


def analyze_text(input_text):
    response = requests.post('http://127.0.0.1:8000/classify', json={'title': input_text})
    return response.json()

