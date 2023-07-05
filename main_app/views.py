from django.shortcuts import render

wines = [
    {'name': 'red', 'color': 'red', 'description': 'dry', 'age': 5},
    {'name': 'red', 'color': 'red', 'description': 'dry', 'age': 5},
]



# class Wine(models.Model):
#     name = models.CharField(max_length=100)
#     color = models.CharField(max_length=100)
#     origin = models.CharField(max_length=100)
#     description = models.TextField(max_length=250)
#     age = models.IntegerField()





# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def wines_index(request):
  return render(request, 'wines/index.html', {
    'wines': wines
  })