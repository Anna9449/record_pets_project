from drf_spectacular.utils import OpenApiResponse


response_400 = OpenApiResponse(
    response=None,
    description='Проверьте корректность введенных данных.'
)

response_401 = OpenApiResponse(
    response=None,
    description='Необходимо авторизоваться.'
)
