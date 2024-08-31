# Generated by Django 4.2.6 on 2023-11-13 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theApp', '0007_alter_appupload_file_alter_bookupload_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appupload',
            name='file',
            field=models.FileField(upload_to='actualFiles/Apps/'),
        ),
        migrations.AlterField(
            model_name='appupload',
            name='image',
            field=models.ImageField(height_field=100, upload_to='coverImages/Apps/', width_field=100),
        ),
        migrations.AlterField(
            model_name='bookupload',
            name='file',
            field=models.FileField(upload_to='actualFiles/Books/'),
        ),
        migrations.AlterField(
            model_name='bookupload',
            name='image',
            field=models.ImageField(height_field=100, upload_to='coverImages/Books/', width_field=100),
        ),
        migrations.AlterField(
            model_name='miscupload',
            name='file',
            field=models.FileField(upload_to='actualFiles/Others/'),
        ),
        migrations.AlterField(
            model_name='miscupload',
            name='image',
            field=models.ImageField(height_field=100, upload_to='coverImages/Others/', width_field=100),
        ),
        migrations.AlterField(
            model_name='moviesupload',
            name='file',
            field=models.FileField(upload_to='actualFiles/Videos/'),
        ),
        migrations.AlterField(
            model_name='moviesupload',
            name='image',
            field=models.ImageField(height_field=100, upload_to='coverImages/Videos/', width_field=100),
        ),
    ]