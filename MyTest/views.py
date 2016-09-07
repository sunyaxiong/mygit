#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, View, DetailView
from demo.models import Book, Author
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.utils import timezone

class AboutView(TemplateView):
    template_name = 'demo.html'

class BookListView(ListView):
    model = Book
    template_name = 'demo.html'

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest('publication_date')
        response = HttpResponse('')
        # RFC 1123 date format
        response['Last-Modified'] = last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response

class MyView(View):

    @method_decorator(login_required)
    def get(self, request):
        return HttpResponse('result')

from demo.models import Publisher

class PublisherList(ListView):
    queryset = Publisher.objects.filter(name='jx')
    context_object_name = 'pub_list'


class PublisherDetail(DetailView):

    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context


class PublisherBookList(ListView):

    template_name = 'demo/publisher_list.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherBookList, self).get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher
        return context

class AuthorDetailView(DetailView):

    template_name = 'demo/publisher_list.html'
    queryset = Author.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(AuthorDetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object