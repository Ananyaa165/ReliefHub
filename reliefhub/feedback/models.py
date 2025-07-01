from django.db import models
from public_reg.models import PublicReg
# Create your models here.
class Feedback(models.Model):
    feedback_id = models.IntegerField(primary_key=True)
    feedback = models.CharField(max_length=100, blank=True, null=True)
    #public_id = models.IntegerField(blank=True, null=True)
    public=models.ForeignKey(PublicReg, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'feedback'
