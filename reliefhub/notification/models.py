from django.db import models
from admin_reg.models import AdminReg

# Create your models here.
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    notification = models.CharField(max_length=45)
   # admin_id = models.IntegerField(blank=True, null=True)
    admin=models.ForeignKey(AdminReg,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'notification'
