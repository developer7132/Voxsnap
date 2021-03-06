# Generated by Django 2.2.5 on 2019-09-22 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_lead_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('ip_addr', models.GenericIPAddressField(blank=True, null=True)),
                ('status', models.CharField(choices=[('N', 'Unprocessed'), ('S', 'Subscribed'), ('U', 'Unsubscribed')], default='U', max_length=1)),
            ],
        ),
    ]
