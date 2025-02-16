import requests

from config.settings import AWS_ACCESS_KEY, AWS_PROD_URL

class AWSContactHandler:
    CONTACTS_ENDPOINT = "/contacts"

    def __init__(self):
        self.api_url = AWS_PROD_URL + self.CONTACTS_ENDPOINT
        self.bearer_token = AWS_ACCESS_KEY

    def fetch_contacts(self):
        headers = {
            "Authorization": f"Bearer {self.bearer_token}"
        }
        response = requests.get(self.api_url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching contacts: {response.status_code}")
            return []
