from django.conf import settings

from rest_framework_api_key.permissions import HasAPIKey


class CustomHasAPIKey(HasAPIKey):
    """
    Кастомный пермишен, расширяет возможности доступа пакета
    rest_framework_api_key.
    Дополнительно дает возможность аутентифицироваться по ключу API_KEY
    из настроек проекта.
    """

    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return True
        return self.get_key(request) == settings.API_KEY
