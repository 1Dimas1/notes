from django.test import TestCase, Client
from django.urls import reverse

import datetime
from ..models import Category, Note


class CreateNoteViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.client.enforce_csrf_checks = True
        cat = Category(title='Wow!')
        cat.save()
        self.test_data_for_new_note = {
            'title': 'Developing new project',
            'text': 'New dummy text',
            'reminder': '2022-09-08',
            'cat': cat.id
        }

    def test_new_note_addition_url_exists(self):
        response = self.client.get(reverse('create_note'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/add_note.html')

    def test_add_new_note(self):
        response = self.client.post(reverse('create_note'), data=self.test_data_for_new_note)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.last().title, 'Developing new project')
        self.assertRedirects(response, f'/note/{Note.objects.last().pk}')


class UpdateNoteViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.test_category = Category(title='Meetings')
        self.test_category.save()
        self.test_note = Note(title='Job Meeting', text='This is a job meeting', reminder='2023-03-04',
                              cat=self.test_category)
        self.test_note.save()
        self.new_title = 'Title is changed'
        self.new_text = 'Text is changed'
        self.new_reminder = '2022-05-06'
        self.new_cat = Category(title='Category is changed')
        self.new_cat.save()

    def test_note_updating_url_exists(self):
        response = self.client.get(reverse('edit-note', kwargs={'pk': self.test_note.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/edit_note.html')

    def test_note_update_title(self):
        response = self.client.post(reverse('edit-note', kwargs={'pk': self.test_note.pk}),
                                    data={
                                        'title': self.new_title,
                                        'text': self.test_note.text,
                                        'reminder': self.test_note.reminder,
                                        'cat': self.test_category.id
                                    })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/note/{self.test_note.pk}')
        title = Note.objects.all().get(id=self.test_note.id).title
        self.assertEqual(title, 'Title is changed')

    def test_note_update_text(self):
        response = self.client.post(reverse('edit-note', kwargs={'pk': self.test_note.pk}),
                                    data={
                                        'title': self.new_title,
                                        'text': self.new_text,
                                        'reminder': self.test_note.reminder,
                                        'cat': self.test_category.id
                                    })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/note/{self.test_note.pk}')
        text = Note.objects.all().get(id=self.test_note.id).text
        self.assertEqual(text, 'Text is changed')

    def test_note_update_reminder(self):
        response = self.client.post(reverse('edit-note', kwargs={'pk': self.test_note.pk}),
                                    data={
                                        'title': self.new_title,
                                        'text': self.new_text,
                                        'reminder': self.new_reminder,
                                        'cat': self.test_category.id
                                    })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/note/{self.test_note.pk}')
        reminder = Note.objects.all().get(id=self.test_note.id).reminder
        self.assertEqual(reminder, datetime.date(2022, 5, 6))

    def test_note_update_reminder(self):
        response = self.client.post(reverse('edit-note', kwargs={'pk': self.test_note.pk}),
                                    data={
                                        'title': self.new_title,
                                        'text': self.new_text,
                                        'reminder': self.new_reminder,
                                        'cat': self.new_cat.id
                                    })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/note/{self.test_note.pk}')
        category = Note.objects.all().get(id=self.test_note.id).cat.title
        self.assertEqual(category, 'Category is changed')

