import unittest
from unittest.mock import patch
import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(base_dir, 'src')  # Adjust 'src' as per your directory name
sys.path.append(src_dir)

from main import get_user_collection

# Your TestGetUserCollection class follows here...

class TestGetUserCollection(unittest.TestCase):
    @patch('main.requests.get')
    def test_get_user_collection_success(self, mock_get):
        # Mock response for user collection request
        mock_get.side_effect = [
            # First call to get user collection
            unittest.mock.Mock(status_code=200, content=b'<items><item objectid="1"><status own="1"/></item></items>'),
            # Second call to get game details
            unittest.mock.Mock(status_code=200, content=b'<items><item><poll name="suggested_numplayers"><results numplayers="1"><result value="Best" numvotes="5"/></results></poll><link type="boardgamecategory" value="Strategy"/></item></items>')
        ]

        collection = get_user_collection('testuser')
        self.assertEqual(len(collection), 1)  # Expecting one game in the collection
        self.assertEqual(collection[0]['game_id'], '1')  # Check if the game ID is correct
        self.assertEqual(collection[0]['best_at_player_count'], '1')  # Check if the best player count is correct
        self.assertIn('Strategy', collection[0]['game_types'])  # Check if game types include 'Strategy'

    @patch('main.requests.get')
    def test_get_user_collection_failure(self, mock_get):
        # Mock response for a failed request
        mock_get.return_value = unittest.mock.Mock(status_code=404)

        with self.assertRaises(Exception):
            get_user_collection('nonexistentuser')

if __name__ == '__main__':
    unittest.main()