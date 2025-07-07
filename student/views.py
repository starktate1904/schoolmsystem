from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms


def index(request):
    participants = models.Participant.objects.all()
    return render(request, 'participant/index.html', {'participants': participants})

def participant_detail(request, participant_id):
    participant = get_object_or_404(models.Participant, id=participant_id)
    return render(request, 'participant/index.html', {'participant': participant})


def create(request):
    form = forms.CreateparticipantForm()
    return render(request, 'participant/create.html', {'form': form})


def store(request):
    if request.method == 'POST':
        form = forms.CreateparticipantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Participant created successfully')
            return redirect('participant.index')
        else:
            return render(request, 'participant/create.html', {'form': form})
    else:
        return redirect('participant.create')


def edit(request, sid):
    try:
        participant = models.Participant.objects.get(id=sid)
        form = forms.CreateparticipantForm(instance=participant)
        return render(request, 'participant/edit.html', {'form': form})
    except models.Participant.DoesNotExist:
        return redirect('participant.index')


def update(request, sid):
    if request.method == 'POST':
        try:
            participant = models.Participant.objects.get(id=sid)
            form = forms.CreateparticipantForm(request.POST, instance=participant)
            if form.is_valid():
                form.save()
                messages.success(request, 'participant updated successfully')
                return redirect('participant.index')
            else:
                return render(request, 'participant/edit.html', {'form': form})
        except models.Participant.DoesNotExist:
            return redirect('participant.index')
    else:
        return redirect('participant.index')


def delete(request, sid):
    if request.method == 'POST':
        try:
            participant = models.Participant.objects.get(id=sid)
            participant.delete()
            messages.success(request, 'participant deleted successfully')
            return redirect('participant.index')
        except models.Participant.DoesNotExist:
            return redirect('participant.index')
    else:
        return redirect('participant.index')
