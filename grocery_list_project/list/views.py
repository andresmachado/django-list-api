from django.contrib.auth import get_user_model

from rest_framework import viewsets, authentication, permissions

from .models import List, Product
from .serializers import ListSerializer, UserSerializer, ProductSerializer

User = get_user_model()


class DefaultMixin(object):
    """
    Defaul settings for authentication, permissions and filters
    """

    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 10
    paginate_by_param = 'page-size'
    max_paginate_by = 100


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset provides list and details actions for Users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListViewSet(DefaultMixin, viewsets.ModelViewSet):
    """
    API endpoint for listing and creating lists
    """

    queryset = List.objects.all()
    serializer_class = ListSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ProductViewSet(DefaultMixin, viewsets.ModelViewSet):
    """
    API endpoint edit, create, delete and update list products
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
