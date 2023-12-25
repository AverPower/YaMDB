from rest_framework import permissions


class HasGroupPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        required_groups = view.permission_groups.get(view.action)
        if required_groups is None:
            return False
        elif '_Public' in required_groups:
            return True
        return request.role in required_groups
