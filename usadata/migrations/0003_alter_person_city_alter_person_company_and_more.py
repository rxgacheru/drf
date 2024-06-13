# Generated by Django 5.0.6 on 2024-06-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usadata', '0002_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='company',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='quiz_points',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='shirt_or_hat',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='team',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
