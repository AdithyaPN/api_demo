from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
class TestSample(TestCase):

    def setup(self):
        self.client = APIClient

    # def test_index(self): # method name should start with test
    #     url = reverse('index') #url in name
    #     res = self.client.get(url) # calling the url and save the response in to a variable
    #     print(res.data)
    #     # the test will pass only if the status code equals to 200. Status code 200 represent the ok or success.
    #     # self.assertEquals(res.status_code, 200)
    #     # the test will pass only if the response is equal to 'Congratulations, you have created an API'
    #     self.assertEquals(res.data, 'Congratulations, you have created an API')

    def test_float(self):
        url = reverse('float')
        res = self.client.get(url)
        if type(res.data) != float:
           raise Exception('Error')