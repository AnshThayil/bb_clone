from django.test import TestCase
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from .models import Profile
from gyms.models import Gym
from walls.models import Wall
from boulders.models import Boulder, Sender

# Create your tests here.
class UsersWithDuplicateUsernamesTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser')

    def test(self):
        with self.assertRaises(IntegrityError) as cm:
            User.objects.create_user(username='testuser')

class ProfileCreatedWithUserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser')
    
    def test(self):
        user = User.objects.get(username='testuser')
        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            self.fail()

class ProfilePointsOperationsTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser')
        Gym.objects.create(name='test_gym', addr='test', staff=User.objects.get(username='testuser'))
        Wall.objects.create(wall_name='test_wall', gym=Gym.objects.get(name='test_gym'), img_url='test.com', img_height=100, img_width=100)
        Boulder.objects.create(boulder_name='test_boulder', grade=5, wall=Wall.objects.get(wall_name='test_wall'), setter=User.objects.get(username='testuser'))
    
    def test(self):
        user = User.objects.get(username='testuser')
        sender = Sender.objects.create(sender=user, boulder=Boulder.objects.get(boulder_name='test_boulder'), flash=False)
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.points, 5)
        sender.delete()
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.points, 0)
        sender = Sender.objects.create(sender=user, boulder=Boulder.objects.get(boulder_name='test_boulder'), flash=True)
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.points, 6)
        sender.delete()
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.points, 0)
        