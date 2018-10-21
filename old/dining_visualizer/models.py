from django.db import models

class Transaction(models.Model):
    date_posted = models.DateTimeField()
    change = models.DecimalField(max_digits=6, decimal_places=2)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.TextField()
