# Generated by Django 4.2.5 on 2023-09-27 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="societe",
            name="adresse",
        ),
        migrations.RemoveField(
            model_name="societe",
            name="continent",
        ),
        migrations.RemoveField(
            model_name="societe",
            name="decideur",
        ),
        migrations.RemoveField(
            model_name="societe",
            name="localisation",
        ),
        migrations.RemoveField(
            model_name="societe",
            name="pays",
        ),
        migrations.RemoveField(
            model_name="societe",
            name="ville",
        ),
        migrations.AddField(
            model_name="societe",
            name="adresses",
            field=models.ManyToManyField(
                related_name="societes_adresse", to="myapp.adresse"
            ),
        ),
        migrations.AddField(
            model_name="societe",
            name="decideurs",
            field=models.ManyToManyField(
                related_name="societes_decideurs", to="myapp.decideur"
            ),
        ),
        migrations.AlterField(
            model_name="societe",
            name="adresse_postal",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="societe_adresse_postal",
                to="myapp.adresse",
            ),
        ),
    ]