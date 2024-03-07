import requests

from infra.api_wrapper import DeckOfCardsAPI


class DeckAPI:
    """A class for interacting with the Deck of Cards API."""

    def __init__(self):
        """Initialize the DeckAPI class."""
        self.url = DeckOfCardsAPI().base_url

    def get_url(self, endpoint=""):
        """Construct the API URL for a given endpoint."""
        return f"{self.url}/{endpoint}"

    def create_new_deck(self, shuffle=False, jokers_enabled=False, deck_count=1):
        """Create a new deck of cards."""
        parameters = {
            'jokers_enabled': 'true' if jokers_enabled else 'false',
            'deck_count': deck_count
        }
        endpoint = "new/shuffle/" if shuffle else "new/"
        response = requests.get(self.get_url(endpoint), params=parameters)
        if response.ok:
            return response.json()
        else:
            return response.status_code

    def shuffle_deck(self, deck_id):
        """Shuffle an existing deck."""
        response = requests.get(self.get_url(f"{deck_id}/shuffle/"))
        if response.ok:
            return response.json()
        else:
            return response.status_code

    def draw_cards(self, deck_id, count=2):
        """Draw cards from a deck."""
        response = requests.get(self.get_url(f"{deck_id}/draw/"), params={'count': count})
        if response.ok:
            return response.json()
        else:
            return response.status_code

    def add_cards_to_pile(self, deck_id, pile_name, deck):
        """Add cards to a pile within a deck."""
        parameters = {'deck': ','.join(deck)}
        response = requests.get(self.get_url(f"{deck_id}/pile/{pile_name}/add/"), params=parameters)
        if response.ok:
            return response.json()
        else:
            return response.status_code

    def draw_from_pile(self, deck_id, pile_name, count):
        """Draw cards from a pile within a deck."""
        response = requests.get(self.get_url(f"{deck_id}/pile/{pile_name}/draw/"), params={'count': count})
        if response.ok:
            return response.json()
        else:
            return response.status_code
