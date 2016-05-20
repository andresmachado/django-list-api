from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'lists', views.ListViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    url(r'^$', views.list_create, name="list_create"),
    url(r'api/v1/', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
