# Generated by Django 4.2.6 on 2023-10-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theApp', '0002_rename_upload_requestupload_requesttitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requesttitle', models.CharField(max_length=10000000000000000)),
            ],
        ),
        migrations.CreateModel(
            name='miscrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requesttitle', models.CharField(max_length=10000000000000000)),
            ],
        ),
        migrations.CreateModel(
            name='moviesrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requesttitle', models.CharField(max_length=10000000000000000)),
            ],
        ),
        migrations.RenameModel(
            old_name='requestUpload',
            new_name='apprequest',
        ),
    ]
