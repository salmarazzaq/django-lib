# Generated by Django 2.2 on 2023-12-06 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20231206_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='issue_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
