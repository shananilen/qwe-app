# Generated by Django 4.1.7 on 2023-04-02 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("deliveries", "0003_vehicleroutestatus_securityteam_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vehicleroute",
            name="securityteam_id",
        ),
    ]