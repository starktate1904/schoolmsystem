from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', login_required(views.index), name='participant.index'),
    path('create/', login_required(views.create), name="participant.create"),
    path('store/', login_required(views.store), name="participant.store"),
    path('edit/<int:sid>/', login_required(views.edit), name="participant.edit"),
    path('update/<int:sid>/', login_required(views.update), name="participant.update"),
    path('delete/<int:sid>/', login_required(views.delete), name="participant.delete"),
]
