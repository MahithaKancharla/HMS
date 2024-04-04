from django.test import TestCase
from .models import StudentInfo,WardenInfo,Hostel,Room
from django.contrib.auth.models import User

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
        hostel = Hostel.objects.create(hostel_type='girls hostel',hostel_name='ABC hostel',capacity=500,filled_seats_count=100)
        
        self.assertEqual(str(hostel),hostel.hostel_name)

class IndexPageTest(TestCase):
    def test_index_page_returns_correct_response(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response,'index.html')
        self.assertEqual(response.status_code,200)

class ListPageTest(TestCase):
    def test_list_page_has_students(self):
        student1 = StudentInfo.objects.create(roll_no='211113',name='Mahitha',department='cse',joining_year='2021',room_no='8',blood_group='O+ve',contact_number='9705697956',address='Andhra pradesh',gender='Female',email='211113@iiitt.ac.in',father_name='Nagesh',father_contact_number='9999999234',mother_name='Vasudha',mother_contact_number='6587738573',guardian_name='priya',guardian_contact_number='5783875839')
        student2 = StudentInfo.objects.create(roll_no='211114',name='Snigdha',department='cse',joining_year='2021',room_no='8',blood_group='AB+ve',contact_number='8748345843',address='Vijayawada',gender='Female',email='211114@iiitt.ac.in',father_name='Satish',father_contact_number='4625472372',mother_name='Seetha',mother_contact_number='6482684328',guardian_name='Reetha',guardian_contact_number='8728579102')

        response = self.client.get('/list',follow=True)

        self.assertContains(response,student1.roll_no)

class RegisterTestCase(TestCase):
    def test_password_validation(self):
        username = '211114@iiitt.ac.in'
        password = '1234bcda@'

        self.user = User.objects.create_user(
            username=username, password=password)
        self.assertTrue(
            self.is_valid_password(
                password), f"Password '{password}' should be valid"
        )

    def is_valid_password(self, password):
        return len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password) and any(char in '!@#$%^&*()-_=+[{]}|;:,<.>/?' for char in password)
    
class ProfilePageTest(TestCase):
    def test_profile_page_has_students(self):
        student = StudentInfo.objects.create(roll_no='211113',name='Mahitha',department='cse',joining_year='2021',room_no='8',blood_group='O+ve',contact_number='9705697956',address='Andhra pradesh',gender='Female',email='211113@iiitt.ac.in',father_name='Nagesh',father_contact_number='9999999234',mother_name='Vasudha',mother_contact_number='6587738573',guardian_name='priya',guardian_contact_number='5783875839')
        
        response = self.client.get(f'/{student.roll_no}/')

        self.assertTemplateUsed(response,'profile.html')
        self.assertEqual(response.status_code,200)