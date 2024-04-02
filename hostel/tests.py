from django.test import TestCase
from .models import StudentInfo

class ModelAttributeTest(TestCase):
    def test_model_attributes_exist(self):
        # Get all fields from the model
        model_fields = [field.name for field in StudentInfo._meta.get_fields()]

        # Check if all expected attributes exist
        expected_attributes = ['department', 'gender','blood_group','joining_year','room_no','contact_number','address','email','father_name','mother_name']  # Add more attributes as needed
        for attribute in expected_attributes:
            self.assertIn(attribute, model_fields)