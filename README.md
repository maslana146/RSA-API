# RSA - Rivest–Shamir–Adleman
created by: Bartosz Maślanka

[RSA - algorithm](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

A python program that creates FastAPI, which allows to encrypt / decode text using API requests.
To run the API server, user should type in to terminal `hypercorn api:app --reload -b "0.0.0.0:9000"`. 
When the server is running user can check if the RSA-API works correctly by executing get-api.py which downloads keys, 
encrypt sample text and then decodes it, or go to eg.`http://0.0.0.0:9000/keys`.

http://0.0.0.0:9000/keys -> get public, private key. User have to authenticate himself with basic auth.

http://0.0.0.0:9000/encrypt_data -> post text with public keys to encrypt text by RSA algorithm. Return encrypted text.

http://0.0.0.0:9000/decode_data -> post encrypted data with private key to decode text. Return decoded text.  

_rsa.py_ -> file which include RSA implementation.

_api.py_ -> FastAPI initialization.

_get_api.py_ -> sample python program which test an API server 

## Run by Docker
Firstly create local image, typing in terminal eg.  `docker build --tag rsa/fastapi .`.
Then type `docker run -p 9000:9000 rsa/fastapi`, after that server should be running and user can run get_api.py to 
check everything works well.


