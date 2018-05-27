from django.db.models import Count
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from core.models import Episode, Show, Season, Person
from core.permissions import IsDirectorOrAdminOrReadOnly
from core.serializer import EpisodeSerializer, SeasonSerializer, ShowSerializer, PersonSerializer


# Create your views here.


class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.order_by('id')
    serializer_class = EpisodeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsDirectorOrAdminOrReadOnly, ]


class ShowViewSet(viewsets.ModelViewSet):
    serializer_class = ShowSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsDirectorOrAdminOrReadOnly, ]

    def get_queryset(self):
        queryset = Show.objects.all()
        queryset = ShowSerializer.setup_eager_loading(queryset)
        return queryset


class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.annotate(episodes_count=Count("episodes")).order_by('id')
    serializer_class = SeasonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsDirectorOrAdminOrReadOnly, ]


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.order_by('id')
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsDirectorOrAdminOrReadOnly, ]


