from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


from .forms import NotesFormAdd
from .models import *
from .filters import OrderFilter


class JsonableResponseMixin:
    """
    Mixin to add JSON support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.accepts('text/html'):
            return response
        else:
            return JsonResponse(form.errors, status=400)

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.accepts('text/html'):
            return response
        else:
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)


class HomeNotesView(ListView):
    model = Note
    template_name = 'notes/home_notes_list.html'
    context_object_name = 'notes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        my_filter = OrderFilter(self.request.GET, queryset)
        context['title'] = 'Main page'
        context['filter'] = my_filter
        return context


class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_details.html'


class CreateNoteView(JsonableResponseMixin, CreateView):
    form_class = NotesFormAdd
    template_name = 'notes/add_note.html'


class UpdateNoteView(UpdateView):
    model = Note
    form_class = NotesFormAdd
    template_name = 'notes/edit_note.html'


class DeleteNoteView(DeleteView):
    model = Note
    template_name = 'notes/delete_note.html'
    success_url = reverse_lazy('home')


def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        notes = Note.objects.filter(title__contains=searched)
        return render(request, 'notes/search.html', {'searched': searched, 'notes': notes, 'title': 'Search'})
    else:
        return render(request, 'notes/search.html', {})
