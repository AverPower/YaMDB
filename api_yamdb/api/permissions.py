from rest_framework import permissions


class RolePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        required_roles = view.permission_groups.get(view.action)
        if required_roles is None:
            return False
        if 'anon' in required_roles:
            return True
        if not request.user.is_authenticated:
            return False
        return request.user.role in required_roles


class CurrentUserPermission(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.user.username == obj.username:
            return True
        return False


class RoleAuthCurrentUserPermission(RolePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == 'user':
            if request.user.username == obj.author.username:
                return True
            return False
        return True
