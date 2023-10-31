from django.db import models

class Аpartments(models.Model):
    name=models.CharField("Название",max_length=50)
    price=models.IntegerField("Цена")
    adress=models.CharField("Адрес",max_length=40)
    guests=models.IntegerField("Количество гостей")
    beds=models.IntegerField("Количество спальныx мест")
    photo=models.ImageField("Фотография", upload_to="my_first_app/photos",default="",blank=True)

    class Meta:
        verbose_name="Квартира"
        verbose_name_plural="Квартиры"
        ordering=["id"]


    def __str__(self):
        return "Квартира {}".format(self.adress)
        """ еще один способ форматирования строки """
        """ return f"Квартира {self.adress}" """