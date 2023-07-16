from django.urls import path
from django.views.decorators.cache import cache_page

from apps.views import UserListCreateAPIView

urlpatterns = [
    path('users', cache_page(16 * 4)(UserListCreateAPIView.as_view()))
]
