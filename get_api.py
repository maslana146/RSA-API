import requests
from requests.auth import HTTPBasicAuth

keys = requests.get("http://127.0.0.1:8000/keys",auth=HTTPBasicAuth('bartek', 'pass')).json()

pub_key = tuple(keys['pub_key'].values())
priv_key = tuple(keys['priv_key'].values())

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# print(pub_key)

data = {
    "text": text,
    "key": pub_key
}
encrypt_data = requests.post("http://127.0.0.1:8000/encrypt_data",json=data).json()["result"]


data = {
    "text": encrypt_data,
    "key": priv_key
}

decode_data = requests.post("http://127.0.0.1:8000/decode_data",json=data).json()["result"]

if decode_data == text:
    print(True)
else:
    print(False)


