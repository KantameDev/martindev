# Generated by Django 4.1.7 on 2023-05-17 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercice',
            name='correction',
            field=models.FileField(default=1, upload_to='fichier/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exercice',
            name='fichier',
            field=models.FileField(upload_to='fichier/'),
        ),
    ]
