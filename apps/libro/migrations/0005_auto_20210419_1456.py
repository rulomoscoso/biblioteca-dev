# Generated by Django 2.2 on 2021-04-19 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0004_autor_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='autor',
            new_name='autor_id',
        ),
    ]