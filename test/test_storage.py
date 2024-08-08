import unittest
import os
from app.storage_json import StorageJson


class TestStorageJson(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setup test environment."""
        cls.file_path = 'test_movies.json'
        cls.storage = StorageJson(cls.file_path)

    def setUp(self):
        """Setup before each test method."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_add_movie(self):
        """Test adding a movie."""
        self.storage.add_movie('xxxxx', 1999, 9, 'yyyyy.jpg')
        movies = self.storage.list_movies()
        self.assertIn('xxxxx', movies)
        self.assertEqual(movies['xxxxx'], {'year': 1999, 'rating': 9, 'poster': 'yyyyy.jpg'})

    def test_update_movie(self):
        """Test updating a movie."""
        self.storage.add_movie('wesfderdf', 2010, 8, 'wefdgwefds.jpg')
        self.storage.update_movie('wesfderdf', 9)
        movies = self.storage.list_movies()
        self.assertEqual(movies['wesfderdf']['rating'], 9)

    def test_delete_movie(self):
        """Test deleting a movie."""
        self.storage.add_movie('qwregfd', 1999, 9, 'werfdsxc.jpg')
        self.storage.delete_movie('qwregfd')
        movies = self.storage.list_movies()
        self.assertNotIn('qwregfd', movies)

    @classmethod
    def tearDownClass(cls):
        """Cleanup after all tests."""
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)


if __name__ == '__main__':
    unittest.main()
