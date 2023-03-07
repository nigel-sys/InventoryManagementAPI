from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import Product, Stock, Order
from .serializers import ProductSerializer, StockSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def add_stock(request):
    product = Product.objects.get(id=request.data['product_id'])
    quantity = request.data['quantity']

    stock = Stock()
    stock.product = product
    stock.quantity = quantity
    stock.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def add_order(request):
    product = Product.objects.get(id=request.data['product_id'])
    quantity = request.data['quantity']

    order = Order()
    order.product = product
    order.quantity = quantity
    order.save()

    stock = Stock.objects.get(product=product)
    stock.quantity -= int(quantity)
    stock.save()

    return Response(status=status.HTTP_201_CREATED)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
