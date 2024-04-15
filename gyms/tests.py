from django.test import TestCase
from .models import Gym
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

# Create your tests here.
class GymCreationTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='TestUser', password='test123')
        Gym.objects.create(name='Gym1', addr='Bangalore', staff=User.objects.get(username='TestUser'))
    
    def test(self):
        gym = Gym.objects.get(name='Gym1')
        self.assertEqual(gym.name, 'Gym1')
        self.assertEqual(gym.addr, 'Bangalore')
        self.assertEqual(gym.staff.username, 'TestUser')

class GymWithDuplicateNameTestCase(TestCase):
    def setUp(self):
        self.user0 = User.objects.create_user(username='TestUser0', password='test123')
        self.user1 = User.objects.create_user(username='TestUser1', password='test123')
        Gym.objects.create(name='Gym0', addr='Bangalore', staff=self.user0)

    def test(self):
        with self.assertRaises(IntegrityError) as cm:
            Gym.objects.create(name='Gym0', addr='Delhi', staff=self.user1)
