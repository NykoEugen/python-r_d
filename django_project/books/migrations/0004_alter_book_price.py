# Generated by Django 4.2.3 on 2023-07-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_author_alter_book_price_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(),
        ),
    ]
