# project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('ledger.urls', namespace="ledger")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
]