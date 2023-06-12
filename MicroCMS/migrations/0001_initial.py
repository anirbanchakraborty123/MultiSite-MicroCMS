# Generated by Django 4.2 on 2023-06-12 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(blank=True, max_length=255, null=True)),
                ('device_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('currency', models.CharField(blank=True, max_length=255, null=True)),
                ('offer_price', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email_id', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('referral_code', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_status', models.CharField(choices=[('Pending', 'Pending'), ('In-progress', 'In-progress'), ('Converted', 'Converted'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email_id', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MicroCMS.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MicroCMS.country')),
                ('managedbyuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.TextField(blank=True, null=True)),
                ('allowed_devices', models.ManyToManyField(to='MicroCMS.devices')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
        ),
        migrations.CreateModel(
            name='Walk_In',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(blank=True, max_length=255, null=True)),
                ('offer_price', models.IntegerField(blank=True, null=True)),
                ('walk_in_datetime', models.DateTimeField()),
                ('token_number', models.IntegerField(blank=True, default=0, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MicroCMS.devices')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MicroCMS.lead')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MicroCMS.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='PageSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.TextField(blank=True, null=True)),
                ('section_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('section_HTMLContent', models.TextField(blank=True, null=True)),
                ('section_order', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=1)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MicroCMS.webpage')),
            ],
        ),
        migrations.AddField(
            model_name='devices',
            name='sourced',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MicroCMS.vendor'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MicroCMS.country'),
        ),
    ]
