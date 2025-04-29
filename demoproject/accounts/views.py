from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout

class LoginView(APIView):
    def post(self, request):
        u = request.data.get('username')
        p = request.data.get('password')
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            return Response({'detail': '登入成功'})
        return Response({'detail': '帳密錯誤'}, status=400)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'detail': '已登出'})
