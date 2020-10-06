from rest_framework import permissions
from rest_framework.permissions import BasePermission

class AdminPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == request.user.ADMIN or request.user.is_staff:
            return True
        return False


