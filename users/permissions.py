from rest_framework import permissions


class AnonPermissionOnly(permissions.BasePermission):
    message = "You are already authenticated"
    """
    Non-authenticated users only
    """

    def has_permission(self, request, view):
        # ip_addr = request.META['REMOTE_ADDR']
        # blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not request.user.is_authenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an owner attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named owner.
        return obj.user == request.user


class RolePermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user.type)
        if request.user.type == 'ADMIN':
            return True