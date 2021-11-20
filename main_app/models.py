from django.db import models
from django.urls import reverse

MEALS = (
  ('S', 'Seed'),
  ('W', 'Worm'),
  ('D', 'Drink')
)

class Finch(models.Model):
  name = models.CharField(max_length=100)
  sex = models.CharField(max_length=20)
  description = models.TextField(max_length=250)
  color = models.CharField(max_length=30)

  def __str__(self):
    return self.name


  def get_absolute_url(self):
    return reverse('finches_detail', kwargs={'finch_id': self.id})

class Feeding(models.Model):
  date = models.DateField('Feeding date')
  meal = models.CharField(
		max_length=1,
		choices=MEALS,
		default=MEALS[0][0]
  )
  # Create a cat_id column in the database
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"