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

    '''Verification addresses'''
    url_tasks = [
            reverse('tasks'),
            reverse('create_task'),
           # reverse('task', kwargs={'pk': 1}),
            reverse('update_task', kwargs={'pk': 1}),
            reverse('delete_task', kwargs={'pk': 1}),
            ]


    def test_access(self, urls=url_tasks):
        '''Not authentication'''
        for url in urls:
            resp = self.client.get(url)
            self.assertEqual(resp.status_code, 302)

        '''Authentication'''
      #  self.client.force_login(self.user)
       # for url in urls:
        #    resp = self.client.get(url)
         #   print(resp)
          #  self.assertEqual(resp.status_code, 200)
