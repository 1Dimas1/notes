from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import NotesFormAdd, RegistrationForm
from .models import *
from .filters import OrderFilter


class HomeNotesView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = '/login'
    model = Note
    template_name = 'notes/home_notes_list.html'
    context_object_name = 'notes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset().filter(author=self.request.user)
        my_filter = OrderFilter(self.request.GET, queryset)
        context['title'] = 'Main page'
        context['filter'] = my_filter
        return context


class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_details.html'


class CreateNoteView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = '/login'
    form_class = NotesFormAdd
    template_name = 'notes/add_note.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))
    else:
        form = RegistrationForm()
    return render(request, 'registration/sign_up.html', {'form': form})
