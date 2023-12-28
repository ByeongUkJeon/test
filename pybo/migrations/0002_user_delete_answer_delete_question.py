# Generated by Django 4.0.3 on 2023-12-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('passwd', models.TextField()),
                ('nickname', models.TextField()),
                ('email', models.TextField()),
                ('mobile', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]