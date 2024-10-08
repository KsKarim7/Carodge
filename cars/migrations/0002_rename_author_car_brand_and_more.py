# Generated by Django 5.1 on 2024-09-06 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='author',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='content',
            new_name='description',
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='car',
            name='quantity',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cars/media/uploads/'),
        ),
    ]
