# Generated by Django 5.1.1 on 2024-09-23 19:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('atividades', models.IntegerField()),
                ('equipe', models.IntegerField()),
                ('comunicacao', models.IntegerField()),
                ('entregas', models.IntegerField()),
                ('gerente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sprints', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('descricao', models.TextField()),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dailys', to='core.sprint')),
            ],
        ),
    ]
