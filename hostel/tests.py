from django.test import TestCase
from .models import StudentInfo,WardenInfo,Hostel,Room

class ModelAttributeTest(TestCase):
    def test_model_attributes_exist(self):
        model_fields = [field.name for field in StudentInfo._meta.get_fields()]

        expected_attributes = ['department', 'gender','blood_group','joining_year','room_no','contact_number','address','email','father_name','mother_name']  # Add more attributes as needed
        for attribute in expected_attributes:
            self.assertIn(attribute, model_fields)

class WardenInfoModelTest(TestCase):
    def test_wardenn_info_exists(self):
        wardens = WardenInfo.objects.count()

        self.assertEqual(wardens,0)

class HostelModelTest(TestCase):
    def test_model_has_string_representation(self):
        hostel = Hostel.objects.create(hostel_type='girls hostel',hostel_name='ABC hostel',capacity=500)
        
        self.assertEqual(str(hostel),hostel.hostel_name)