import pytest
from viewing_party.movie import Movie 

def test_create_movie():
    # Arrange
    title = "Lion King"
    genre = "action"
    rating = 5
    host = "Netflix"

    # Act
    movie = Movie(title, genre, rating, host)
    
    # Assert
    assert movie.title == title 
    assert movie.genre == genre
    assert movie.rating == rating
    assert movie.host == host 

def test_update_rating_of_movie():
    # Arrange
    title = "Lion King"
    genre = "action"
    rating = 4
    host = "Netflix"


    # Act
    movie = Movie(title, genre, rating, host)
    movie.update_rating(rating)


    # Assert
    assert movie.rating == 4


