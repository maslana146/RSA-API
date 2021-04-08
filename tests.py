import unittest
import requests
import rsa


class MyTestCase(unittest.TestCase):
    def test_sample_text(self):
        text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
        pub_key, priv_key = rsa.gen_key()
        encrypt_data = rsa.encrypt_rsa(text, pub_key)
        self.assertEqual(text, rsa.decode_rsa(encrypt_data, priv_key))

    def test_api_keys_no_auth(self):
        resp = requests.get("http://0.0.0.0:9000/keys")
        self.assertEqual(resp.status_code,401)

    def test_api_encrypt(self):
        text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
        data = {
            "text": text,
            "key": (3233,17)
        }
        encrypt_data = rsa.encrypt_rsa(text, (3233,17))
        self.assertEqual(requests.post("http://0.0.0.0:9000/encrypt_data",json=data).json()["result"],encrypt_data)


if __name__ == '__main__':
    unittest.main()
