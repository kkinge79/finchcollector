from django.shortcuts import render

from django.http import HttpResponse


class Finch:  
  def __init__(self, name, sex, description, color):
    self.name = name
    self.sex = sex
    self.description = description
    self.color = color

finches = [
  Finch('Dee', 'female', 'Kinda rude.', 'brown'),
  Finch('Big Bird', 'male', 'Looks like a robot.', 'yellow'),
  Finch('gogurt', 'female', 'Happy fluff ball.', 'blue'),
  Finch('Bico', 'female', 'chirps loudly.', 'red')
]
def home(request):
  return HttpResponse('<h1>HELLO WORLD</h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {'finches' : finches })