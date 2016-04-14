# -*- coding: UTF-8 -*-

import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse


class JsonResponse(HttpResponse):

    def __init__(self, content, *args, **kwargs):
        kwargs['content_type'] = 'application/json'
        super(JsonResponse, self).__init__(
            json.dumps(content, cls=DjangoJSONEncoder), *args, **kwargs)
