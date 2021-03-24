from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=124)

    def __str__(self):
        return self.name


INSTITUTION_TYPES = [
    ('F', 'fundacja'),
    ('OP', 'organizacja pozarządowa'),
    ('ZL', 'zbiórka lokalna'),
]

class Institution(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.CharField(max_length=2, choices=INSTITUTION_TYPES, default='F')
    categories = models.ManyToManyField(Category, related_name='institution')


    # @property
    # def categories(self):
    #     all_categories = Category.objects.filter(institution=self.pk).values_list()
    #     return all_categories

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institutions = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=16)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)