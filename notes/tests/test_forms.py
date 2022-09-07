from django.test import TestCase

from ..models import Category
from ..forms import NotesFormAdd


class NotesFormAddTest(TestCase):
    def setUp(self) -> None:
        self.form = NotesFormAdd()

    def test_notes_form_title_lable(self):
        self.assertTrue(self.form['title'].value() is None or self.form['title'].value() == 'Title')

    def test_notes_form_text_lable(self):
        self.assertTrue(self.form['text'].value() is None or self.form['text'].value() == 'Text')

    def test_notes_form_reminder_lable(self):
        self.assertTrue(self.form['reminder'].value() is None or self.form['reminder'].value() == 'Reminder')

    def test_notes_form_category_lable(self):
        self.assertTrue(self.form['cat'].value() is None or self.form['cat'].value() == 'Category')
