from django.db import models


class GuestBook(models.Model):
    name = models.CharField(max_length=100)


class GuestBookEntry(models.Model):
    guestbook = models.ForeignKey(GuestBook)
    full_name = models.CharField(max_length=100)
    message = models.TextField()
    website = models.URLField(blank=True)
