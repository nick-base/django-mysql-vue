from django.views import View
from api.helper import response_success
from api.models import GenData, SaveData
import random
import json


class Hello(View):
    def get(self, request, *args, **kwargs):
        return response_success({'test': 'hello'})


class GenDataView(View):
    def get(self, request, *args, **kwargs):
        gen_list = [random.randint(0, 100) for i in range(10)]
        gen_data = GenData()
        gen_data.data = json.dumps(gen_list)
        gen_data.save()
        return response_success({'values': gen_list})


class SaveDataView(View):
    def get(self, request, *args, **kwargs):
        save_data_list = SaveData.objects.all().order_by('-id')[:100]
        result = []
        for save_data in save_data_list:
            result.append({
                'id': save_data.id,
                'data': save_data.data
            })
        return response_success({'values': result})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        if (data and data['data']):
            save_data = SaveData()
            save_data.data = data['data']
            save_data.save()
            return response_success({'id': save_data.id})
        return response_success({'id': -1})
