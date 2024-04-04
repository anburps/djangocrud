from django.shortcuts import redirect, render

from django.urls import reverse_lazy
from curdapp.form import CrudForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from curdapp.models import CrudView
# Create your views here.

class BookListView(ListView):
    model = CrudView
    template_name = 'createlist.html'

class BookCreateView(CreateView):
    model = CrudView
    form_class = CrudForm
    template_name = 'createform.html'
    
    success_url = reverse_lazy('book_create')
    

    def get_success_url(self):
        # Print the object when determining the success URL
        print(self.object)
        return super().get_success_url()
    
class BookUpdateView(UpdateView):
    model = CrudView
    form_class = CrudForm
    template_name = 'createform.html'
    success_url = reverse_lazy('createlist')

class BookDeleteView(DeleteView):
    model = CrudView
    success_url = reverse_lazy('createlist')