# Generated by Django 3.0.3 on 2020-02-24 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0004_favorite_add_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumbnail',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='ocr/image/Thumbnail'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocr.Image'),
        ),
    ]
