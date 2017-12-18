from django.db import models

# Create your models here.
class Event(models.Model):
    #event, Holiday, Exam
    #description
    #heading
    #datetime
    CHOICES = (
        ('EV', 'Event'),
        ('HD', 'Holiday'),
        ('EX', 'Exam')
    )
    type = models.CharField(blank=True, null=True, choices=CHOICES, max_length=10, default='EV')
    #description = models.CharField(max_length=50, null=True, blank=True, default='')
    title = models.CharField(max_length=100, default='Title')
    start = models.DateField()
    end = models.DateField()
    #all_day = models.BooleanField(default=False)

    def __str__(self):
        return self.type + " =>  " + self.heading
