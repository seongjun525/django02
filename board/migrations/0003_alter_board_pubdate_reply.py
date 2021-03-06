# Generated by Django 4.0.2 on 2022-02-24 19:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0002_alter_board_pubdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 24, 19, 30, 23, 386344)),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('pubdate', models.DateTimeField()),
                ('b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.board')),
                ('replyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
