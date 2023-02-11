from urllib import response
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Booking, MenuItem
from .serializer import BookingSerializer, UserSerializer, MenuItemSerializer
from django.contrib.auth.models import User
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated]


def index(request):
    return render(request, 'index.html', {})


# class MenuItemView(generics.ListCreateAPIView):

#     def post(request):
#         return

#     def get(request):
#         return


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):

    def post(request):
        return

    def get(request):
        return

    def delete(request):
        return


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return response({"message": "This view is protected"})
