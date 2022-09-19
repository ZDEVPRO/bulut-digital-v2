# Generated by Django 4.1.1 on 2022-09-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logo',
            options={'verbose_name': 'Site Logo', 'verbose_name_plural': 'Site Logo'},
        ),
        migrations.AddField(
            model_name='logo',
            name='favicon',
            field=models.ImageField(default='icon', upload_to='favicon/'),
            preserve_default=False,
        ),
    ]
