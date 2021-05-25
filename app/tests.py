from django.test import TestCase, Client
from app.models import UUIDModel
from datetime import datetime
import uuid
from django.urls import reverse
from . import views

# Create your tests here.

# models
class UuidModelTest(TestCase):
    def setUp(self):

        ''' setup uuid object to run tests '''

        self.t_uuid = uuid.uuid4()
        self.t_timestamp = datetime.now()
        UUIDModel.objects.create(timestamp=self.t_timestamp, UUID=self.t_uuid)

    def test_UUIDModel_model(self):

        ''' test UUIDModel "UUID" field '''

        t_obj = UUIDModel.objects.get(UUID=self.t_uuid)
        self.assertEqual(t_obj.UUID, self.t_uuid)

# views
class HomeTestCase(TestCase):

    def setup(self):

        ''' setup client to run tests '''

        self.client = Client

    def test_home_view(self):

        ''' test response code from "home" view '''

        url = reverse('index')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
