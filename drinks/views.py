from django.shortcuts import render
from mixologos.drinks.models import Drink

# Create your views here.

def index(request,
          drink_id=None):
    """
    """
    if drink_id:
        drink_detail = Drink.objects.get(id=drink_id)
    else:
        drink_detail = None
    return render(request,
                  'templates/index.html',
                  {'drinks': Drink.objects.all(),
                   'drink_detail': drink_detail})