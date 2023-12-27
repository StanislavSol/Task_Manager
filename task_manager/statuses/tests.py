from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.users.models import User


class CRUD_Status_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''Create user'''
        User.objects.create(
            first_name='Rodion',
            last_name='Raskol`nikov',
            username='Dostoevsky',
            password='1866'
        )
        '''Create statuses'''
        Status.objects.create(name='At work')
        Status.objects.create(name='Сompleted')

    # READ
    def test_ListStatus(self):
        user = User.objects.get(id=1)

        '''Not authentication'''
        resp = self.client.get(reverse('statuses'))
        self.assertEqual(resp.status_code, 302)

        '''Authentication'''
        self.client.force_login(user)

        resp = self.client.get(reverse('statuses'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['statuses']) == 2)

    # CREATE
    def test_CreateStatus(self):
        user = User.objects.get(id=1)

        '''Not authentication'''
        resp = self.client.get(reverse('create_status'))
        self.assertEqual(resp.status_code, 302)

        '''Authentication'''
        self.client.force_login(user)
        resp = self.client.get(reverse('create_status'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='statuses/create.html')

        resp = self.client.post(
            reverse('create_status'),
            {'name': 'On testing'}
        )
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('statuses'))

    # UPDATE
    def test_UpdateStatus(self):
        user = User.objects.get(id=1)
        status = Status.objects.get(id=1)

        '''Not authentication'''
        resp = self.client.get(
            reverse('update_status', kwargs={'pk': status.id})
        )
        self.assertEqual(resp.status_code, 302)

        '''Authentication'''
        self.client.force_login(user)

        resp = self.client.get(
            reverse('update_status', kwargs={'pk': status.id})
        )
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post(
            reverse('update_status', kwargs={'pk': status.id}),
            {'name': 'New'}
        )
        self.assertEqual(resp.status_code, 302)
        status.refresh_from_db()
        self.assertEqual(status.name, 'New')

    # DELETE
    def test_DeleteStatus(self):
        user = User.objects.get(id=1)
        status = Status.objects.get(id=2)

        '''Not authentication'''
        resp = self.client.get(
            reverse('delete_status', kwargs={'pk': status.id})
        )
        self.assertEqual(resp.status_code, 302)
        self.assertIn('login', resp.url)

        '''Authentication'''
        self.client.force_login(user)

        resp = self.client.get(
            reverse(
                'delete_status',
                kwargs={'pk': status.id}
            )
        )
        self.assertEqual(resp.status_code, 200)

        resp = self.client.pos(
            reverse(
                'delete_status',
                kwargs={'pk': status.id}
            )
        )

        self.assertRedirects(resp, reverse('statuses'))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Status.objects.count(), 1)
