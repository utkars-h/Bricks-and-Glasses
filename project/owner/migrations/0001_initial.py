# Generated by Django 3.2 on 2021-04-19 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('ownerID', models.IntegerField()),
                ('oname', models.CharField(blank=True, max_length=40)),
                ('contact', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('pwd', models.CharField(blank=True, max_length=40)),
            ],
        ),
    ]