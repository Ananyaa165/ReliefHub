from django.db import models

# Create your models here.
from scheduling.models import Scheduling


class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=300)
    # task_id = models.IntegerField()
    task=models.ForeignKey(Scheduling, on_delete=models.CASCADE)
    public_id = models.IntegerField()
    sendertype = models.CharField(max_length=45)
    rectype = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'chat'



