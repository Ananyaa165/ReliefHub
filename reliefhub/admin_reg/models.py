from django.db import models

# Create your models here.
class AdminReg(models.Model):
    admin_id = models.AutoField(db_column='Admin_id', primary_key=True)  # Field name made lowercase.
    admin_name = models.CharField(db_column='Admin_name', max_length=45)  # Field name made lowercase.
    designation = models.CharField(max_length=45)
    user_name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    contact_no = models.CharField(max_length=45)
    email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'admin_reg'
