from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        role = request.user.profile.role

        if request.method in ['GET']:
            return True

        if role == 'admin':
            return True

        return False