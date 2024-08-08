import csv
from app.istorage import IStorage


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def _load_data(self):
        """Load data from the CSV file."""
        data = {}
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row.get('title')
                    if title:
                        data[title] = {
                            'rating': float(row.get('rating', 0)),
                            'year': int(row.get('year', 0)),
                            'poster': str(row.get('poster', 0))
                        }
        except FileNotFoundError:
            pass
        return data

    def _save_data(self, data):
        """save data to the CSV file."""
        with open(self.file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'rating', 'year', 'poster'])
            for title, info in data.items():
                writer.writerow([title, info['rating'], info['year'], info['poster']])

    def list_movies(self):
        """Returns a list of movie"""
        return self._load_data()

    def add_movie(self, title, year, rating, poster):
        """Adds a movie to the movies."""
        data = self._load_data()
        data[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_data(data)

    def delete_movie(self, title):
        """Deletes a movie from the movies."""
        data = self._load_data()
        if title in data:
            del data[title]
            self._save_data(data)

    def update_movie(self, title, rating):
        """Updates a movie in the movies."""
        data = self._load_data()
        if title in data:
            data[title]["rating"] = rating
            self._save_data(data)
