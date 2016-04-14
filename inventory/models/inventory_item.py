# -*- coding: UTF-8 -*-

from django.db import models


class InventoryItem(models.Model):

    """
    M2M model for item in inventory.
    I prefer explicit declaration over built-in django ManyToMany field
    """

    MIN_X, MIN_Y, MAX_X, MAX_Y = 0, 0, 4, 4

    wizard = models.ForeignKey('inventory.Wizards')
    item = models.ForeignKey('inventory.MagicItems')
    pos_x = models.PositiveSmallIntegerField()
    pos_y = models.PositiveSmallIntegerField()

    class Meta:
        app_label = 'inventory'

    def save(self, *args, **kwargs):
        if (self.pos_x > self.MAX_X or self.pos_y > self.MAX_Y or
                self.pos_x < self.MIN_X or self.pos_y < self.MIN_Y):
            raise ValueError('Position is out of bounds')

        super(InventoryItem, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'{} {} {}x{}'.format(self.wizard, self.item, self.pos_x, self.pos_y)
