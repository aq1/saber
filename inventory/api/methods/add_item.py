# -*- coding: UTF-8 -*-

import json

from inventory.functions import JsonResponse
from inventory.models import Wizards, MagicItems, InventoryItem


def add_item(request):
    """
    Add item into player's inventory.
    The method looks heavy.
    I need to check if the place is empty before adding an item.
    """

    try:
        params = json.loads(request.body)
        wizard_name = params['wizard_name']
        item_name = params['item_name']
        pos_x = params['pos_x']
        pos_y = params['pos_y']
        wizard = Wizards.objects.get(wizard_name=wizard_name)
        item = MagicItems.objects.get(item_name=item_name)
    except ValueError:
        return JsonResponse({'ok': False, 'reason': 'Bad request'})
    except KeyError as e:
        return JsonResponse({'ok': False, 'reason': 'Need {} parameter'.format(e)})
    except Wizards.DoesNotExist:
        return JsonResponse({'ok': False, 'reason': 'Wizard "{}" was not found'.format(wizard_name)})
    except MagicItems.DoesNotExist:
        return JsonResponse({'ok': False, 'reason': 'Magic Item "{}" was not found'.format(item_name)})

    for each in InventoryItem.objects.filter(wizard=wizard).select_related('item'):
        if (each.pos_x <= pos_x <= each.pos_x + each.item.size_x and
                each.pos_y <= pos_y <= each.pos_y + each.item.size_y):
            return JsonResponse({'ok': False, 'reason': 'Bad position'})

    try:
        new_item = InventoryItem.objects.create(wizard=wizard, item=item, pos_x=pos_x, pos_y=pos_y)
    except ValueError as e:
        return JsonResponse({'ok': False, 'reason': str(e)})

    return JsonResponse({'ok': True, 'id': new_item.id})
