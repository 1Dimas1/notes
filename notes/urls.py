from django.urls import path
from . import views
from .views import HomeNotesView, NoteDetailView, CreateNoteView, UpdateNoteView, DeleteNoteView

urlpatterns = [
    path('', HomeNotesView.as_view(), name='home'),
    path('note/<int:pk>', NoteDetailView.as_view(), name='note-detail'),
    path('add_note/', CreateNoteView.as_view(), name='create_note'),
    path('note/edit/<int:pk>', UpdateNoteView.as_view(), name='edit-note'),
    path('note/<int:pk>/remove', DeleteNoteView.as_view(), name='delete-note'),
    path('search', views.search, name='search'),
    path('sign_up', views.sign_up, name='sign-up'),

]
