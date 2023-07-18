from django.db import models
from datetime import datetime, timezone






class AddReminder(models.Model):
    Caption=models.CharField(max_length=100)
    reminder_for=models.CharField(max_length=100)
    date=models.DateField(null=True)
    time=models.TimeField()
    options=(
        ('Health','Health'),
        ('Workout','Workout'),
        ('Study','Study'),
        ('Company','Company'),
        ('task','task'),
        ('Events','Events')
    )
    category=models.CharField(max_length=100,choices=options,default='Health')

    def __str__(self):
        return self.Caption
    





