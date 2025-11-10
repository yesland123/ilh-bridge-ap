import requests
from requests.auth import HTTPBasicAuth

class APClient:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.session = requests.Session()

        # ✅ L’URL officielle de l’API AP (SOAP)
        self.base_url = "https://b2b.autopartner.com.pl/api/v2/soap/"

    def request(self, action: str, body_xml: str):
        """
        Envoie une requête SOAP vers AutoPartner
        """
        headers = {
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": action
        }

        response = self.session.post(
            self.base_url,
            headers=headers,
            data=body_xml.encode("utf-8"),
            auth=HTTPBasicAuth(self.username, self.password)
        )

        return response.text  # on parse ensuite

    def search(self, reference: str):
        """
        Recherche d'une référence via AP (SOAP)
        """
        body = f"""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:api="http://autopartner.com.pl/api">
           <soapenv:Header/>
           <soapenv:Body>
              <api:getArticleByReference>
                 <api:reference>{reference}</api:reference>
              </api:getArticleByReference>
           </soapenv:Body>
        </soapenv:Envelope>
        """

        result = self.request("getArticleByReference", body)
        return result
