import os

import requests
import random

from dotenv import load_dotenv

from app.istorage import IStorage


class MovieApp:
    API_URL = "http://www.omdbapi.com/"

    def __init__(self, storage: IStorage):
        self._storage = storage
        load_dotenv()
        self.API_KEY = os.getenv('API_KEY')
        if not self.API_KEY:
            raise Exception("Movie API Key not found in environment variables.")

    def _fetch_movie_data(self, title):
        """Fetch movie data from OMDb API."""
        url = f'{self.API_URL}?apikey={self.API_KEY}&t={title}'
        response = requests.get(url)

        if response.status_code != 200:
            raise ConnectionError("Failed to connect to OMDb API")

        data = response.json()
        if data.get('Response') == 'False':
            raise ValueError("Movie not found")

        return {
            'title': data.get('Title'),
            'year': int(data.get('Year')),
            'rating': float(data.get('imdbRating')),
            'poster': data.get('Poster')
        }

    def _command_list_movies(self):
        """List all movies."""
        movies = self._storage.list_movies()
        for title, info in movies.items():
            print(f"Title: {title}, Year: {info['year']}, Rating: {info['rating']}, Poster: {info['poster']}")

    def _command_add_movie(self):
        """Add a movie using the OMDb API."""
        title = input("Enter the movie title: ")
        try:
            movie_data = self._fetch_movie_data(title)
            self._storage.add_movie(
                movie_data['title'],
                movie_data['year'],
                movie_data['rating'],
                movie_data['poster']
            )
            print(f"Movie '{title}' successfully added.")
        except ValueError as ve:
            print(ve)
        except ConnectionError as ce:
            print(ce)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _command_delete_movie(self):
        """Delete a movie."""
        title = input("Enter the title of the movie to delete: ")
        self._storage.delete_movie(title)
        print(f"Movie '{title}' deleted successfully.")

    def _command_stats(self):
        """Display movie statistics."""
        movies = self._storage.list_movies()
        ratings = [info['rating'] for info in movies.values()]
        average_rating = sum(ratings) / len(ratings) if ratings else 0
        print(f"Number of movies: {len(movies)}")
        print(f"Average rating: {average_rating:.2f}")

    def _command_random_movie(self):
        """Display a random movie."""
        movies = self._storage.list_movies()
        if movies:
            title = random.choice(list(movies.keys()))
            info = movies[title]
            print(
                f"Random Movie:\nTitle: {title}, Year: {info['year']}, Rating: {info['rating']}, Poster: {info['poster']}")
        else:
            print("No movies available.")

    def _command_search_movie(self):
        """Search for a movie by title."""
        title = input("Enter the title of the movie to search: ")
        movies = self._storage.list_movies()
        if title in movies:
            info = movies[title]
            print(
                f"Found Movie:\nTitle: {title}, Year: {info['year']}, Rating: {info['rating']}, Poster: {info['poster']}")
        else:
            print("Movie not found.")

    def _command_movies_sorted_by_rating(self):
        """List movies sorted by rating."""
        movies = self._storage.list_movies()
        sorted_movies = sorted(movies.items(), key=lambda x: x[1]['rating'], reverse=True)
        for title, info in sorted_movies:
            print(f"Title: {title}, Year: {info['year']}, Rating: {info['rating']}, Poster: {info['poster']}")

    def _command_generate_website(self):
        """Generate an HTML website with the movie list."""
        movies = self._storage.list_movies()
        movie_items = ""

        for title, info in movies.items():
            movie_items += f"""
            <li class="movie">
                <img class="movie-poster" src="{info['poster']}" alt="Poster of {title}">
                <div class="movie-title">{title}</div>
                <div class="movie-year">{info['year']}</div>
            </li>
            """

        template_path = os.path.join(os.path.dirname(__file__), '..', '_static', 'index_template.html')
        with open(template_path, 'r', encoding='utf-8') as template_file:
            template_content = template_file.read()

        output_content = template_content.replace('__TEMPLATE_TITLE__', 'My Movie List').replace(
            '__TEMPLATE_MOVIE_GRID__', movie_items)

        output_path = os.path.join(os.path.dirname(__file__), '..', 'movies.html')
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(output_content)

        print("Website generated successfully")

    def run(self):
        """Run the movie application."""
        while True:
            print("\nMovie Application")
            print("0. Exit")
            print("1. List movies")
            print("2. Add movie")
            print("3. Delete movie")
            print("4. Update movie")
            print("5. Stats")
            print("6. Random movie")
            print("7. Search movie")
            print("8. Movies sorted by rating")
            print("9. Generate website")

            choice = input("Enter your choice (0-9): ")

            if choice == '0':
                print("Exiting the application.")
                break
            elif choice == '1':
                self._command_list_movies()
            elif choice == '2':
                self._command_add_movie()
            elif choice == '3':
                self._command_delete_movie()
            elif choice == '4':
                print("Update movie functionality is not available.")
            elif choice == '5':
                self._command_stats()
            elif choice == '6':
                self._command_random_movie()
            elif choice == '7':
                self._command_search_movie()
            elif choice == '8':
                self._command_movies_sorted_by_rating()
            elif choice == '9':
                self._command_generate_website()
            else:
                print("Invalid choice. Please try again.")
