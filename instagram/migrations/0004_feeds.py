# Generated by Django 3.2.3 on 2021-06-21 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_remove_instausers_dateofbirth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgFeed', models.ImageField(upload_to=None)),
                ('caption', models.TextField(max_length=500)),
            ],
        ),
    ]