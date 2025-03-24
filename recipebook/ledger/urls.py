from django.urls import path
from .views import recipe_list, recipe_detail, custom_login
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('recipes/', recipe_list, name='list'),
    path('recipe/<str:recipe_name>/', recipe_detail, name='detail'),
    path('login/', custom_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]

app_name = "ledger"
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)