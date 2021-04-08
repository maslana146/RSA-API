import requests
from requests.auth import HTTPBasicAuth

""" Getting public and private keys from server. """
keys = requests.get("http://127.0.0.1:8000/keys", auth=HTTPBasicAuth('bartek', 'pass')).json()
pub_key = tuple(keys['pub_key'].values())
priv_key = tuple(keys['priv_key'].values())

"""Sample text to encrypt."""
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
print("Sample text to encrypt:", text)

"""Preparing encrypt model."""
data = {
    "text": text,
    "key": pub_key
}

"""Getting encrypted data."""
encrypt_data = requests.post("http://127.0.0.1:8000/encrypt_data", json=data).json()["result"]
print("Encrypted data:", *encrypt_data)

"""Preparing decode model."""
data = {
    "text": encrypt_data,
    "key": priv_key
}

"""Requesting for decoded data."""
decode_data = requests.post("http://127.0.0.1:8000/decode_data", json=data).json()["result"]

"""Checking that decoded data is equal to original text."""
if decode_data == text:
    print("Decoded data is equal to original:", True)
else:
    print("Decoded data is equal to original:", False)