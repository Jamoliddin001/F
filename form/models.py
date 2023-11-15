from django.db import models

# Create your models here.

class FormTemplate(models.Model):
    name = models.CharField(max_length=255)
    field_name_1 = models.CharField(max_length=255)
    field_name_2 = models.CharField(max_length=255)
    data_create = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name