from django.db import models
from django.urls import reverse
from datetime import date

CONDITIONS = (
  ('C', 'Clean'),
  ('S', 'Slightly Dirty'),
  ('D', 'Dirty')
)

class Store(models.Model):
  name = models.CharField(max_length=30)
  location = models.CharField(max_length=30)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('stores_detail', kwargs={'pk': self.id})


# Create your models here.
class Shoe(models.Model):
  model_name = models.CharField(max_length=40)
  brand_name = models.CharField(max_length=20)
  colorway = models.CharField(max_length=20)
  size = models.IntegerField()
  stores = models.ManyToManyField(Store)

  def __str__(self):
    return self.model_name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'shoe_id': self.id})

  def clean_for_today(self):
    return self.cleaning_set.filter(date=date.today()).count() >= len(CONDITIONS)

class Cleaning(models.Model):
  date = models.DateField()
  condition = models.CharField(
    max_length=1,
    choices=CONDITIONS,
    default=CONDITIONS[0][0]
    )
  shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

  def __str__(self):
    return f'The shoe is {self.get_condition_display()} on {self.date}'

  class Meta:
    ordering = ['-date']