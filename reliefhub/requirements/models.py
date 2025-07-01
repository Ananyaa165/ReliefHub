from django.db import models
from volunteer_reg.models import VolunteerReg
from camp_details.models import CampDetails
from delivery.models import Delivery

# Create your models here.
class Requirements(models.Model):
    requirement_id = models.AutoField(primary_key=True)
    requirements = models.CharField(max_length=100)
    # volunteer_id = models.IntegerField()
    volunteer = models.ForeignKey(VolunteerReg, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    # camp_id = models.IntegerField()
    camp = models.ForeignKey(CampDetails, on_delete=models.CASCADE)
    # delivery_id = models.IntegerField()
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'requirements'

