# Generated by Django 4.2.3 on 2023-07-14 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='user_id',
            new_name='user',
        ),
    ]