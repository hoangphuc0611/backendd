# cities/models.py
from django.db import models


class City(models.Model):
    stt = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    ban_giao = models.CharField(max_length=255)
    loai_hinh = models.CharField(max_length=255)
    quy_mo = models.CharField(max_length=255)
    so_tang = models.CharField(max_length=255)
    dien_tich = models.CharField(max_length=255)
    toa_do = models.CharField(max_length=255)
    image = models.CharField(max_length=255)


    def __str__(self):
        return self.name

class QH(models.Model):
    stt = models.CharField(max_length=255)
    html = models.TextField(max_length=10000)


    def __str__(self):
        return self.stt