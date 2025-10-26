from rest_framework import permissions

class IsSuperUserForUpdate(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['update', 'partial_update']:
            return request.user and request.user.is_superuser
        return True