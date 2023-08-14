# Generated by Django 4.2.3 on 2023-08-13 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oneday', '0011_onedaycreate_hashtag'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnedayApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.PositiveIntegerField()),
                ('people', models.PositiveIntegerField()),
                ('memo', models.TextField()),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
