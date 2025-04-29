from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        u = request.data.get('username')
        p = request.data.get('password')
        user = authenticate(request, username=u, password=p)
        if not user:
            return Response({'error': '帳號或密碼錯誤'}, status=400)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=204)
