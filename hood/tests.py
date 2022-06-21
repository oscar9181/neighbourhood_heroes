from django.test import TestCase
from .models import Business

# Create your tests here.


class BusinessTestClass(TestCase):
  def setUp(self):
      self.new_business = Business(biz_name ='Zaimet',biz_email = 'zaimet@food.com', biz_description='Eat good Live good', biz_digits='0700112233')

  def test_instance(self):
      self.assertTrue(isinstance(self.new_business, Business))

  def test_update_business(self):
      self.new_business.save_business()
      business_id = self.new_business.id
      Business.update_business(id, "ZaimetKiller")
      self.assertEqual(self.business.business, "ZaimetKiller")

  def test_delete_business(self):
      self.business.save_business()
      self.business.delete_business()
      business = Business.objects.all()
      self.assertTrue(len(business) == 0)