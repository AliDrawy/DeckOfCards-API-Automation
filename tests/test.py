import unittest
from logic.deck_endpoints import DeckAPI


class CardDeckAPITestCase(unittest.TestCase):
    """Tests for the CardDeckAPI class."""

    def setUp(self):
        """Instantiate CardDeckAPI for testing."""
        self.deck_api = DeckAPI()

    def test_create_new_deck_without_jokers(self):
        """Test creating a new deck without including jokers."""
        response = self.deck_api.create_new_deck(shuffle=False, jokers_enabled=False)
        self.assertTrue(response['success'])
        self.assertEqual(response['remaining'], 52)

    def test_create_new_deck_with_jokers(self):
        """Test creating a new deck including jokers."""
        response = self.deck_api.create_new_deck(shuffle=False, jokers_enabled=True)
        self.assertTrue(response['success'])
        self.assertEqual(response['remaining'], 54)

    def test_shuffle_deck(self):
        """Test shuffling a new deck."""
        deck = self.deck_api.create_new_deck()
        response = self.deck_api.shuffle_deck(deck['deck_id'])
        self.assertTrue(response['success'])
        self.assertTrue(response['shuffled'])

    def test_draw_more_cards_than_remaining_in_deck(self):
        """Test trying to draw more deck than remaining in the deck."""
        deck = self.deck_api.create_new_deck(shuffle=True)
        remaining_cards = deck['remaining']
        response = self.deck_api.draw_cards(deck['deck_id'], count=remaining_cards + 1)
        self.assertFalse(response['success'])

    def test_draw_from_empty_pile(self):
        """Test trying to draw deck from an empty pile."""
        deck = self.deck_api.create_new_deck(shuffle=True)
        pile_name = "empty_pile"
        self.deck_api.add_cards_to_pile(deck['deck_id'], pile_name, deck)
        response = self.deck_api.draw_from_pile(deck['deck_id'], pile_name, count=2)
        self.assertNotEqual(response, 200)

    def test_draw_from_nonexistent_pile(self):
        """Test trying to draw deck from a nonexistent pile."""
        deck = self.deck_api.create_new_deck(shuffle=True)
        nonexistent_pile_name = "nonexistent_pile"
        response = self.deck_api.draw_from_pile(deck['deck_id'], nonexistent_pile_name, count=2)
        self.assertNotEqual(response, 200)
