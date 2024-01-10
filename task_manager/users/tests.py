from django.test import TestCase
from task_manager.users.models import User
from django.urls import reverse


class CRUD_Users_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            first_name='Rodion',
            last_name='Raskol`nikov',
            username='Dostoevsky',
            password='1866'
        )
        User.objects.create(
            first_name='Pavel',
            last_name='Chichikov',
            username='Gogol`',
            password='1842'
        )

    # CREATE
    def test_CreateUser(self):
        resp = self.client.get(reverse('create_user'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='users/create.html')

        # Passwords match
        resp = self.client.post(
            reverse('create_user'),
            {
                'first_name': 'Pavel',
                'last_name': 'Afanas`evich',
                'username': 'Griboedov',
                'password1': '1825',
                'password2': '1825'
            }
        )
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        user = User.objects.last()
        self.assertEqual(user.username, 'Griboedov')

        # Password mismatch
        resp = self.client.post(
            reverse('create_user'),
            {
                'first_name': 'Bazarov',
                'last_name': 'Eugene',
                'username': 'Turgenev',
                'password1': '1862',
                'password2': '1854'
            }
        )
        self.assertEqual(resp.status_code, 200)

    # READ
    def test_ListUsers(self):
        resp = self.client.get(reverse('users'))
        self.assertTrue(len(resp.context['users']) == 2)

    # UPDATE
    def test_UpdateUser(self):
        user = User.objects.get(id=1)

        '''Not authentication'''
        resp = self.client.get(
            reverse('update_user', kwargs={'pk': user.id})
        )
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        '''Authentication'''
        self.client.force_login(user)

        resp = self.client.get(
            reverse(
                'update_user',
                kwargs={'pk': user.id}
            )
        )
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post(
            reverse(
                'update_user',
                kwargs={'pk': user.id}),
            {
                'first_name': 'Boris',
                'last_name': 'Godunov',
                'username': 'Pushkin',
                'password1': '1831',
                'password2': '1831',
            }
        )

        self.assertEqual(resp.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'Boris')

    # DELETE
    def test_DeleteUser(self):
        user = User.objects.get(username="Gogol`")

        '''Not authentification'''
        resp = self.client.get(
            reverse('delete_user', kwargs={'pk': user.id})
        )

        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        '''Authentification'''
        self.client.force_login(user)
        resp = self.client.get(
            reverse(
                'delete_user',
                kwargs={'pk': user.id}
            )
        )
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post(
            reverse(
                'delete_user',
                kwargs={'pk': user.id}
            )
        )

        self.assertRedirects(resp, reverse('users'))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(User.objects.count(), 1)
