from django.db import models
from volunteer_reg.models import VolunteerReg
# Create your models here.
class VolunteerActivites(models.Model):
    activity_id = models.AutoField(primary_key=True)
    #volunteer_id = models.IntegerField(blank=True, null=True)
    volunteer=models.ForeignKey(VolunteerReg,on_delete=models.CASCADE)
    activity = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'volunteer_activites'

