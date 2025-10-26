from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUserForUpdate

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsSuperUserForUpdate]
    
    def get_queryset(self):
        user = self.request.user
        
        if user.is_superuser:
            return Order.objects.all()
        
        return Order.objects.filter(user=user)