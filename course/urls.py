from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', login_required(views.index), name='program.index'),
    path('create/', login_required(views.create), name='program.create'),
    path('store/', login_required(views.store), name="program.store"),
    path('edit/<int:cid>/', login_required(views.edit), name="program.edit"),
    path('update/<int:cid>/', login_required(views.update), name="program.update"),
    path('delete/<int:cid>/', login_required(views.delete), name="program.delete"),
]
