from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Allows access only to Owner users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.OWNER)

class IsOwnerOrDealer(BasePermission):
    """
    Allows access only to Owner and Dealer users.
    """

    def has_permission(self, request, view):
        return bool(request.user and (request.user.OWNER or request.user.DEALER))