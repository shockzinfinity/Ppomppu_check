from django.test import TestCase
from .models import CrawlingData as CD

class ModelTestCase(TestCase):

    def setUp(self):
        self.test_title = "Test title"
        self.test_category = "Test Category"
        self.test_date = "Test Date"
        self.test_link = "Test Link"
        self.test_instance = CD(title=self.test_title,
                                category=self.test_category,
                                write_date=self.test_date,
                                detail_link=self.test_link)

    def test_model_can_create_a_crawling_data(self):
        old_count = CD.objects.count()
        self.test_instance.save()
        new_count = CD.objects.count()
        self.assertNotEqual(old_count, new_count)

from .views import run_crawling

class CrawlingTestCase(TestCase):
    
    def setUp(self):
        pass

    def test_crawling_save_db(self):
        old_count = CD.objects.count()
        url = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=1'
        run_crawling(url)
        new_count = CD.objects.count()
        self.assertNotEqual(old_count, new_count)
