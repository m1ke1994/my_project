from django.db import models
from my_first_app.models import Аpartments



class Order(models.Model):
    apartment=models.ForeignKey(Аpartments,verbose_name="Квартира",on_delete=models.CASCADE)
    name=models.CharField("Имя", max_length=50)
    phone=models.CharField("Телефон", max_length=50)
    date=models.DateTimeField("Дата заявки",auto_now_add=True)