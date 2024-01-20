from django.db import models
from django.utils import timezone
from django.db.models import Sum

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)


    class Meta:
        abstract = True

# Create your models here.
class Institutions(BaseModel):
    name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    income = models.IntegerField(blank=True,null=True)
    salary_payment = models.IntegerField(blank=True,null=True)
    vehicle_procurement = models.IntegerField(blank=True,null=True)
    construction = models.IntegerField(blank=True,null=True)
    total = models.IntegerField(blank=True,null=True)

    def calculate_total(self):
        # Filter entries for the same institution name and exclude instances where 'income' is null
        entries = Institutions.objects.filter(institution__iexact=self.institution).exclude(income__isnull=True)

        # Calculate the sum of the 'total' field
        total = entries.aggregate(Sum('total'))['total__sum']

        # Return the total
        return total
