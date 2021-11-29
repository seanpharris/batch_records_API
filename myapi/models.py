from django.db import models


class BatchJob(models.Model):
    batch_number = models.CharField(max_length=5, primary_key=True)
    submitted_at = models.DateTimeField(max_length=30)
    nodes_used = models.CharField(max_length=6)

    def __str__(self):
        return self.batch_number
