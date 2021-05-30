from django.test import SimpleTestCase
from app.views import *
from app.models import *
from django.db import models
import datetime

class ViewTestCase(SimpleTestCase):
    
    def testPostDate(self):
        p = Post(date=datetime.datetime.now(), photo=random_picture())
        d1 = p.date
        d2 = datetime.datetime.now()
        self.assertTrue(abs(d2 - d1) < datetime.timedelta(seconds=5))
        assert type(p.photo) is str

    def testPostPhoto(self):
        p = Post(date=datetime.datetime.now(), photo=random_picture())
        assert type(p.photo) is str

    def testModels(self):
        pass
