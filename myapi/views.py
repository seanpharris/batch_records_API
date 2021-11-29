from rest_framework import viewsets
from rest_framework.response import Response

from myapi.models import BatchJob
from myapi.serializers import BatchJobSerializer


class BatchJobsViewSet(viewsets.ModelViewSet):
    serializer_class = BatchJobSerializer

    def get_queryset(self):
        jobs = BatchJob.objects.all()
        return jobs

    def retrieve(self, response, *args, **kwargs):
        params = kwargs
        params_list = params['pk'].split('&')
        jobs = BatchJob.objects.all()
        for i in range(len(params_list)):
            if params_list[i].__contains__('filter[submitted_after]='):
                jobs = jobs.filter(
                    submitted_at__gte=params_list[i].replace("filter[submitted_after]=", ""))
            elif params_list[i].__contains__('filter[submitted_before]='):
                jobs = jobs.filter(
                    submitted_at__lte=(params_list[i].replace("filter[submitted_before]=", "")))
            elif params_list[i].__contains__('filter[max_nodes]='):
                jobs = jobs.filter(nodes_used__lte=params_list[i].replace("filter[max_nodes]=", ""))
            elif params_list[i].__contains__('filter[min_nodes]='):
                jobs = jobs.filter(nodes_used__gte=params_list[i].replace("filter[min_nodes]=", ""))
            elif params_list[i].__contains__('filter[batch_number]='):
                jobs = jobs.filter(batch_number=params_list[i].replace("filter[batch_number]=", ""))
        serializer = BatchJobSerializer(jobs, many=True)
        return Response(serializer.data)






