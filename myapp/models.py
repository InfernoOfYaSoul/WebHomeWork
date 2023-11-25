from django.conf import settings
from django.db import models
from django.utils import timezone


# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title

class Info(models.Model):

    choice_sex = [
        ('M', 'Парень'),
        ('F', 'Девушка'),
    ]

    photo = models.ImageField(upload_to="static/img/pics", default = "null")
    # sex1 = models.CharField(max_length = 200)
    # sex2 = models.CharField(max_length = 200)
    sex = models.CharField(default="", max_length=1, choices=choice_sex, verbose_name="Пол")
    birth_date = models.DateField(default="")
    name = models.CharField(max_length = 200)
    tg = models.CharField(max_length = 200)
    phone_num = models.CharField(max_length = 12, default="")
    text = models.TextField(default = "")

    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # name = models.TextField()
    # birth_date = models.DateTimeField(default=timezone.now)
    # tg = models.CharField(max_length=200)
    # phone_num = models.CharField(max_length = 11)
    # text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name