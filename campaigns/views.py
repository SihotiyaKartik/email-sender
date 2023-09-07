from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Campaigns

# Create your views here.


class CampaignsListView(ListView):
    model = Campaigns
    template_name = 'campaigns/list.html'
    context_object_name = 'campaigns_list'

    def get_queryset(self):
        return Campaigns.objects.all()


class CampaignsUpdateView(UpdateView):
    model = Campaigns
    fields = ['subject', 'preview_text', 'article_url', 'html_content',
              'plain_text_content', 'published_date', 'is_active']
    template_name = 'campaigns/update.html'

    def get_success_url(self) -> str:
        return reverse_lazy('detail_campaigns', kwargs={'pk': self.object.pk})


class CampaignsCreateView(CreateView):
    model = Campaigns
    fields = ['subject', 'preview_text', 'article_url',
              'html_content', 'plain_text_content', 'published_date']
    template_name = 'campaigns/add.html'
    success_url = '/campaigns/list'


class CampaignsDetailView(DetailView):
    model = Campaigns
    template_name = 'campaigns/detail.html'
    context_object_name = 'campaign'


class CampaignsDeleteView(DeleteView):
    model = Campaigns
    template_name = 'campaigns/delete.html'
    success_url = '/campaigns/list/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = self.get_object()
        return context
