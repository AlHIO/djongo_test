from django.contrib import admin
from django.urls import path, include
from accounts.views import SignUpView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),

    # 註冊頁面
    path('accounts/signup/', SignUpView.as_view(), name='signup'),

    # HTML 登入/登出
    path('accounts/', include('django.contrib.auth.urls')),

    # 使用者個人頁面（登入成功後 redirect 會到這）
    path('accounts/profile/', ProfileView.as_view(), name='profile'),

    # JSON API 登入/登出
    path('api/accounts/', include('accounts.api_urls')),
]
