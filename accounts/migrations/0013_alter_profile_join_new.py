# Generated by Django 3.2 on 2023-01-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_profile_join_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='join_new',
            field=models.DateField(blank=True, null=True, verbose_name='وقت الإنضمام: '),
        ),
    ]