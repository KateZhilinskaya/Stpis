from django.test import TestCase, Client
from django.contrib.auth.models import User
from accounts.models import Profile, Company
from django.urls import reverse


class StaffTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='tester')
        self.user.set_password('1')
        self.user.save()

        self.client = Client()
        self.client.login(username="tester", password="1")

        self.staff_url = reverse('staff')

    def test_staff_page_for_owner(self):
        company = Company.objects.create(owner=self.user, name="test company")
        Profile.objects.create(user=self.user, status=2, company=company)

        response = self.client.get(self.staff_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'control/staff.html')

    def test_staff_page_not_for_owner(self):
        owner = User.objects.create(username='owner')
        owner.set_password('1')
        owner.save()

        company = Company.objects.create(owner=owner, name="test company")
        Profile.objects.create(user=self.user, status=1, company=company)

        response = self.client.get(self.staff_url)
        self.assertEqual(response.content, b'No permission')
        self.assertEquals(response.status_code, 200)


class EmployeeTest(TestCase):

    def setUp(self):
        self.owner = User.objects.create(username='tester')
        self.owner.set_password('1')
        self.owner.save()

        company = Company.objects.create(owner=self.owner, name="test company")
        Profile.objects.create(user=self.owner, status=2, company=company)

        self.client = Client()
        self.client.login(username="tester", password="1")

        self.employee = User.objects.create(username='employee')
        self.employee.set_password('1')
        self.employee.save()
        Profile.objects.create(user=self.employee, status=0, company=company)

        self.employee_url = reverse('employee', kwargs={"uid": self.employee.id})

    def test_employee_page_GET(self):
        response = self.client.get(self.employee_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "control/employee.html")

    def test_employee_page_POST(self):
        response = self.client.post(self.employee_url, {
            "email": "employee@emp.ru",
            "first_name": "Emp",
            "last_name": "loyee",
            "patronymic": "",
            "status": 1
        })

        employee = User.objects.get(id=self.employee.id)

        self.assertEquals(response.status_code, 302)
        self.assertEqual(employee.email, "employee@emp.ru")
        self.assertEqual(employee.first_name, "Emp")

