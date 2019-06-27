from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

class GenData(BaseModel):
    data = models.TextField()

    class Meta:
        db_table = 'gen_data'

class SaveData(BaseModel):
    data = models.TextField()

    class Meta:
        db_table = 'save_data'
