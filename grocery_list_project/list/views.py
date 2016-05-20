from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from rest_framework import viewsets, authentication, permissions
from rest_framework import filters

from .forms import ListFormSet, CreateListForm
from .models import List, Product
from .serializers import ListSerializer, UserSerializer, ProductSerializer

User = get_user_model()


def list_create(request, template_name="lists/list_create.html"):
    # lists = List.objects.all()
    if request.method == 'POST':
        form = CreateListForm(request.POST or None)
        if form.is_valid():
            grocery_list = form.save(commit=False)
            grocery_list.creator = request.user
            products_formset = ListFormSet(request.POST, instance=grocery_list)
            if products_formset.is_valid():
                grocery_list.save()
                products_formset.save()
                return HttpResponseRedirect(reverse('list_create'))
    else:
        form = CreateListForm()
        products_formset = ListFormSet(instance=List())
    context = {
        'form': form,
        'products': products_formset
    }
    return render(request, template_name, context)


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
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('creator',)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ProductViewSet(DefaultMixin, viewsets.ModelViewSet):
    """
    API endpoint edit, create, delete and update list products
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
