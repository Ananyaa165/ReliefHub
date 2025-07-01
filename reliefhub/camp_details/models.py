from django.db import models

# Create your models here.
class CampDetails(models.Model):
    camp_id = models.AutoField(primary_key=True)
    camp_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    no_of_refugees = models.IntegerField(db_column='no.of_refugees')  # Field renamed to remove unsuitable characters.
    no_of_volunteers = models.IntegerField(db_column='no.of_volunteers')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'camp_details'
