# Movie  Application

## Overview

A Python application for managing movies with for listing, adding, deleting, and generating HTML reports, 
using JSON/CSV storage using OMDb API.

## Features

- List all movies in the collection
- Add a new movie by fetching details from the OMDb API
- Delete a movie 
- Display movie statistics (e.g., average rating)
- Show a random movie
- Search for a movie
- List movies sorted by rating
- Generate an HTML website to display the movie

## Installation

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/narayanghimire/movie.git
    cd movie
    ```

2 **Install Dependencies**

 ```bash
  pip install -r requirements.txt
 ```


4. **Set Up Environment Variables**

    Create a `.env` file in the root directory of the project and add your OMDb API key:

    ```
    API_KEY=omdb_api_key
    ```

## Usage

1. **Run the Application**

    ```bash
    python3 main.py
    ```

2. **Commands**

    - `0`: Exit 
    - `1`: List movies
    - `2`: Add new movie
    - `3`: Delete movie
    - `4`: Update movie
    - `5`: Stats
    - `6`: Random movie
    - `7`: Search movie 
    - `8`: Movies sorted by rating
    - `9`: Generate website

## Project Structure

- `app/`
  - `__init__.py`: Package initialization
  - `movie_app.py`: Contains the `MovieApp` class
  - `istorage.py`: Defines the `IStorage` interface
- `storage/
  - `storage_json.py`: JSON storage implementation
  - `storage_csv.py`: CSV storage implementation
- `tests/`
  - `test_storage_csv.py`: Unit tests for CSV storage
- `_static/`
  - `index_template.html`: HTML template for generating the website
  - `style/`
    - `style.css`: CSS file for styling the website
- `.env`: Environment variables file
- `main.py`: Entry point for the application
- `requirements.txt`: List of project dependencies
- `README.md`: Project documentation

