from django.test import TestCase
from django.urls import reverse
from .models import Task
from django.contrib.auth.models import User
from task_manager.statuses.models import Status

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
        user = User.objects.get(id=1)

        '''Create status'''
        Status.objects.create(name='status1')
        status = Status.objects.get(id=1)


        '''Create task'''
        Task.objects.create(
                name='Finish the project',
                description='',
                status=status,
                author=user)

        Task.objects.create(
                name='Start learning English',
                description='',
                status=status,
                author=user)


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
        self.assertTemplateUsed(resp, template_name='tasks/create.html')

        resp = self.client.post(
                reverse('create_task'),
                data={
                    "name": "Complete the fifth step of the project",
                    "description": "new task description",
                    "status": 1,
                    "labels": [],
                    "author": 1,
                    "executor": 1
                    })

             
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('tasks'))

    #UPDATE
    def test_UpdateTask(self):
        user = User.objects.get(id=1)
        task = Task.objects.get(id=1)

        '''Not authentication'''
        resp = self.client.get(
            reverse('update_task', kwargs={'pk': task.id})
        )
        self.assertEqual(resp.status_code, 302)
        self.assertIn('login', resp.url)

        '''Authentication'''
        self.client.force_login(user)

        resp = self.client.get(
            reverse('update_task', kwargs={'pk': task.id})
        )
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post(
            reverse('update_task', kwargs={'pk': task.id}),
            data={
                "name": "Work out",
                "description": "new task description",
                "status": 1,
                "labels": [],
                "author": 1,
                "executor": 1
                })
    
        self.assertEqual(resp.status_code, 302)
        task.refresh_from_db()
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

        '''Authentication'''
        self.client.force_login(user)

        resp = self.client.get(
            reverse('delete_task', kwargs={'pk': task.id})
        )
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post(
                reverse('delete_task', kwargs={'pk': task.id})
                )
        self.assertRedirects(resp, reverse('tasks'))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
