# Generated by Django 3.2.4 on 2021-06-04 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demande',
            old_name='Contacte',
            new_name='Contactes',
        ),
        migrations.RenameField(
            model_name='pub',
            old_name='Predicateur',
            new_name='Predicateurs',
        ),
        migrations.AddField(
            model_name='pub',
            name='reference',
            field=models.IntegerField(null=True),
        ),
    ]