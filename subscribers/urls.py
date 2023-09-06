from django.urls import path
from .views import *

urlpatterns = [
    path('add/', SubscribersCreateView.as_view(), name='add_subscriber'),
    path('list/', SubscribersListView.as_view(), name='list_subscriber'),
    path('update/<int:pk>', SubscribersUpdateView.as_view(),
         name='update_subscriber'),
    path('delete/<int:pk>', SubscriberDeleteView.as_view(), name='delete_subscriber')
]
