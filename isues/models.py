from django.db import models
from django.utils import timezone

class Issue(models.Model):
    issue_text = models.TextField(max_length=1000)
    pub_date = models.DateField("data published")
    likes_num = models.IntegerField(default=0)

    def __str__(self):
        return self.issue_text

    def Was_publishe_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Comment(models.Model):
    Comment_text = models.TextField(max_length=1000)
    pub_date = models.DateField("data published")
    likes_num = models.IntegerField(default=0)

    def __str__(self):
        return self.Comment_text
# Create your models here.
