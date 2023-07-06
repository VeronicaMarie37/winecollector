from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Wine


# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def wines_index(request):
  wines = Wine.objects.all()
  return render(request, 'wines/index.html', {
    'wines': wines
  })

def wines_detail(request, wine_id):
  wine= Wine.objects.get(id=wine_id)
  return render(request, 'wines/detail.html', { 
    'wine': wine 
    })

class WineCreate(CreateView):
  model = Wine
  fields = '__all__'
   # Special string pattern Django will use
  # success_url = '/wines/{wine_id}' # <--- must specify an exact ID
  # # Or..more fitting... you want to just redirect to the index page
  # # success_url = '/wines'


class WineUpdate(UpdateView):
    model = Wine
  # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['color', 'origin','description', 'age']

class WineDelete(DeleteView):
  model = Wine
  success_url = '/wines'