# Generated by Django 4.2.3 on 2023-07-16 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('title', 'author')},
        ),
    ]