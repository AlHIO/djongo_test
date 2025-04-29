from django.contrib import admin
from django.urls import path, include
from accounts.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),

    # 註冊頁面
    path('accounts/signup/', SignUpView.as_view(), name='signup'),

    # HTML 登入/登出
    path('accounts/', include('django.contrib.auth.urls')),

    # JSON API 登入/登出
    path('api/accounts/', include('accounts.api_urls')),
]
