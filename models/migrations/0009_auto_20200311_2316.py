# Generated by Django 3.0.4 on 2020-03-11 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0008_auto_20200311_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='bedtype',
            field=models.IntegerField(choices=[(1, 'red'), (2, 'yellow'), (3, 'green'), (4, 'gray')], default=4),
        ),
        migrations.AlterField(
            model_name='bed',
            name='statustype',
            field=models.IntegerField(choices=[('1', 'red'), ('2', 'yellow'), ('3', 'green')], default='3'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='notificationtype',
            field=models.IntegerField(choices=[(1, 'red'), (2, 'yellow'), (3, 'green'), (4, 'blue')], default=4),
        ),
    ]
