# Generated by Django 2.0.3 on 2018-05-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('book_name', models.CharField(max_length=100)),
                ('book_cover', models.FileField(upload_to='book/')),
            ],
        ),
    ]