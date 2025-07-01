from django.db import models
from camp_details.models import CampDetails
# Create your models here.
class VolunteerReg(models.Model):
    volunteer_id = models.AutoField(primary_key=True)
    volunteer_name = models.CharField(max_length=45)
    volunteer_ph = models.CharField(max_length=45)
    email_id = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    availability = models.CharField(max_length=45)
    designation = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    user_name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    document = models.CharField(max_length=500)
    # camp_id = models.IntegerField()
    camp=models.ForeignKey(CampDetails,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'volunteer_reg'
