# Generated by Django 3.0.3 on 2020-03-03 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='alerts',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='generalstatus',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='patientimg',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='risks',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='statustype',
        ),
        migrations.AddField(
            model_name='bed',
            name='alerts',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='bed',
            name='generalstatus',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='bed',
            name='patientimg',
            field=models.ImageField(blank=True, null=True, upload_to='patientimg'),
        ),
        migrations.AddField(
            model_name='bed',
            name='risks',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='bed',
            name='statustype',
            field=models.CharField(choices=[('1', 'red'), ('2', 'yellow'), ('3', 'green'), ('4', 'gray')], default='4', max_length=1),
        ),
        migrations.AlterField(
            model_name='bed',
            name='nurse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='models.Nurse'),
        ),
    ]
