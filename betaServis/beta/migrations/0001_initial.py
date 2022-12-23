# Generated by Django 4.1.4 on 2022-12-22 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Betaservis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.TextField()),
                ('services', models.TextField()),
                ('works', models.TextField()),
                ('forms', models.TextField()),
                ('contacts', models.TextField()),
                ('site', models.TextField()),
                ('outsorcing', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BetaservisText',
            fields=[
                ('main_text', models.TextField()),
                ('services_text', models.TextField()),
                ('works_text', models.TextField()),
                ('forms_text', models.TextField()),
                ('contacts_text', models.TextField()),
                ('site_text', models.TextField()),
                ('outsorcing_text', models.TextField()),
                ('Betaservis', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='beta.betaservis')),
            ],
        ),
    ]