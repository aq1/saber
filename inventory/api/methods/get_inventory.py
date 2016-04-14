# -*- coding: UTF-8 -*-

import json

from inventory.functions import JsonResponse
from inventory.models import Wizards, InventoryItem


def get_inventory(request):
    """
    Get list of items for a player.
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
    else:
        resp = {
            'ok': True,
            'items': list(InventoryItem.objects.values().filter(wizard=wizard))
        }

    return JsonResponse(resp)
