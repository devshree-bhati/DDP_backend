# Generated by Django 4.2 on 2024-11-19 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ddpui", "0103_connectionjob_connectionmeta_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="orgdataflowv1",
            name="clear_conn_dataflow",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="clear_connection_dataflow",
                to="ddpui.orgdataflowv1",
            ),
        ),
    ]
