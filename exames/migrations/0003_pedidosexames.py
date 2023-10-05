# Generated by Django 4.2.6 on 2023-10-05 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exames', '0002_solicitacaoexame'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidosExames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agendado', models.BooleanField(default=True)),
                ('data', models.DateField()),
                ('exames', models.ManyToManyField(to='exames.solicitacaoexame')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
