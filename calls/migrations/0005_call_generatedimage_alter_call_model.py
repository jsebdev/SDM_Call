# Generated by Django 4.1.7 on 2023-02-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0004_alter_call_seed'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='generatedImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='call',
            name='model',
            field=models.CharField(default='CompVis/stable-diffusion-v1-4', max_length=200),
        ),
    ]
