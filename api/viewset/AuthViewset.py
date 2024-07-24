import json
from rest_framework import viewsets
from rest_framework.response import Response
from django.views.generic import (View, TemplateView, CreateView, UpdateView, ListView)
from api.core.request import Request
from api.constant import URL_API


class LoginViewset(viewsets.ModelViewSet, Request):

    def post(self, request, *args, **kwargs):
        # jwt = self._get_jwt(request)
        data = json.loads(request.body)
        url = URL_API + '/login/'
        req = self.requestData(data, url, "")
        return Response(req, status=200)
    
    def _get_jwt(self, data):
        data = data.META
        try:  
          return data.Authorization
        except Exception as e:
          return