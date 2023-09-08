from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from .management.kafka_config import producer

from .models import Campaigns
from subscribers.models import Subscribers
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


def send_campaign_email(request, pk):

    try:

        campaign = get_object_or_404(Campaigns, pk=pk)

        active_subscribers = Subscribers.objects.filter(is_active=True)

        subject = campaign.subject
        article_url = campaign.article_url
        preview_text = campaign.preview_text
        html_content = campaign.html_content
        plain_text_content = campaign.plain_text_content
        published_date = campaign.published_date

        email = render_to_string('campaign_email.html', {
            'subject': subject,
            'article_url': article_url,
            'preview_text': preview_text,
            'html_content': html_content,
            'plain_text_content': plain_text_content,
            'published_date': published_date,
        })

        for subscriber in active_subscribers:

            producer.produce('bkpzcrni-mail_system',
                             key=subscriber.email, value=email)

        producer.flush()

        return redirect('detail_campaigns', pk=pk)

    except Exception as e:

        return redirect('detail_campaigns', pk=pk)
