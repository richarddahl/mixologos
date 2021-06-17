from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext as _ug


# Create your models here.
class Drink(models.Model):
    name = models.CharField(
	    unique=True,
        max_length=300,
        verbose_name=_('Name'))
    picture = models.FileField(
        blank=True,
        null=True,
        upload_to='media/',
        max_length=300,
        verbose_name=_('Picture'))
    base_spirits = models.ManyToManyField(
        'BaseSpiritMeasurement',
	    blank=True,
        verbose_name=_('Base Spirits'))
    sweeteners = models.ManyToManyField(
        'SweetenerMeasurement',
	    blank=True,
        verbose_name=_('Sweeteners'))
    juices = models.ManyToManyField(
        'JuiceMeasurement',
	    blank=True,
        verbose_name=_('Juices'))
    other_ingredient = models.ManyToManyField(
        'OtherMeasurement',
	    blank=True,
        verbose_name=_('Other Ingredients'))
    garnishes = models.ManyToManyField(
        'Garnish',
	    blank=True,
        verbose_name=_('Garnishes'))
    preparation = models.ForeignKey(
        'Preparation',
        on_delete=models.CASCADE,
        verbose_name=_('Preparation'))
    glass = models.ForeignKey(
        'Glass',
        on_delete=models.CASCADE,
        verbose_name=_('Glass'))
    preparations = models.ForeignKey(
        'Instruction',
        on_delete=models.CASCADE,
        verbose_name=_('Instructions'))

    class Meta:
        ordering = ['name']
        verbose_name = _ug('Drink')
        verbose_name_plural = _ug('Drinks')

    def __str__(self):
        return f'{self.name}'


class Ingredient(models.Model):
    name = models.CharField(
	    unique=True,
        max_length=300,
        verbose_name=_('Name'))
    ingredient_type = models.ForeignKey(
        'IngredientType',
        on_delete=models.CASCADE,
        verbose_name=_('Ingredient Type'))


    class Meta:
        ordering = ['name']
        verbose_name = _ug('Ingredient')
        verbose_name_plural = _ug('Ingredients')

    def __str__(self):
        return f'{self.name}'


class IngredientType(models.Model):
    name = models.CharField(
	    unique=True,
        max_length=300,
        verbose_name=_('Name'))


    class Meta:
        ordering = ['name']
        verbose_name = _ug('Ingredient Type')
        verbose_name_plural = _ug('Ingredient Types')

    def __str__(self):
        return f'{self.name}'


class Preparation(models.Model):
    name = models.CharField(
	    unique=True,
        max_length=300,
        verbose_name=_('Name'))


    class Meta:
        ordering = ['name']
        verbose_name = _ug('Preparation')
        verbose_name_plural = _ug('Preparations')

    def __str__(self):
        return f'{self.name}'


class BaseSpiritMeasurement(models.Model):
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE,
	    limit_choices_to={'ingredient_type__name': 'Base Spirit'},
        verbose_name=_('Ingredient'))
    measurement = models.ForeignKey(
        'Measurement',
        on_delete=models.CASCADE,
        verbose_name=_('Measurement'))

    class Meta:
        verbose_name = _ug('Base Spirit Measurement')
        verbose_name_plural = _ug('Base Spirit Measurements')

    def __str__(self):
        return f'{self.measurement} of {self.ingredient}'


class SweetenerMeasurement(models.Model):
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE,
	    limit_choices_to={'ingredient_type__name': 'Sweetener'},
        verbose_name=_('Ingredient'))
    measurement = models.ForeignKey(
        'Measurement',
        on_delete=models.CASCADE,
        verbose_name=_('Measurement'))

    class Meta:
        verbose_name = _ug('Sweetener Measurement')
        verbose_name_plural = _ug('Sweetener Measurements')

    def __str__(self):
        return f'{self.measurement} of {self.ingredient}'


class JuiceMeasurement(models.Model):
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE,
	    limit_choices_to={'ingredient_type__name': 'Juice'},
        verbose_name=_('Ingredient'))
    measurement = models.ForeignKey(
        'Measurement',
        on_delete=models.CASCADE,
        verbose_name=_('Measurement'))

    class Meta:
        verbose_name = _ug('Juice Measurement')
        verbose_name_plural = _ug('Juice Measurements')

    def __str__(self):
        return f'{self.measurement} of {self.ingredient}'


class OtherMeasurement(models.Model):
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE,
	    limit_choices_to={'ingredient_type__name': 'Other'},
        verbose_name=_('Ingredient'))
    measurement = models.ForeignKey(
        'Measurement',
        on_delete=models.CASCADE,
        verbose_name=_('Measurement'))

    class Meta:
        verbose_name = _ug('Other Ingredient Measurement')
        verbose_name_plural = _ug('Other Ingredient Measurements')

    def __str__(self):
        return f'{self.measurement} of {self.ingredient}'


class Measurement(models.Model):
    name = models.CharField(
	    unique=True,
        max_length=300,
        verbose_name=_('Name'))
    quantity = models.FloatField(
	    verbose_name=_('Quantity'))
    measurement_unit = models.ForeignKey(
        'MeasurementUnit',
        on_delete=models.CASCADE,
        verbose_name=_('Measurement Unit'))
 

    class Meta:
        verbose_name = _ug('Measurement')
        verbose_name_plural = _ug('Measurements')

    def __str__(self):
        return f'{self.name}'

    def convert_measurement(self, unit):
        """
        """
        if unit == 'Mililiter' and self.measurement_unit.name == 'Ounce':
            return self.quantity * 29.57
        if unit == 'Ounce' and self.measurement_unit.name == 'Mililiter':
            return self.quantity / 29.57
        if unit == 'Gallon' and self.measurement_unit.name == 'Ounce':
            return self.quantity / 133.2275 
        if unit == 'Ounce' and self.measurement_unit.name == 'Gallon':
            return self.quantity * 133.2275 


class MeasurementUnit(models.Model):
    name = models.CharField(
	    unique=True,
        max_length=300,
        verbose_name=_('Name'))

    class Meta:
        verbose_name = _ug('Measurement Unit')
        verbose_name_plural = _ug('Measurement Units')

    def __str__(self):
        return f'{self.name}'


class Garnish(models.Model):
    name = models.CharField(
	    unique=True,
	    max_length=300,
	    verbose_name=_('Name'))
 

    class Meta:
        verbose_name = _ug('Garnish')
        verbose_name_plural = _ug('Garnishes')

    def __str__(self):
        return f'{self.name}'


class Glass(models.Model):
    name = models.CharField(
	    unique=True,
        max_length=300,
        verbose_name=_('Name'))
    picture = models.FileField(
        blank=True,
        null=True,
        upload_to='media/',
        max_length=300,
        verbose_name=_('Picture'))
 

    class Meta:
        verbose_name = _ug('Glass')
        verbose_name_plural = _ug('Glasses')

    def __str__(self):
        return f'{self.name}'


class Instruction(models.Model):
    number = models.PositiveBigIntegerField(
        verbose_name=_('Number'))
    text = models.TextField(
        max_length=300,
        verbose_name=_('Name'))
 

    class Meta:
        ordering = ['number']
        verbose_name = _ug('Instruction')
        verbose_name_plural = _ug('Instructions')

    def __str__(self):
        return f'{self.number}: {self.text}'