# Generated by Django 2.2.7 on 2019-11-16 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
