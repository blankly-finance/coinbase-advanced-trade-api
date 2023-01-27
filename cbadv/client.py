import requests


class Client:
    def __init__(self, api_key: str, secret_key: str, sandbox: bool):
        requests.get('https://api.pro.coinbase.com/products/')
