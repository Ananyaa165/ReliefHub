from django.db import models

# Create your models here.
class PublicReg(models.Model):
    public_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    phone_no = models.CharField(max_length=45)
    address = models.CharField(max_length=200)
    user_name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'public_reg'
