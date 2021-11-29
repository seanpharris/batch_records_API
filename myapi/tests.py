import json

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse, resolve
from myapi.views import BatchJobsViewSet
from myapi.models import BatchJob
import random


class GetBatchJobTest(APITestCase):

    def test_get_all_batch_jobs(self):
        path = reverse('batch_jobs-list')
        assert resolve(path).view_name == 'batch_jobs-list'

    def test_get_batch_job_by_batch_number(self):
        num_list = [range(len(BatchJob.objects.all()))]
        num = random.choice(num_list)
        path = reverse('batch_jobs-detail', kwargs={'pk': "filter[batch_number]=" + str(num)})
        assert resolve(path).view_name == 'batch_jobs-detail'

    def test_get_batch_job_by_max_nodes(self):
        num_list = [range(len(BatchJob.objects.all()))]
        num = random.choice(num_list)
        path = reverse('batch_jobs-detail', kwargs={'pk': "filter[max_nodes]=" + str(num)})
        assert resolve(path).view_name == 'batch_jobs-detail'

    def test_get_batch_job_by_min_nodes(self):
        num_list = [range(len(BatchJob.objects.all()))]
        num = random.choice(num_list)
        path = reverse('batch_jobs-detail', kwargs={'pk': "filter[min_nodes]=" + str(num)})
        assert resolve(path).view_name == 'batch_jobs-detail'

    def test_get_batch_job_by_submitted_after(self):
        path = reverse('batch_jobs-detail', kwargs={'pk': "filter[submitted_after]=2018-03-02T15:14:25+00:00"})
        assert resolve(path).view_name == 'batch_jobs-detail'

    def test_get_batch_job_by_submitted_before(self):
        path = reverse('batch_jobs-detail', kwargs={'pk': "filter[submitted_before]=2018-03-02T15:14:25+00:00"})
        assert resolve(path).view_name == 'batch_jobs-detail'

    def test_get_batch_job_by_combo_filter(self):
        path = reverse('batch_jobs-detail',
                       kwargs={'pk': "filter[submitted_after]='2018-02-28T15:00:00+00:00'&"
                                     "filter[submitted_before]='2018-03-01T15:00:00+00:00'&"
                                     "filter[min_nodes]=2&filter[max_nodes]=20"})
        assert resolve(path).view_name == 'batch_jobs-detail'

