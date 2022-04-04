import pytest
from viewing_party.person import Person
from viewing_party.movie import Movie 

def test_create_person():
    # Arrange
    name = "Nishat"
    watched = []
    friends = []
    subscriptions = []

    # Act
    person = Person(name, watched, friends, subscriptions)
    
    # Assert
    assert person.name == name
    assert person.watched == watched
    assert person.friends == friends
    assert person.subscriptions == subscriptions


def test_add_watched_movie_to_empty_watched_list():
    # Arrange
    name = "Nishat"
    watched = []
    friends = []
    subscriptions = []

    title = "Lion King"
    genre = "action"
    rating = 5
    host = "Netflix"

    # Act
    person = Person(name, watched, friends, subscriptions)
    movie = Movie(title, genre, rating, host)
    person.add_watched(movie)

    # Assert
    assert movie in person.watched
    #assert len(person.watched) == 1

def test_length_of_num_watched():
    # Arrange
    name = "Nishat"
    watched = ["Lion King", ]
    friends = []
    subscriptions = []

    title = "Tangled"
    genre = "comedy"
    rating = 5
    host = "Disney Plus"

    # Act
    person = Person(name, watched, friends, subscriptions)
    movie = Movie(title, genre, rating, host)
    person.add_watched(movie)

    # Assert
    #assert movie in person.watched
    assert len(person.watched) == 2