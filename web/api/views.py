from django.views import View
from api.helper import response_success

class Hello(View):
    def get(self, request, *args, **kwargs):
        return response_success({'test': 'hello'})
