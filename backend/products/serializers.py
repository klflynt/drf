from rest_framework import serializers

from .models import Product

# class ProductsForm(serializers.ModelSerializer)
class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
            # 'get_discount',
        ]

    def get_my_discount(self, obj):
        # print(obj.id)
        # obj.user -> user.username
        # return obj.get_discount()
        # try:
        #     return obj.get_discount()
        # except:
        #     return None
        return obj.get_discount()