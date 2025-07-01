from django.db import models
from volunteer_reg.models import VolunteerReg
# from camp_details.models import CampDetails
# Create your models here.
class Scheduling(models.Model):
    task_id = models.AutoField(primary_key=True)
    # volunteer_id = models.IntegerField(blank=True, null=True)
    volunteer = models.ForeignKey(VolunteerReg, on_delete=models.CASCADE)
    scheduled_task = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    # camp_id = models.IntegerField()
    # camp_details=models.ForeignKey(CampDetails,on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'scheduling'


