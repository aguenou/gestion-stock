# Generated by Django 4.1.6 on 2023-02-15 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appGestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magasin',
            name='dirigeant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dirigeant', to='appGestion.dirigeant'),
        ),
        migrations.AlterField(
            model_name='meuble',
            name='etat',
            field=models.CharField(choices=[('NF', 'NEUF'), ('OC', 'OCCASION'), ('ME', 'MAUVAIS ETAT'), ('INU', 'INUTILSABLE')], default='NF', max_length=3),
        ),
        migrations.AlterField(
            model_name='meuble',
            name='lieu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lieu', to='appGestion.magasin'),
        ),
    ]