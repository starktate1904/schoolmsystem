from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from enrollment.models import Enroll


class Payment(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('swipe_usd', 'Swipe USD'),
        ('swipe_usd', 'Swipe ZWG'),
        ('ecocash', 'Ecocash'),
        ('bank_transfer', 'Bank Transfer'),
    ]

    enroll_id = models.ForeignKey(Enroll, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    paid_with = models.CharField(max_length=255, choices=PAYMENT_METHODS, default='cash')
    
    
    def __str__(self):
        return f"Payment of {self.amount} by {self.paid_with} on {self.date_created}"


class Action(models.Model):
    sender = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(ContentType, blank=True, null=True,
                                  related_name='target_obj', on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.pk
