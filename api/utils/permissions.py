from rest_framework import permissions

class IsAnonymous(permissions.BasePermission):
    message = 'Logout before you perform this action.'

    def has_permission(self, request, view):
         return request.user.is_anonymous()
