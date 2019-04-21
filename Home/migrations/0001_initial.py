# Generated by Django 2.1 on 2019-04-15 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sanpham',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Code', models.CharField(blank=True, max_length=12, null=True)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Describe', models.TextField(blank=True, null=True)),
                ('Useway', models.TextField(blank=True, null=True)),
                ('DescribeImg', models.FileField(blank=True, null=True, upload_to='./UsewayImg')),
                ('Quantity', models.IntegerField(default=0)),
                ('Price', models.IntegerField(default=0)),
                ('SalePrice', models.IntegerField(default=0)),
                ('BuyQuantity', models.IntegerField(default=0)),
            ],
        ),
    ]
