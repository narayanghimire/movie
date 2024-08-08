from app.storage_csv import StorageCsv
from app.movie_app import MovieApp


def main():
    #storage = StorageJson('movies.json')
    #movie_app = MovieApp(storage)
    #movie_app.run()

    storage = StorageCsv('storage/movies.csv')
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()
