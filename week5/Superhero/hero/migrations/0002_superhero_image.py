# Generated by Django 3.2.7 on 2021-09-22 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='image',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
