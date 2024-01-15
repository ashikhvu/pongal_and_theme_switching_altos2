# Generated by Django 3.2.16 on 2023-01-31 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_vacancy_application_vacancys'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ps_head', models.CharField(max_length=255)),
                ('ps_des', models.TextField(default='')),
                ('ps_des2', models.TextField(default='')),
                ('ps_des3', models.TextField(default='')),
                ('ps_img', models.FileField(upload_to='events')),
                ('ps_cre_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='ev_des1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='event',
            name='ev_des2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='event',
            name='ev_des3',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='ev_des',
            field=models.TextField(default=''),
        ),
    ]
