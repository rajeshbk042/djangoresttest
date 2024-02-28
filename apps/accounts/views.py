from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from rest_framework import viewsets

from apps.accounts.serializers import CustomerSerializer
from apps.accounts.models import Customer


class LogoutView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            print(refresh_token)

            # token = RefreshToken(refresh_token)
            # token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CustomerViewSet(viewsets.ModelViewSet):
    """
    Customer viewset
    """
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    model_class = Customer

    def get_queryset(self):
        return self.model_class.objects.all()

    def create(self, request):
        print(">>>>>", request.data)
        return super().create(request)
