# Generated by Django 3.2.19 on 2023-07-11 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0046_version_4_6_0'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpreferences',
            name='tool_adjustment_notifications',
            field=models.ManyToManyField(blank=True, help_text='Tools to receive adjustment notifications for. If empty all notifications will be received.', related_name='_NEMO_userpreferences_tool_adjustment_notifications_+', to='NEMO.Tool'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_facility_manager',
            field=models.BooleanField(default=False, help_text='Designates this user as facility manager. Facility managers receive updates on all reported problems in the facility and also review access and adjustment requests.', verbose_name='facility manager'),
        ),
    ]
