# Generated by Django 4.0.5 on 2023-01-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvupload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]