# Generated by Django 3.2.3 on 2021-05-25 21:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uuidmodel',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterField(
            model_name='uuidmodel',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('e364ef0c-794c-46f1-820e-a92feaaedc98'), editable=False),
        ),
    ]