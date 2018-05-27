import pytest
from core.models import Person
import json

# Create your tests here.
from django.core.management import call_command

from core.models import Show, Season, Episode

@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'data.json')


def test_creating_person_by_anonymous_person(db, client):
    """
        Anonymous person cannot create new person.
    """
    new_user_data = json.dumps({
        "username": "new_username",
        "password": "randompassword",
        "gender": "M"
    })
    response = client.post("/persons/", new_user_data, content_type="application/json")
    data = json.loads(response.content)

    assert response.status_code == 403 and data["detail"] == "Authentication credentials were not provided."


def test_creating_person_by_admin(db, client):
    """
        Only admin can create new person. Admin login is 'tamirok'
    """
    client.login(username="tamirok", password="maddijane")
    new_user_data = json.dumps({
        "username": "new_username",
        "password": "randompassword",
        "gender": "M"
    })
    response = client.post("/persons/", new_user_data, content_type="application/json")
    data = json.loads(response.content)

    # checking that response is successful
    assert response.status_code == 201 and data["username"] == "new_username" and data["gender"] == "M"

    new_user_id = data["id"]

    # get information about new created user
    response = client.get(f"/persons/{new_user_id}/", content_type="application/json")
    data = json.loads(response.content)
    assert response.status_code == 200 and data["username"] == "new_username" and data["gender"] == "M"


def test_deleting_episode_by_director(db, client):
    """
        Only director of the show and admin can edit and delete episodes
    """
    # login as existing director
    client.login(username="custom", password="custom")
    director = Person.objects.get(username="custom")
    assert director.check_password("custom")
    # checking that director manages some shows
    assert Show.objects.filter(directors=director).exists()

    show = Show.objects.filter(directors=director).first()
    episode = show.seasons.first().episodes.first()

    # removing episode
    response = client.delete(path=f"/episodes/{episode.id}/")

    assert response.status_code == 204

    response = client.get(path=f"/episodes/{episode.id}/")

    # checking that deleted episode does not exist
    assert response.status_code == 404