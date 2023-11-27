from django.test import TestCase
from django.urls import reverse
from .models import Task
from .forms import TaskForm


class CRUD_Task_Test(TestCase):
    
    @classmethod
    def setUpTestData(cls):

        '''Create user'''
        User.objects.create(
                first_name='Rodion',
                last_name='Raskol`nikov',
                username='Dostoevsky',
                password='1866'
                )

        '''Create task'''
        Task.objects.create(
                name='Finish the project',
                description='',
                status='')

        Task.objects.create(
                name='Start learning English',
                description='',
                status='')


    #READ
    def test_ListTasks(self):
        user = User.objects.get(id=1)

        '''Not authentication'''
        resp = self.client.get(reverse('tasks'))
        self.assertEqual(resp.status_code, 302)
        self.assertIn('login', resp.url)

        '''Authentication'''
        self.client.force_login(user)

        resp = self.client.get(reverse('tasks'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['tasks']) == 2)

    
    #CREATE
    def test_CreateTask(self):
        user = User.objects.get(id=1)

        '''Not authentication'''
        resp = self.client.get(reverse('create_task'))
        self.assertEqual(resp.status_code, 302)
        self.assertIn('login', resp.url)

        '''Authentication'''
        self.client.force_login(user)
        resp = self.client.get(reverse('create_task'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='task/create.html')

        resp = self.client.post(
                reverse('create_task'),
                {'name': 'Complete the fifth step of the project'})
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('tasks'))


    #UPDATE
    def test_CreateTask(self):
        user = User.objects.get(id=1)
        task = Task.objects.get(id=1)

        '''Not authentiComplete the fifth step of the projectcation'''
        resp = self.client.get(
            reverse('update_task', kwargs={'pk': status.id})
        )
        self.assertEqual(resp.status_code, 302)
        self.assertIn('login', resp.url)

        '''Authentication'''
        self.client.force_login(user)

        resp = self.client.get(
            reverse('update_task', kwargs={'pk': status.id})
        )
        self.assertEqual(resp.status_code, 200)


        resp = self.client.post(
            reverse('update_task', kwargs={'pk': status.id}),
            {'name': 'Work out'}
        )
        self.assertEqual(resp.status_code, 302)
        status.refresh_from_db()
        self.assertEqual(task.name, 'Work out')


    #DELETE
    def test_DeleteTask(self):
        user = User.objects.get(id=1)
        task = Task.objects.get(id=2)

        '''Not authentication'''
        resp = self.client.get(
            reverse('delete_task', kwargs={'pk': task.id})
        )
        self.assertEqual(resp.status_code, 302)
        self.assertIn('login', resp.url)

        '''Authentication'''
        self.client.force_login(user)

        resp = self.client.get(
            reverse('delete_task', kwargs={'pk': task.id})
        )
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post(
                reverse('delete_task', kwargs={'pk': user.id})
                )
        self.assertRedirects(resp, reverse('tasks'))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
