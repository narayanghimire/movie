import json
from app.istorage import IStorage

class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def _load_data(self):
        """ method to load data from the JSON file. """
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _save_data(self, data):
        """ method to save data to the JSON file. """
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def list_movies(self):
        """
        Returns a list of movie
        """
        return self._load_data()

    def add_movie(self, title, year, rating, poster):
        """
        Adds a movie to the movies .
        """
        data = self._load_data()
        data[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_data(data)

    def delete_movie(self, title):
        """ Deletes a movie from the movies. """
        data = self._load_data()
        if title in data:
            del data[title]
            self._save_data(data)

    def update_movie(self, title, rating):
        """ Updates a movie in the movies. """
        data = self._load_data()
        if title in data:
            data[title]["rating"] = rating
            self._save_data(data)
