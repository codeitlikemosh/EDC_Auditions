# Generated by Django 3.2.16 on 2023-12-27 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20231227_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.inductees'),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]