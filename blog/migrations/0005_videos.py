# Generated by Django 3.2.4 on 2021-06-10 11:16

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210606_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
    ]