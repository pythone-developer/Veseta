# Generated by Django 3.2 on 2023-01-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_profile_join_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='join_new',
            field=models.DateTimeField(auto_now_add=True, verbose_name='وقت الإنضمام: '),
        ),
    ]