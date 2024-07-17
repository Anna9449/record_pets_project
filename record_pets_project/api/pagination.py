from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.LimitOffsetPagination):
    """Кастомный пагинатор с измененной структурой ответа."""

    default_limit = 20

    def get_paginated_response(self, data):
        return Response({
            'count': self.count,
            'items': data
        })
