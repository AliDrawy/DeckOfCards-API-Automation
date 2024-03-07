import requests


class DeckOfCardsAPI:

    def __init__(self):
        self.response = None
        self.base_url = "https://deckofcardsapi.com/api/deck"
        self.request = requests

    def get_url(self, endpoint=""):
        url = f"{self.base_url}/{endpoint}"
        self.api_get_request(url)

    def api_get_request(self, url):
        self.response = self.request.get(url)
        return self.response
