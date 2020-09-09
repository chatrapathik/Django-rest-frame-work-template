from rest_framework import routers

from .views import TaskViewSet, TaskSearch

_router = routers.SimpleRouter()
_router.register(r"api/v1/tasks", TaskViewSet)
_router.register(r"api/v1/tasks_search", TaskSearch)


urlpatterns = _router.urls
