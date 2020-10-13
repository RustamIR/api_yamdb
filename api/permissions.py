from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.models import Users



class AdminPermissions(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == request.user.ADMIN or request.user.is_staff



class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Users.MODERATOR



class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class TitleAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return (request.user.role == request.user.ADMIN
                    or request.user.is_staff)
        else:
            return False


class ForReviewPerm(BasePermission):
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user
                and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if (request.user.is_staff or
                    request.user.role == Users.ADMIN or
                    request.user.role == Users.MODERATOR or
                    obj.author == request.user or
                    request.method == 'POST' and
                    request.user.is_authenticated):
                return True
        return request.method in SAFE_METHODS

