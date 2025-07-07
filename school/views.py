from datetime import datetime

from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.shortcuts import render

from enrollment.models import Enroll
from payment.models import Payment, Action
from student.models import Participant
from datetime import datetime


def index(request):
    user = request.user
    payment = Payment.objects.all().order_by('-date_created')[:10]
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    current_date = now.strftime("%B %d, %Y")

    # Determine the greeting based on the current time
    if now.hour < 12:
        greeting = "Good Morning"
    elif 12 <= now.hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    earnings = {}
    for month in range(1, 13):
        earnings[month] = Payment.objects.filter(date_created__month=month).aggregate(Sum('amount'))['amount__sum'] or 0

    monthly = earnings[datetime.now().month]
    annual = sum(earnings.values())
    enroll = Enroll.objects.all().count()
    participants = Participant.objects.all().count()

    return render(request, 'index.html', {
        'payment': payment,
        'earnings': earnings,
        'monthly': monthly,
        'annual': annual,
        'enroll': enroll,
        'participants': participants,
        'user': user,
        'greeting': greeting,
        'current_date': current_date,
        'current_time': current_time
    })


def activity(request):
    payment_activity = Action.objects.all().order_by('-created')
    return render(request, 'activity/index.html', {'payment_activity': payment_activity})
