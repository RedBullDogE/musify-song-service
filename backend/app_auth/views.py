from django.conf import settings
from django.contrib.auth import login, logout
from rest_framework import authentication, generics, permissions, response, views

from .serializers import LoginSerializer, UserSerializer


class SigninView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (authentication.SessionAuthentication,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return response.Response(UserSerializer(user).data)


class SignoutView(views.APIView):
    def post(self, request):
        logout(request)
        return response.Response()


class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.backend = settings.AUTHENTICATION_BACKENDS[0]
        login(self.request, user)


class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = "pk"

    def get_object(self, *args, **kwargs):
        return self.request.user
