from django.urls import path,include
from accounts.views import *
from schema.views import *
from data.views import *

urlpatterns = [
    path("api/users/",UsersListView.as_view()),
    path("api/users/<str:id>/",UserDetailsView.as_view()),
    path("api/data/<str:entity>/",DataView.as_view()),
    path("api/entities/",EntitiesListView.as_view()),
]
