# Generated by Django 2.2 on 2019-04-24 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_path', models.ImageField(blank=True, max_length=500, null=True, upload_to='ocr/image/')),
                ('uplaod_date', models.DateTimeField(auto_now=True)),
                ('tag', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_date', models.DateTimeField(auto_now=True)),
                ('result', models.TextField()),
                ('text_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocr.Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]