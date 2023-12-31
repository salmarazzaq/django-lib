# Generated by Django 2.2 on 2023-12-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.AddField(
            model_name='book',
            name='available_copies',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='issue_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='total_copies',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='total_books_due',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
