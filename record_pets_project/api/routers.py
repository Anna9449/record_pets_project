from rest_framework import routers


class CustomRouter(routers.SimpleRouter):
    """
    Кастомный роутер, который:
        - пропускает метод 'delele' по урлу {basename}-list
        - ограничивает работу с урлами формата {basename}-detail
    """

    routes = [
        routers.Route(
            url=r'^{prefix}/$',
            mapping={'get': 'list',
                     'post': 'create',
                     'delete': 'destroy'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        routers.DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}/$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        )
    ]
