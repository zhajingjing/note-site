# Generated by Django 5.0.3 on 2024-03-31 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_notes_create_user_alter_article_subtitle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='reference_text',
            field=models.CharField(blank=True, default='', max_length=10000, null=True),
        ),
    ]
