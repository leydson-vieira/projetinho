# Generated by Django 2.0 on 2018-08-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesquisa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatperguntavaga',
            name='respondida',
            field=models.BooleanField(default=False),
        ),
    ]
