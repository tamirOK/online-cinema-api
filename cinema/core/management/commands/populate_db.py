from django.core.management.base import BaseCommand

from core.models import Episode, Season, Show, Person
from mimesis import Person as RandomPerson, Datetime, Address, Text
from mimesis.enums import Gender
import random


class Command(BaseCommand):
    """
        Command for poppulating database with test data
    """
    person_gen = RandomPerson('en')
    date_gen = Datetime()
    country_gen = Address()
    show_gen = Text()

    def _create_persons(self, amount=10):
        result = []

        for _ in range(amount):
            gender = random.choice([Gender.MALE, Gender.FEMALE])
            short_gender = 'M' if gender is Gender.MALE else 'F'

            actor = Person(
                username=self.person_gen.username(),
                first_name=self.person_gen.name(gender=gender),
                last_name=self.person_gen.last_name(gender=gender),
                email=self.person_gen.email(),
                gender=short_gender,
                birth_date=self.date_gen.datetime().date(),
                country=self.country_gen.country()
            )
            password = Person.objects.make_random_password()
            actor.set_password(password)
            actor.save()

            result.append(actor)

        return result

    def _create_shows(self, directors, actors, amount=10, directors_per_show=3, actors_per_show=10):
        result = []

        for _ in range(amount):
            show = Show(
                name=self.show_gen.word(),
                released_date=self.date_gen.datetime().date(),
                description=self.show_gen.text(quantity=2)
            )
            show.save()
            show_directors = [random.choice(directors) for _ in range(directors_per_show)]
            show_actors = [random.choice(actors) for _ in range(actors_per_show)]

            show.directors.add(*show_directors)
            show.actors.add(*show_actors)

            result.append(show)

        return result

    def _create_seasons(self, shows, seasons_per_show):
        result = []

        for show in shows:
            current_show_seasons_number = random.choice(seasons_per_show)
            for season_number in range(current_show_seasons_number):
                season = Season(
                    season_number=season_number,
                    description=self.show_gen.text(quantity=1),
                    show=show
                )
                season.save()
                result.append(season)

        return result

    def _create_episodes(self, seasons, episodes_per_season):
        for season in seasons:
            for episode_number in range(episodes_per_season):
                episode = Episode(
                    episode_number=episode_number,
                    name=self.show_gen.title(),
                    season=season,
                    description=self.show_gen.text(quantity=1),
                    released_date=self.date_gen.datetime().date(),
                )
                episode.save()

    def handle(self, *args, **options):
        actors = self._create_persons(amount=100)
        directors = self._create_persons(amount=10)
        shows = self._create_shows(directors, actors, amount=20)
        seasons = self._create_seasons(shows, seasons_per_show=range(5, 11))
        self._create_episodes(seasons, episodes_per_season=10)