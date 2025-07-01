from django.db import models
from camp_details.models import CampDetails
from volunteer_reg.models import VolunteerReg
from public_reg.models import PublicReg
# Create your models here.
class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    #camp_id = models.IntegerField(blank=True, null=True)
    camp= models.ForeignKey(CampDetails, on_delete=models.CASCADE)
    #volunteer_id = models.IntegerField(blank=True, null=True)
    volunteer=models.ForeignKey(VolunteerReg, on_delete=models.CASCADE)
    #public_id = models.IntegerField(blank=True, null=True)
    public=models.ForeignKey(PublicReg, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=45)
    item = models.CharField(max_length=100)
    quantity_c = models.CharField(max_length=45)
    public_location = models.CharField(max_length=200)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'delivery'
