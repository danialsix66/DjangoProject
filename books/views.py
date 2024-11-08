from django.shortcuts import render
from django.views import generic
from . models import Book
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookCreateView(LoginRequiredMixin,generic.CreateView):
    model = Book
    fields = ['user','title' , 'author','translator', 'description','price' , 'cover']
    template_name = 'books/book_create.html'


class BookUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    model = Book
    fields = ['title' , 'author','translator', 'description','price' , 'cover']
    template_name = 'books/book_update.html'

    def test_func(self):
        obj=self.get_object()
        return obj.user==self.request.user


class BookDeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model=Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
    success_massages='Deleted'

    def test_func(self):
        obj=self.get_object()
        return obj.user==self.request.user