from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import generics, viewsets, permissions

from .serializers import UserSerializer, LoginSerializer, TripSerializer
from rest_framework_simplejwt.views import TokenObtainPairView # new
from trips.models import Trip


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LoginView(TokenObtainPairView): # new
    serializer_class = LoginSerializer


class TripView(viewsets.ReadOnlyModelViewSet):
    # The lookup_field variable tells the view to get the trip record by its id value.
    # The lookup_url_kwarg variable tells the view what named parameter to use to extract the id value from the URL
    
    lookup_field = 'id'
    lookup_url_kwarg = 'trip_id'
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TripSerializer

    def get_queryset(self): # new
        user = self.request.user
        if user.group == 'driver':
            return Trip.objects.filter(
                Q(status=Trip.REQUESTED) | Q(driver=user)
            )
        if user.group == 'rider':
            return Trip.objects.filter(rider=user)
        return Trip.objects.none()
