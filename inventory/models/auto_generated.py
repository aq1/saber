# -*- coding: UTF-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class MagicItems(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(unique=True, max_length=64)
    size_x = models.IntegerField()
    size_y = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'magic_items'

    def __unicode__(self):
        return self.item_name


class MagicRuleIngredients(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    rule = models.ForeignKey('MagicRules', on_delete=models.PROTECT)
    item = models.ForeignKey(MagicItems, on_delete=models.PROTECT)
    pos_x = models.IntegerField()
    pos_y = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'magic_rule_ingredients'

    def __unicode__(self):
        return u'%s %sx%s' % (self.rule, self.pos_x, self.pos_y)


class MagicRules(models.Model):
    rule_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(MagicItems, on_delete=models.PROTECT)
    description = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'magic_rules'

    def __unicode__(self):
        return 'Rule for %s' % self.item


class Wizards(models.Model):
    wizard_id = models.AutoField(primary_key=True)
    wizard_name = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'wizards'

    def __unicode__(self):
        return self.wizard_name
