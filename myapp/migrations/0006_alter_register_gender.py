# Generated by Django 4.1.6 on 2023-02-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_alter_register_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="register",
            name="gender",
            field=models.CharField(
                choices=[("Male", "Male"), ("Female", "Female"), ("Others", "Others")],
                max_length=10,
            ),
        ),
    ]