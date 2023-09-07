from django.urls import path
from .views import *

urlpatterns = [
    path('add/', CampaignsCreateView.as_view(), name='add_campaigns'),
    path('list/', CampaignsListView.as_view(), name='list_campaigns'),
    path('details/<int:pk>', CampaignsDetailView.as_view(), name='detail_campaigns'),
    path('update/<int:pk>', CampaignsUpdateView.as_view(),
         name='update_campaigns'),
    path('delete/<int:pk>', CampaignsDeleteView.as_view(), name='delete_campaigns'),
    path('send_email/<int:pk>', send_campaign_email, name='email_campaigns')
]
