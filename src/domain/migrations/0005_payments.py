# Generated by Django 4.2.1 on 2023-06-29 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0004_payments_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('bill_id', models.CharField(db_index=True, max_length=50)),
                ('date_of_issue', models.DateTimeField(auto_now=True)),
                ('value_date', models.DateTimeField(auto_now=True)),
                ('delivery_date', models.DateTimeField(auto_now=True)),
                ('payment_method', models.CharField(max_length=50)),
                ('content', models.JSONField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='domain.customer')),
                ('payments_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='domain.payments_details')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='domain.person')),
            ],
        ),
    ]
