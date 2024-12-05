# Generated by Django 4.2.2 on 2023-06-30 08:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contents', '0001_initial'),
        ('employers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=512, null=True, verbose_name='Description')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Salary')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employers.company')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.location')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]