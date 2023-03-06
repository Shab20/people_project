from django.urls import path
from .views import people_list, PersonDetailView


urlpatterns = [
    path('people/', people_list, name='people_list'),
    path('people/<int:pk>/', PersonDetailView.as_view(), name='person_detail'),
]
