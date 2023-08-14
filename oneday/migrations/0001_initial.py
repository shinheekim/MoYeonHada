# Generated by Django 4.2.3 on 2023-08-10 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnedayApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('people', models.CharField(max_length=50)),
                ('memo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OnedayRecruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('period', models.CharField(max_length=50)),
                ('region', models.CharField(default='', max_length=50)),
                ('hashtag', models.CharField(default='', max_length=50)),
                ('title', models.CharField(default='', max_length=50)),
                ('content', models.CharField(default='', max_length=50)),
                ('picture', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
