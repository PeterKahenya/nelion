from django.contrib import admin
from django.urls import path
from accounts.views import UsersListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users',UsersListView.as_view())
]
