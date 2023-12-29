from rest_framework import permissions


class RolePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        required_roles = view.permission_groups.get(view.action)
        if required_roles is None:
            return False
        if required_roles.get('anon'):
            return True
        if not request.user.is_authenticated:
            return False
        return request.user.role in required_roles


class CurrentUserPermission(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.user.username == obj.username:
            return True
        return False
