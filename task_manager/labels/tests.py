from django.test import TestCase
from django.urls import reverse
from task_manager.labels.models import Label
from task_manager.users.models import User


class CRUD_Label_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''Create user'''
        User.objects.create(
            first_name='Pavel',
            last_name='Chichikov',
            username='Gogol`',
            password='1842'
        )

        '''Create lables'''
        Label.objects.create(name='Urgently')
        Label.objects.create(name='Do not rush')

    # READ
    def test_ListLabels(self):
        user = User.objects.get(id=1)

        '''Not authentication'''
        resp = self.client.get(reverse('labels'))
        self.assertEqual(resp.status_code, 302)

        '''Authentication'''
        self.client.force_login(user)

        resp = self.client.get(reverse('labels'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['labels']) == 2)

    # CREATE
    def test_CreateLabel(self):
        user = User.objects.get(id=1)

        '''Not authentication'''
        resp = self.client.get(reverse('create_label'))
        self.assertEqual(resp.status_code, 302)
        self.assertIn('login', resp.url)

        '''Authentication'''
        self.client.force_login(user)
        resp = self.client.get(reverse('create_label'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='labels/create.html')

        resp = self.client.post(reverse('create_label'), {'name': 'Control'})
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('labels'))

    # UPDATE
    def test_UpdateLabel(self):
        user = User.objects.get(id=1)
        label = Label.objects.get(id=1)

        '''Not authentication'''
        resp = self.client.get(
            reverse('update_label', kwargs={'pk': label.id})
        )
        self.assertEqual(resp.status_code, 302)
        self.assertIn('login', resp.url)

        '''Authentication'''
        self.client.force_login(user)

        resp = self.client.get(
            reverse('update_label', kwargs={'pk': label.id})
        )
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post(
            reverse('update_label', kwargs={'pk': label.id}),
            {'name': 'New label'}
        )
        self.assertEqual(resp.status_code, 302)
        label.refresh_from_db()
        self.assertEqual(label.name, 'New label')

    # DELETE
    def test_DeleteLabel(self):
        user = User.objects.get(id=1)
        label = Label.objects.get(id=2)

        '''Not authentication'''
        resp = self.client.get(
            reverse('delete_label', kwargs={'pk': label.id})
        )
        self.assertEqual(resp.status_code, 302)
        self.assertIn('login', resp.url)

        '''Authentication'''
        self.client.force_login(user)

        resp = self.client.get(
            reverse('delete_label', kwargs={'pk': label.id})
        )
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post(reverse(
            'delete_label',
            kwargs={'pk': label.id}))
        self.assertRedirects(resp, reverse('labels'))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Label.objects.count(), 1)
