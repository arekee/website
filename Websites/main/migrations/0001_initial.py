# Generated by Django 4.0.3 on 2022-04-05 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trips', models.CharField(default='', max_length=50, verbose_name='Trips')),
                ('prices', models.CharField(default='', max_length=50, verbose_name='Prices')),
                ('description', models.TextField(default='', max_length=200, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50, verbose_name='Author')),
                ('comment', models.TextField(max_length=300, verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'Пікір',
                'verbose_name_plural': 'Пікірлер',
                'ordering': ['-nickname', 'comment'],
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Hotel name')),
                ('descrip', models.TextField(max_length=200, verbose_name='Hotel description')),
            ],
        ),
    ]
