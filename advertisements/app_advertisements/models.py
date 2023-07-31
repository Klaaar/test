from django.db import models

# Create your models here.
class Advertisements(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)#max_digits-макс допуст знаков в числе,decimal_places- кол-во десятичных разрядов(цифрф после запятой)
    auction = models.BooleanField("торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
