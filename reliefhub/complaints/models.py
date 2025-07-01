from django.db import models
from volunteer_reg.models import VolunteerReg
# Create your models here.
class Complaints(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    # volunteer_id = models.IntegerField()
    volunteer = models.ForeignKey(VolunteerReg, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'complaints'


