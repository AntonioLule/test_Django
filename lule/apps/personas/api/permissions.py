from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene permiso para realizar la accion (GET, POST, PUT O Delete)
        """
        # si quiere crear un usuario, sea quien sea
        from apps.personas.api.views import UserDetailAPI
        if request.method == "POST":
            return True
        # si no es POST, el superusuario siempre puede
        elif request.user.is_superuser:
            return True
        # si es un GET  ala vista de detalle, tomo la decision en has_object_permisions en
        elif isinstance(view, UserDetailAPI):
            return True
        else:
            # GET a api/1.0/users/
            return False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario autenticado en request.user tiene permiso para realizar la accion (GET, PUT O Delete)
        sobre el object
        """
        return request.user.is_superuser or request.user == obj
