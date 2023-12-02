from django.test import TestCase
from django.urls import reverse
from .models import Task
from django.contrib.auth.models import User
from task_manager.statuses.models import Status

class CRUD_Task_Test(TestCase):
    def setUp(self):
        '''Create user'''
        User.objects.create(
                first_name='Rodion',
                last_name='Raskol`nikov',
                username='Dostoevsky',
                password='1866'
                )
        self.user = User.objects.get(id=1)

        '''Create status'''
        Status.objects.create(name='status1')
        self.status = Status.objects.get(id=1)


        '''Create task'''
        Task.objects.create(
                name='Finish the project',
                description='',
                status=self.status,
                author=self.user)

        Task.objects.create(
                name='Start learning English',
                description='',
                status=self.status,
                author=self.user)


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
        status = Status.objects.get(id=1)

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
                {'name': 'Complete the fifth step of the project',
                 'status': status,
                 'description': '',
                 'author': user})

        task = Task.objects.get(id=1)
        tasks = Task.objects.all()
        print(tasks)
                   
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('tasks'))

    #UPDATE
    def test_UpdateTask(self):
        user = User.objects.get(id=1)
        task = Task.objects.get(id=1)
        status = Status.objects.get(id=1)

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
            {'description':'123'})
    
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
        self.assertIn('login', resp.url)

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

   # '''Verification addresses'''
   # url_tasks = [
    #        reverse('tasks'),
      #      reverse('create_task'),
       #     reverse('task', kwargs={'pk': 1}),
     #       reverse('update_task', kwargs={'pk': 1}),
         #   reverse('delete_task', kwargs={'pk': 1}),
        #    ]


   # def test_access(self, urls=url_tasks):
    #    '''Not authentication'''
     #   for url in urls:
      #      resp = self.client.get(url)
       #     self.assertEqual(resp.status_code, 302)

       # '''Authentication'''
      #  self.client.force_login(self.user)
       # for url in urls:
        #    resp = self.client.get(url)
         #   print(resp)
          #  self.assertEqual(resp.status_code, 200)
