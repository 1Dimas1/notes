from django.test import TestCase

from ..models import Note, Category


class NoteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(title='Sports')
        Note.objects.create(title='Football', text='Tournament in Kyiv',
                            reminder='2022-10-04', cat=category)
        Note.objects.create(title='Basketball', text='Tournament in Lviv',
                            reminder='2022-12-11', cat=category)

    def test_title_lable(self):
        note = Note.objects.get(id=1)
        field_label = note._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Title')

    def test_text_lable(self):
        note = Note.objects.get(id=1)
        field_label = note._meta.get_field('text').verbose_name
        self.assertEqual(field_label, 'Text')

    def test_reminder_lable(self):
        note = Note.objects.get(id=1)
        field_label = note._meta.get_field('reminder').verbose_name
        self.assertEqual(field_label, 'Reminder')

    def test_category_lable(self):
        note = Note.objects.get(id=1)
        field_label = note._meta.get_field('cat').verbose_name
        self.assertEqual(field_label, 'Category')

    def test_title_max_length(self):
        note = Note.objects.get(id=1)
        max_length = note._meta.get_field('title').max_length
        self.assertEqual(max_length, 250)

    def test_text_max_length(self):
        note = Note.objects.get(id=1)
        max_length = note._meta.get_field('title').max_length
        self.assertEqual(max_length, 250)

    def test_reminder_max_length(self):
        note = Note.objects.get(id=1)
        max_length = note._meta.get_field('reminder').max_length
        self.assertEqual(max_length, 100)

    def test_get_absolute_url(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.get_absolute_url(), '/note/1')

    def test_object_representation(self):
        note = Note.objects.get(id=1)
        expected_representation = f'{note.title}'
        self.assertEqual(str(note), expected_representation)

    def test_objects_ordering(self):
        notes = Note.objects.all()
        expected_ordering = Note.objects.all().order_by('title')
        objects_ordering = Note.objects.all()
        self.assertQuerysetEqual(objects_ordering, expected_ordering)

    def test_model_verbose_name_plural(self):
        model_plural_name = Note._meta.verbose_name_plural.title()
        self.assertEqual(model_plural_name, 'Notes')


class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title='Home')

    def test_title_lable(self):
        field_label = self.category._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Title')

    def test_title_max_length(self):
        max_length = self.category._meta.get_field('title').max_length
        self.assertEqual(max_length, 250)

    def test_object_representation(self):
        expected_representation = f'{self.category.title}'
        self.assertEqual(str(self.category), expected_representation)

    def test_objects_ordering(self):
        expected_ordering = Category.objects.all().order_by('title')
        objects_ordering = Category.objects.all()
        self.assertQuerysetEqual(objects_ordering, expected_ordering)

    def test_model_verbose_name_plural(self):
        model_plural_name = Category._meta.verbose_name_plural.title()
        self.assertEqual(model_plural_name, 'Categories')