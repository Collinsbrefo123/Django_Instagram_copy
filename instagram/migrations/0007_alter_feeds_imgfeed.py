# Generated by Django 3.2.3 on 2021-06-28 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_alter_feeds_imgfeed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='imgFeed',
            field=models.ImageField(upload_to='upload'),
        ),
    ]
