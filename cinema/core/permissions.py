from rest_framework import permissions
from core import models


class IsDirectorOrAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow directorsof a show and admin to edit it.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True

        # disallow to create new episode/show/season for anyone except admin
        if request.method == "POST":
            return False

        return True

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True

        # allow director to make only deletes, full and partial updates
        if request.method not in ["DELETE", "PUT", "PATCH"]:
            return False

        print(request.user)

        if isinstance(obj, models.Episode):
            return obj.season.show.directors.filter(id=request.user.id).exists()

        elif isinstance(obj, models.Season):
            return obj.show.directors.filter(id=request.user.id).exists()

        elif isinstance(obj, models.Show):
            return obj.directors.filter(id=request.user.id).exists()

        return False
