from django.test import TestCase
from app.views import *
from app.models import *
from django.db import models
import datetime

class ViewTestCase(TestCase):
    
    def testPost(self):
        p = Post(date=datetime.datetime.now(), photo=random_picture())
        d1 = p.date
        d2 = datetime.datetime.now()
        self.assertTrue(abs(d1 - d2) < datetime.timedelta(seconds=1))
        assert type(p.photo) is str
