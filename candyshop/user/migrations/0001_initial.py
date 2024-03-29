# Generated by Django 3.2.9 on 2021-12-31 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('details', models.TextField()),
                ('stock', models.IntegerField()),
                ('image1', models.FileField(upload_to='img')),
                ('image2', models.FileField(upload_to='img')),
            ],
        ),
    ]
