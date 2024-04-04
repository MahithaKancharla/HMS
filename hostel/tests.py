from django.test import TestCase, Client
from .models import StudentInfo, WardenInfo, Hostel, Room
from django.contrib.auth.models import User


class ModelAttributeTest(TestCase):
    def test_model_attributes_exist(self):
        model_fields = [field.name for field in StudentInfo._meta.get_fields()]

        expected_attributes = ['department', 'gender', 'blood_group', 'joining_year', 'room_no',
                               'contact_number', 'address', 'email', 'father_name', 'mother_name']  # Add more attributes as needed
        for attribute in expected_attributes:
            self.assertIn(attribute, model_fields)


class WardenInfoModelTest(TestCase):
    def test_wardenn_info_exists(self):
        wardens = WardenInfo.objects.count()

        self.assertEqual(wardens, 0)


class HostelModelTest(TestCase):
    def test_model_has_string_representation(self):
        hostel = Hostel.objects.create(
            hostel_type='girls hostel', hostel_name='ABC hostel', capacity=500, filled_seats_count=100)

        self.assertEqual(str(hostel), hostel.hostel_name)


class RegisterTestCase(TestCase):
    def test_password_validation(self):
        username = '211114@iiitt.ac.in'
        password = '1234abcd'

        self.user = User.objects.create_user(
            username=username, password=password)
        self.assertTrue(
            self.is_valid_password(
                password), f"Password '{password}' should be valid"
        )

    def is_valid_password(self, password):
        return len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password) and any(char in '!@#$%^&*()-_=+[{]}|;:,<.>/?' for char in password)
