# Generated by Django 2.2.5 on 2019-09-21 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_veiculo_proprietario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veiculo',
            old_name='name',
            new_name='marca',
        ),
    ]
