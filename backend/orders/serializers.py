from rest_framework import serializers
from .models import Order
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'
    
    # TODO it works but maybe there is more clean way to separate creation from updating
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.instance is None:
            self.fields['status'].read_only = True
        
    def create(self, validated_data):
        request = self.context.get('request')
        user = getattr(request, 'user', None)
        
        products = validated_data.pop('products', [])
        
        total_price = sum(product.price for product in products)
        
        order = Order.objects.create(
            user=user, 
            total_price=total_price,
            **validated_data
        )
        order.products.set(products)
        order.save()
        
        return order