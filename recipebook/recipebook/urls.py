# project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('ledger.urls', namespace="ledger")),
    #first quotation is the subsequent page
    path('admin/', admin.site.urls),
]