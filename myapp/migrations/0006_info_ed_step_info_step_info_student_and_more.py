# Generated by Django 4.2.7 on 2023-11-28 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_remove_info_sex1_remove_info_sex2_info_sex_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="info",
            name="ed_step",
            field=models.CharField(
                choices=[
                    ("bachelor", "Бакалавриат"),
                    ("magistracy", "Магистратура"),
                    ("postgraduate", "Аспирантура"),
                ],
                default="",
                max_length=12,
                verbose_name="Ступень образования",
            ),
        ),
        migrations.AddField(
            model_name="info",
            name="step",
            field=models.CharField(
                choices=[
                    ("1", "1"),
                    ("2", "2"),
                    ("3", "3"),
                    ("4", "4"),
                    ("5", "5"),
                    ("6", "6"),
                    ("n", "Уже окончил вышку"),
                ],
                default="",
                max_length=1,
                verbose_name="Курс",
            ),
        ),
        migrations.AddField(
            model_name="info",
            name="student",
            field=models.CharField(
                choices=[("S", "Студент / выпускник"), ("T", "Сотрудник")],
                default="",
                max_length=1,
                verbose_name="Студент или сотрудник",
            ),
        ),
        migrations.AlterField(
            model_name="info",
            name="birth_date",
            field=models.DateField(default="", verbose_name="Дата рождения"),
        ),
        migrations.AlterField(
            model_name="info",
            name="name",
            field=models.CharField(max_length=200, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="info",
            name="phone_num",
            field=models.CharField(
                default="", max_length=12, verbose_name="Номер телефона"
            ),
        ),
        migrations.AlterField(
            model_name="info",
            name="photo",
            field=models.ImageField(
                default=None, upload_to="img/", verbose_name="Фото профиля"
            ),
        ),
        migrations.AlterField(
            model_name="info",
            name="text",
            field=models.TextField(default="", verbose_name="О себе"),
        ),
        migrations.AlterField(
            model_name="info",
            name="tg",
            field=models.CharField(max_length=200, verbose_name="Телеграм"),
        ),
    ]
