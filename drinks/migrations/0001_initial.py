# Generated by Django 3.1.7 on 2021-06-15 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseSpiritMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Base Spirit Measurement',
                'verbose_name_plural': 'Base Spirit Measurements',
            },
        ),
        migrations.CreateModel(
            name='Garnish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Garnish',
                'verbose_name_plural': 'Garnishes',
            },
        ),
        migrations.CreateModel(
            name='Glass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True, verbose_name='Name')),
                ('picture', models.FileField(max_length=300, upload_to='media/', verbose_name='Picture')),
            ],
            options={
                'verbose_name': 'Glass',
                'verbose_name_plural': 'Glasses',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredients',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='IngredientType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Ingredient Type',
                'verbose_name_plural': 'Ingredient Types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveBigIntegerField(verbose_name='Number')),
                ('text', models.TextField(max_length=300, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Instruction',
                'verbose_name_plural': 'Instructions',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True, verbose_name='Name')),
                ('quantity', models.FloatField(verbose_name='Quantity')),
            ],
            options={
                'verbose_name': 'Measurement',
                'verbose_name_plural': 'Measurements',
            },
        ),
        migrations.CreateModel(
            name='MeasurementUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Measurement Unit',
                'verbose_name_plural': 'Measurement Units',
            },
        ),
        migrations.CreateModel(
            name='Preparation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Preparation',
                'verbose_name_plural': 'Preparations',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SweetenerMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(limit_choices_to={'ingredient_type__name': 'Sweetener'}, on_delete=django.db.models.deletion.CASCADE, to='drinks.ingredient', verbose_name='Ingredient')),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinks.measurement', verbose_name='Measurement')),
            ],
            options={
                'verbose_name': 'Sweetener Measurement',
                'verbose_name_plural': 'Sweetener Measurements',
            },
        ),
        migrations.CreateModel(
            name='OtherMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(limit_choices_to={'ingredient_type__name': 'Other'}, on_delete=django.db.models.deletion.CASCADE, to='drinks.ingredient', verbose_name='Ingredient')),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinks.measurement', verbose_name='Measurement')),
            ],
            options={
                'verbose_name': 'Other Ingredient Measurement',
                'verbose_name_plural': 'Other Ingredient Measurements',
            },
        ),
        migrations.AddField(
            model_name='measurement',
            name='measurement_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinks.measurementunit', verbose_name='Measurement Unit'),
        ),
        migrations.CreateModel(
            name='JuiceMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(limit_choices_to={'ingredient_type__name': 'Juice'}, on_delete=django.db.models.deletion.CASCADE, to='drinks.ingredient', verbose_name='Ingredient')),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinks.measurement', verbose_name='Measurement')),
            ],
            options={
                'verbose_name': 'Juice Measurement',
                'verbose_name_plural': 'Juice Measurements',
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='ingredient_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinks.ingredienttype', verbose_name='Ingredient Type'),
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True, verbose_name='Name')),
                ('picture', models.FileField(max_length=300, upload_to='media/', verbose_name='Picture')),
                ('base_spirits', models.ManyToManyField(blank=True, to='drinks.BaseSpiritMeasurement', verbose_name='Base Spirits')),
                ('garnishes', models.ManyToManyField(blank=True, to='drinks.Garnish', verbose_name='Garnishes')),
                ('glass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinks.glass', verbose_name='Glass')),
                ('juices', models.ManyToManyField(blank=True, to='drinks.JuiceMeasurement', verbose_name='Juices')),
                ('other_ingredient', models.ManyToManyField(blank=True, to='drinks.OtherMeasurement', verbose_name='Other Ingredients')),
                ('preparation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinks.preparation', verbose_name='Preparation')),
                ('preparations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinks.instruction', verbose_name='Instructions')),
                ('sweeteners', models.ManyToManyField(blank=True, to='drinks.SweetenerMeasurement', verbose_name='Sweeteners')),
            ],
            options={
                'verbose_name': 'Drink',
                'verbose_name_plural': 'Drinks',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='basespiritmeasurement',
            name='ingredient',
            field=models.ForeignKey(limit_choices_to={'ingredient_type__name': 'Base Spirit'}, on_delete=django.db.models.deletion.CASCADE, to='drinks.ingredient', verbose_name='Ingredient'),
        ),
        migrations.AddField(
            model_name='basespiritmeasurement',
            name='measurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinks.measurement', verbose_name='Measurement'),
        ),
    ]
