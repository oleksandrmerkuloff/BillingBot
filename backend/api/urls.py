from rest_framework import routers

from api.views import MeterViewSet, ReportViewSet


api_router = routers.SimpleRouter()
api_router.register('meters', MeterViewSet)
api_router.register('reports', ReportViewSet)


urlpatterns = api_router.urls
