from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.fields.files import ImageField
from user.models import GeneralUser


class Challenge(models.Model):
    CHALLANGE_CHOICES =(
        ('PH', '집 앞 식물 심기'),
        ('RC', '재활용')

    )
    writer = models.ForeignKey(GeneralUser, on_delete=CASCADE)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=3, choices=CHALLANGE_CHOICES, null=True, blank=True)
    content = RichTextUploadingField(
        blank=True, null=True, config_name='answer_ckeditor')
    thumbnail = ImageField(default='../static/images/baseimg.jpg',upload_to='event/%y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Issue(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(
        blank=True, null=True, config_name='answer_ckeditor')
    thumbnail = ImageField(default='../static/images/baseimg.jpg',upload_to='event/%y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title