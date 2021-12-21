# Generated by Django 3.1.12 on 2021-12-03 10:20

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0038_auto_20210606_2237'),
        ('upload', '0005_auto_20190131_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True, default='')),
                ('brand', models.CharField(blank=True, default='', max_length=60)),
                ('warranty', models.BooleanField(default=False)),
                ('packaging', models.BooleanField(default=False)),
                ('condition', multiselectfield.db.fields.MultiSelectField(choices=[('1', '01/10'), ('2', '02/10'), ('3', '03/10'), ('4', '04/10'), ('5', '05/10'), ('6', '06/10'), ('7', '07/10'), ('8', '08/10'), ('9', '09/10'), ('10', '10/10')], max_length=20)),
                ('action', multiselectfield.db.fields.MultiSelectField(choices=[('sell', 'Sell'), ('giveaway', 'Give Away'), ('rell', 'Rent')], max_length=18)),
                ('status', models.BooleanField(default=True)),
                ('price', models.IntegerField(default=100)),
                ('negotiable', models.BooleanField(default=True)),
                ('contact_details', models.CharField(max_length=300)),
                ('images', models.ManyToManyField(blank=True, related_name='_product_images_+', to='upload.UploadedImage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
        ),
    ]