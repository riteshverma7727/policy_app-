from django.urls import path
from .views import PolicyListCreateAPIView, PolicyRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('policies/', PolicyListCreateAPIView.as_view(), name='policy-list-create'),
    path('policies/<int:pk>/', PolicyRetrieveUpdateDestroyAPIView.as_view(), name='policy-retrieve-update-destroy'),
]
