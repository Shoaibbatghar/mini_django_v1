# Generated by Django 4.1.5 on 2023-01-07 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2023, 1, 7, 14, 49, 34, 733795, tzinfo=datetime.timezone.utc))),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
