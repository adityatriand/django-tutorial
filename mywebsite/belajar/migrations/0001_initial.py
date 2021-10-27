# Generated by Django 3.2.8 on 2021-10-27 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PengalamanBelajar',
            fields=[
                ('id_belajar', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=100)),
                ('isi', models.TextField()),
            ],
            options={
                'db_table': 'pengalaman_belajar',
                'managed': False,
            },
        ),
    ]
