from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """
        Returns a list of movie
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """
        Adds a movie to the movies .
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        Deletes a movie from the movies.
        """
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """
        Updates a movie in the movies.
        """
        pass
