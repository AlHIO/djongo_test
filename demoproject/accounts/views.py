from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.urls import reverse_lazy

class LoginView(DjangoLoginView):
    template_name = 'registration/login.html'   # 可先用 Django 預設模板
    success_url = reverse_lazy('some_dashboard')  # 登入後導向

class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('login')            # 登出後導向
