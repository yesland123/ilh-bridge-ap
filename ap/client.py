import requests

class APClient:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.base_url = "https://api.autopartner-api.com"  # on remplacera par la bonne URL

    def login(self):
        payload = {
            "username": self.username,
            "password": self.password
        }
        r = self.session.post(self.base_url + "/login", json=payload)
        return r.json()

    def search(self, reference: str):
        payload = {"search": reference}
        r = self.session.post(self.base_url + "/search", json=payload)
        return r.json()
