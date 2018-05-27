from django.contrib.auth.hashers import make_password
from django.core.exceptions import NON_FIELD_ERRORS
from rest_framework import serializers
from core import models
from core.models import Person


class SeasonSerializer(serializers.ModelSerializer):
    episodes_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Season
        fields = ('id', 'season_number', 'description', 'show', "episodes_count")
        read_only_fields = ("id", "episodes_count")


class ShowSerializer(serializers.ModelSerializer):

    @staticmethod
    def setup_eager_loading(queryset):
        return queryset.prefetch_related("actors", "directors")

    class Meta:
        model = models.Show
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):

    def validate_username(self, username):
        if len(username) < 6:
            raise serializers.ValidationError("Username must be 6 length long")
        return username

    def validate_password(self, password):
        if len(password) < 6:
            raise serializers.ValidationError("Password must be 6 length long")
        return password

    def create(self, validated_data):
        return Person.objects.create(
            password=make_password(validated_data.pop('password')),
            **validated_data
        )

    def update(self, instance, validated_data):
        # hash password if user wants to update it
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super().update(instance, validated_data)

    class Meta:
        model = models.Person
        fields = ("id", "username", "password", 'first_name', 'last_name', 'email', 'birth_date', 'gender', 'country')
        read_only_fields = ("id",)
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Episode
        fields = ('id', 'episode_number', 'name', 'season', 'description', 'released_date',)
