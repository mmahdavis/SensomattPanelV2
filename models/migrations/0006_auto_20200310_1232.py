# Generated by Django 3.0.4 on 2020-03-10 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_auto_20200310_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurse',
            name='patient',
        ),
        migrations.AddField(
            model_name='patient',
            name='nurse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='models.Nurse'),
        ),
    ]