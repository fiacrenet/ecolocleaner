# Generated by Django 5.1 on 2024-08-31 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('before_image', models.ImageField(upload_to='realizations/before/')),
                ('after_image', models.ImageField(upload_to='realizations/after/')),
            ],
        ),
    ]
