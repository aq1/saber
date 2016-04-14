# -*- coding: UTF-8 -*-

import json

from inventory.functions import JsonResponse
from inventory.models import Wizards, InventoryItem


def remove_item(request):
    """
    Remove item from inventory.
    """

    try:
        params = json.loads(request.body)
        pos_x = params['pos_x']
        pos_y = params['pos_y']
        wizard_name = params['wizard_name']
        wizard = Wizards.objects.get(wizard_name=wizard_name)
        item = InventoryItem.objects.get(wizard=wizard, pos_x=pos_x, pos_y=pos_y)
    except ValueError:
        return JsonResponse({'ok': False, 'reason': 'Bad request'})
    except KeyError as e:
        return JsonResponse({'ok': False, 'reason': 'Need {} parameter'.format(e)})
    except Wizards.DoesNotExist:
        return JsonResponse({'ok': False, 'reason': 'Wizard "{}" was not found'.format(wizard_name)})
    except InventoryItem.DoesNotExist:
        return JsonResponse({'ok': False, 'reason': 'Item was not found'})
    else:
        item.delete()
        return JsonResponse({'ok': True})
