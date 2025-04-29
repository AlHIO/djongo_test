# demoproject/accounts/views.py

from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

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


# ─────────── 新增以下這段 ───────────

class SignUpView(generic.CreateView):
    """
    HTML 註冊頁面 (使用 Django 內建的 UserCreationForm)
    註冊成功後 redirect 回 'login' (accounts/login/)
    """
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')



class ProfileView(LoginRequiredMixin, TemplateView):
    """
    使用者必須已登入才能看
    template_name 會對應到 templates/registration/profile.html
    """
    template_name = 'registration/profile.html'
