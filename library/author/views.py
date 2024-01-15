from django.shortcuts import render
from django.views.generic import ListView, DetailView
from author.models import Author
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from book.models import Book
from author.forms import AuthorForm


class AuthorPage(ListView):
    model = Author
    template_name = "author/author.html"
    context_object_name = 'authors'
    ordering = 'surname'


class AuthorDetails(DetailView):
    model = Author
    template_name = "author/author_details.html"
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        context['books'] = Book.objects.filter(authors=author)
        return context


def remove_author(request, author_id):
    if request.method == 'POST':
        try:
            author = Author.objects.get(pk=author_id)
            books_authors = Book.objects.filter(authors=author)
        except Author.DoesNotExist:
            raise Http404("Question does not exist")
        if len(books_authors) == 0:
            author.delete()
        return HttpResponseRedirect(reverse('author:author'))


def submit_add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('author:author'))
        else:
            return render(request, template_name='author/author_create.html', context={'form': form})
    else:
        form = AuthorForm()
        return render(request, template_name='author/author_create.html', context={'form': form})
