# Generated by Django 4.2.7 on 2023-11-29 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_livromodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livromodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]