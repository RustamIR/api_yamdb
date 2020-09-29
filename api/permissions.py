from rest_framework import permissions
from rest_framework.permissions import BasePermission


class AdminPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, ):
        return request.user.is_authenticated and request.user.is_admin
