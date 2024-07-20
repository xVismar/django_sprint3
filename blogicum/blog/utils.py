from django.db import models
from django.utils import timezone


class QuerySet(models.query.QuerySet):
    def check_time(self):
        return self.filter(pub_date__lte=timezone.now())
