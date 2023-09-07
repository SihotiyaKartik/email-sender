from django.db import models

# Create your models here.


class Campaigns(models.Model):
    subject = models.CharField(max_length=400)
    preview_text = models.TextField()
    article_url = models.URLField()
    html_content = models.TextField()
    plain_text_content = models.TextField()
    published_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
