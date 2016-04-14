# -*- coding: UTF-8 -*-

import json

from inventory.functions import JsonResponse
from inventory.models import Wizards, InventoryItem


def abracadabra(request):
    """
    Craft items in wizards's inventory.
    """

    try:
        name = json.loads(request.body)['wizard_name']
        wizard = Wizards.objects.get(wizard_name=name)
    except ValueError:
        resp = {'ok': False, 'reason': 'Bad request'}
    except KeyError:
        resp = {'ok': False, 'reason': 'Need "wizard_name" parameter'}
    except Wizards.DoesNotExist:
        resp = {'ok': False, 'reason': 'Wizard "{}" was not found'.format(name)}

    items = InventoryItem.objects.filter(wizard=wizard)

    return JsonResponse(resp)
