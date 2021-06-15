from django.contrib import admin
from mixologos.drinks.models import *

# Register your models here.
admin.site.register(Drink)
admin.site.register(Ingredient)
admin.site.register(Measurement)
admin.site.register(MeasurementUnit)
admin.site.register(BaseSpiritMeasurement)
admin.site.register(JuiceMeasurement)
admin.site.register(SweetenerMeasurement)
admin.site.register(OtherMeasurement)
admin.site.register(Glass)
admin.site.register(Garnish)
admin.site.register(IngredientType)
admin.site.register(Instruction)
