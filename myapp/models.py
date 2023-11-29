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

    choice_stud = [
        ('S', 'Студент / выпускник'),
        ('T', 'Сотрудник'),
    ]

    choice_step = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('n', 'Уже окончил вышку')
    ]

    choice_ed_step = [
        ('bachelor', 'Бакалавриат'),
        ('magistracy', 'Магистратура'),
        ('postgraduate', 'Аспирантура'),
    ]
    def contact_default():
        src = "../static/img/Photomini.svg"
        return src
    

    photo = models.ImageField(upload_to="img/", default = contact_default(), verbose_name="Фото профиля")
    sex = models.CharField(default="", max_length=1, choices=choice_sex, verbose_name="Пол")
    birth_date = models.DateField(default="2004-12-12", verbose_name="Дата рождения")
    name = models.CharField(max_length = 200, verbose_name="Имя")
    tg = models.CharField(max_length = 200, verbose_name="Телеграм")
    phone_num = models.CharField(max_length = 12, default="", verbose_name="Номер телефона")
    text = models.TextField(default = "", verbose_name="О себе")

    student =  models.CharField(default="", max_length=1, choices=choice_stud, verbose_name='Студент или сотрудник')
    step = models.CharField(default="", max_length=1, choices=choice_step, verbose_name='Курс')
    ed_step = models.CharField(default="", max_length=12, choices=choice_ed_step, verbose_name='Ступень образования')

    


    def publish(self):
        self.save()

    def __str__(self):
        return self.name