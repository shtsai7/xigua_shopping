# Generated by Django 2.0 on 2017-12-28 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20171227_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('iid', models.AutoField(primary_key=True, serialize=False)),
                ('idate', models.DateTimeField(verbose_name='Date Received')),
                ('icost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Value')),
                ('ishipping', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Shipping Cost')),
                ('itype', models.CharField(max_length=20, null=True, verbose_name='Shipping Method')),
                ('inote', models.CharField(max_length=100, null=True, verbose_name='Note')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='cnote',
            field=models.CharField(max_length=100, null=True, verbose_name='Note'),
        ),
        migrations.AddField(
            model_name='order',
            name='onote',
            field=models.CharField(max_length=100, null=True, verbose_name='Note'),
        ),
        migrations.AddField(
            model_name='product',
            name='pnote',
            field=models.CharField(max_length=100, null=True, verbose_name='Note'),
        ),
    ]
