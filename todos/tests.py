from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import CustomUser, TodoItem, TodoSubtask
import datetime

# Create your tests here.

class UserAccountTests(TestCase):
    # Registriert User
    def test_registration(self):
        response = self.client.post(reverse('register'), data={
            'email': 'test@test.de',
            'username': 'testuser',
            'password': 'testpassword123'
        })
        self.assertTrue(CustomUser.objects.filter(email='test@test.de').exists())

    # Registeriert User und loggt ein
    def test_login(self):
        self.client.post(reverse('register'), data={
            'email': 'test@test.de',
            'username': 'testuser',
            'password': 'testpassword123'
        })
        response = self.client.post(reverse('login'), data={
            'email': 'test@test.de',
            'password': 'testpassword123',
        })

class TodoItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Ersellt Benutzer
        test_user = get_user_model().objects.create_user(email='test@test.de', username='testuser', password='12345')
        test_user.save()

        # Erstellt TodoItem
        cls.todo_item = TodoItem.objects.create(
            title='Test Todo',
            description='Test description',
            created_at=datetime.date.today(),
            priority='medium',
            category='technical',
            status='todo'
        ).users.add(test_user)

        # Erstellt Subtask für TodoItem
        TodoSubtask.objects.create(
            todo_item=TodoItem.objects.get(id=1),
            text='text subtask',
            is_completed=False
        )

    # Prüft ob TodoItem erstellt wurde
    def test_todo_item_creation(self):
        todo_item = TodoItem.objects.get(id=1)
        self.assertTrue(isinstance(todo_item, TodoItem))
        expected_str_output = f'({todo_item.id}, {todo_item.status}) {todo_item.title}'
        self.assertEqual(todo_item.__str__(), expected_str_output)
        self.assertEqual(todo_item.status, 'todo')
        self.assertEqual(todo_item.priority, 'medium')
        self.assertEqual(todo_item.category, 'technical')
        self.assertEqual(todo_item.description, 'Test description')
        self.assertEqual(todo_item.title, 'Test Todo')
        self.assertEqual(todo_item.created_at, datetime.date.today())
        self.assertEqual(todo_item.users.count(), 1)
        self.assertEqual(todo_item.users.first().username, 'testuser')

    # Prüft ob Subtask erstellt wurde
    def test_todo_subtask_creation(self):
        todo_subtask = TodoSubtask.objects.get(id=1)
        todo_item = TodoItem.objects.get(id=1)
        self.assertTrue(isinstance(todo_subtask, TodoSubtask))
        self.assertEqual(todo_subtask.todo_item.id, 1)
        self.assertEqual(todo_subtask.text, 'text subtask')
        self.assertEqual(todo_subtask.is_completed, False)

        # Überprüfen der Beziehung zum TodoItem
        self.assertEqual(todo_subtask.todo_item.id, todo_item.id)