# demoproject/accounts/api_urls.py
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import LogoutAPIView  # 你已經實作好的 LogoutAPIView

urlpatterns = [
    # POST /api/accounts/login/ → 回傳 token
    path('login/', obtain_auth_token, name='api-login'),
    # POST /api/accounts/logout/ → 刪 token
    path('logout/', LogoutAPIView.as_view(), name='api-logout'),
]
