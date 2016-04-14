# -*- coding: UTF-8 -*-

from django.conf.urls import url

import inventory.api.methods as api


urlpatterns = [
    url(r'^add_item/?$', api.add_item),
    url(r'^remove_item/?$', api.remove_item),
    url(r'^get_inventory/?$', api.get_inventory),
]
