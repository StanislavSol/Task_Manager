from django.test import TestCase
from django.urls import reverse
from .models import Lable
from django.contrib.auth.models import User

# Create your tests here.
class CRUD_Lable_Test(TestCase):

    @classmethod
    def SetUp(cls):
        '''Create user'''
        User.objects.create(
                first_name='Rodion',
                last_name='Raskol`nikov',
                username='Dostoevsky',
                password='1866'
                )

        '''Create lable'''
        Lable.objects.create(
                name='Urgently')
        Lable.objects.create(
                name='Do not rush')

    #READ
    def test_ListLables(self):
        user = User.objects.get(id=1)

        '''Not authentication'''
        resp = self.client.get(reverse('lables'))
        self.assertEqual(resp.status_code, 302)
       # self.assertIn('login', resp.url)

        '''Authentication'''
        self.client.force_login(user)

        resp = self.client.get(reverse('lables'))
        self.assertEqualt(resp.status_code, 200)
        self.assertTrue(len(resp.context['lables']) == 2)

    #CREATE
    def test_CreateLable(self):
        user = User.objects.get(id=1)

        '''Not authentication'''
        resp = self.client.get(reverse('create_lable'))
        self.assertEqual(resp.status_code, 302)
      #  self.assertIn('login', resp.url)

       '''Authentication'''
        self.client.force_login(user)
        resp = self.client.get(reverse('create_lable'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='lables/create.html')

        resp = self.client.post(
                reverse('create_lable'),
                {'name': 'Control'})
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('lables'))


    #UPDATE
    def test_CreateStatus(self):
        user = User.objects.get(id=1)
        lable = Lable.objects.get(id=1)

        '''Not authentication'''
        resp = self.client.get(
            reverse('update_lable', kwargs={'pk': status.id})
        )
        self.assertEqual(resp.status_code, 302)
       # self.assertIn('login', resp.url)

        '''Authentication'''
        self.client.force_login(user)

        resp = self.client.get(
            reverse('update_lable', kwargs={'pk': status.id})
        )
        self.assertEqual(resp.status_code, 200)


        resp = self.client.post(
            reverse('update_lable', kwargs={'pk': status.id}),
            {'name': 'New lable'}
        )
        self.assertEqual(resp.status_code, 302)
        status.refresh_from_db()
        self.assertEqual(status.name, 'New lable')


    #DELETE
    def test_DeleteStatus(self):
        user = User.objects.get(id=1)
        lable = Lable.objects.get(id=2)

        '''Not authentication'''
        resp = self.client.get(
            reverse('delete_lable', kwargs={'pk': lable.id})
        )
        self.assertEqual(resp.status_code, 302)
       # self.assertIn('login', resp.url)

        '''Authentication'''
        self.client.force_login(user)

        resp = self.client.get(
            reverse('delete_lable', kwargs={'pk': lable.id})
        )
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post(
                reverse('delete_lable', kwargs={'pk': lable.id})
                )
        self.assertRedirects(resp, reverse('lables'))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Lable.objects.count(), 1)
