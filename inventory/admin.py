from django.contrib import admin


from inventory.models import *


@admin.register(MagicItems)
class MagicItemsAdmin(admin.ModelAdmin):

    list_display = 'item_name', 'size_x', 'size_y'


@admin.register(MagicRuleIngredients)
class MagicRuleIngredientsAdmin(admin.ModelAdmin):

    list_display = '__unicode__', 'item', 'pos_x', 'pos_y'


@admin.register(MagicRules)
class MagicRulesAdmin(admin.ModelAdmin):

    list_display = 'item', 'description'


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):

    pass


class InventoryItemInline(admin.TabularInline):

    model = InventoryItem
    extra = 1


@admin.register(Wizards)
class WizardsAdmin(admin.ModelAdmin):

    list_display = 'wizard_name',
    inlines = [InventoryItemInline]
