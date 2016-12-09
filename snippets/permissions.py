from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission that allows the owner of the object to edit/delete it
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        # GET, HEADS, OPTIONS requests are allowed
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
