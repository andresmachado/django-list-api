from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import List, Product

User = get_user_model()


class ProductListingField(serializers.RelatedField):
    def to_representation(self, field):
        price = '%.02f' % field.price
        return '%s: %s (R$ %s)' % (field.name, field.quantity, price)


class ListSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
#    products = serializers.SlugRelatedField(many=True,
#                                            slug_field='name',
#                                            read_only=True)

    products = ProductListingField(many=True,
                                   read_only=True)

    class Meta:
        model = List
        fields = ('url', 'creator', 'name', 'products',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    lists = serializers.HyperlinkedIdentityField(many=True,
                                                 view_name='list-detail',
                                                 read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'lists')


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('url', 'list', 'name', 'quantity', 'price',)
