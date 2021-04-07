from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import rsa


class EncryptData(BaseModel):
    text: str
    key: tuple


class DecodeData(BaseModel):
    text: list
    key: tuple


app = FastAPI()
security = HTTPBasic()


@app.get('/keys')
def get_key(credentials: HTTPBasicCredentials = Depends(security)):
    pub_key, priv_key = rsa.gen_key()
    return {"user": credentials.username,
            "pub_key": {"n": pub_key[0],
                        "e": pub_key[1]},
            "priv_key": {"n": priv_key[0],
                         "d": priv_key[1]}}


@app.post('/encrypt_data')
async def encrypt_data(encryptData: EncryptData):
    result = rsa.encrypt_rsa(encryptData.text, encryptData.key)
    return {"result": result}


@app.post('/decode_data')
async def decode_data(decodeData: DecodeData):
    result = rsa.decode_rsa(decodeData.text, decodeData.key)
    return {"result": result}
