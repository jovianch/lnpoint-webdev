from rest_framework import status, response, views, permissions, generics
from api.serializers.accounts import RegisterSerializer, UserSerializer
from api.utils.permissions import IsAnonymous
from utils.jwt import jwt_response_payload_handler

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (IsAnonymous, )

    def post(self, request, format=None):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            response_payload = jwt_response_payload_handler(user=user, request=request)

            return response.Response(response_payload)

        except Exception as e:
            return response.Response({'detail' : str(e)},
                                     status=status.HTTP_400_BAD_REQUEST)

class MeView(views.APIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, format=None):
        try:
            serializer = self.serializer_class(request.user)
            return response.Response(serializer.data)
        except Exception as e:
            return response.Response({'detail' : str(e)},
                                 status=status.HTTP_400_BAD_REQUEST)
