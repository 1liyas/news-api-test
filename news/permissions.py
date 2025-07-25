from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsPublishedOrReadOnly(BasePermission):
    """
    Разрешает доступ только к опубликованным новостям (GET),
    редактировать/удалять может только админ.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return obj.is_published
        return False
