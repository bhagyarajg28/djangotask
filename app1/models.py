from django.db import models


# Create your models here.

# class Bank(models.Model):
#     bank_name = models.CharField(max_length=64)


# class Bank(models.Model):
#     bank_name = models.CharField(max_length=64)
#     ifsc_code = models.CharField(max_length=64,unique=True)
#     bank_addr = models.CharField(max_length=64)
#     city = models.CharField(max_length=64)
#
#     def __str__(self):
#         return self.bank_name


class Branches(models.Model):
    ifsc = models.CharField(max_length=12, unique=True, blank=False)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=74, blank=False)
    address = models.CharField(max_length=195, blank=False)
    city = models.CharField(max_length=50, blank=False)
    district = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=26, blank=False)
    bank_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.bank_name
