from rest_framework.permissions import BasePermission, SAFE_METHODS



class AdminPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == request.user.ADMIN or request.user.is_staff:
            return True
        return False


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == request.user.MODERATOR:
            return True
        return False


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
            return request.user.role == request.user.ADMIN \
                   or request.user.is_staff
        else:
            return False
