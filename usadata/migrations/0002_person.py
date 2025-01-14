# Generated by Django 5.0.6 on 2024-06-13 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usadata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id_number', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state_code', models.CharField(max_length=2)),
                ('shirt_or_hat', models.CharField(verbose_name=50)),
                ('quiz_points', models.IntegerField()),
                ('team', models.CharField(max_length=50)),
                ('signup', models.DateField()),
                ('age', models.IntegerField()),
                ('company', models.CharField(max_length=100)),
            ],
        ),
    ]
