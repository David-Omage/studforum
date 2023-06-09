# Generated by Django 4.1.1 on 2022-10-09 19:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_topic_rooms_host_message_rooms_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rooms',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='rooms',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participant', to=settings.AUTH_USER_MODEL),
        ),
    ]
