import decimal

from django.db import models

from course.models import Program
from student.models import Participant


class Enroll(models.Model):
    participant_id = models.ForeignKey(Participant, on_delete=models.CASCADE)
    program_id = models.ForeignKey(Program, on_delete=models.CASCADE)
    total_fee = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s/%s $%s" % (self.participant_id.name, self.program_id.name, self.program_id.level, self.total_fee)

    @property
    def paid(self):
        return sum([p.amount for p in self.payment_set.all()])

    def balance(self):
        return decimal.Decimal(self.total_fee) - self.paid

    def last_payment(self):
        return self.payment_set.order_by('-date_created').first()