from rest_framework import permissions
from images.models import Images


class Basic(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        return True


class Premium(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.user.is_staff:
            if request.user.has_perm('Images.view_image'): #'app_name.action_model_name' - action -np dodawanie images
                return True
            if request.user.has_perm('Images.add_image'):
                return True
            return False
        return False


class Enterprise(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        return True


class Admin(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            if request.user.has_perm('Images.view_image'): #'app_name.action_model_name' - action -np dodawanie images
                return True
            if request.user.has_perm('Images.delete_image'):
                return True
            if request.user.has_perm('Images.change_image'):
                return True
            if request.user.has_perm('Images.add_image'):
                return True
            return True
        return False