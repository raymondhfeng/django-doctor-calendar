# Generated by Django 3.1.5 on 2021-01-08 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Calendar', '0003_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Calendar.doctor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Calendar.patient'),
        ),
    ]