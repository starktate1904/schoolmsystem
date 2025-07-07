from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

from course.models import Program
from enrollment.forms import CreateEnrollForm
from enrollment.models import Enroll


def index(request):
    enrolls = Enroll.objects.all()
    return render(request, 'enrollment/index.html', {'enrolls': enrolls})


def create(request):
    form = CreateEnrollForm()
    return render(request, 'enrollment/create.html', {'form': form})


def get_program_total_amount(request):
    if request.method == 'POST':
        program_id = request.POST.get('program_id')
        print(f"Received program_id: {program_id}")  # Log the program_id
        if not program_id:
            return JsonResponse({'error': 'Program ID is required'}, status=400)
        
        try:
            program = Program.objects.get(id=program_id)
            return JsonResponse({'data': program.total_amount})
        except Program.DoesNotExist:
            return JsonResponse({'error': 'Program not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)


# views.py
def store(request):
    if request.method == 'POST':
        form = CreateEnrollForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Participant enrolled successfully')
            return redirect('enroll.index')
        else:
            return render(request, 'enrollment/create.html', {'form': form})
    else:
        return redirect('enroll.index')


def edit(request, eid):
    try:
        enroll = Enroll.objects.get(id=eid)
        form = CreateEnrollForm(instance=enroll)
        return render(request, 'enrollment/edit.html', {'form': form, 'enroll': enroll})
    except Enroll.DoesNotExist:
        return redirect('enroll.index')


def update(request, eid):
    try:
        if request.method == 'POST':
            enroll = Enroll.objects.get(id=eid)
            form = CreateEnrollForm(request.POST, instance=enroll)
            if form.is_valid():
                form.save()
                messages.success(request, 'Enrolled info updated successfully')
                return redirect('enroll.index')
            else:
                return render(request, 'enrollment/edit.html', {'form': form, 'enroll': enroll})
        else:
            return redirect('enroll.index')
    except Enroll.DoesNotExist:
        return redirect('enroll.index')


def delete(request, eid):
    if request.method == 'POST':
        try:
            enroll = Enroll.objects.get(id=eid)
            enroll.delete()
            return redirect('enroll.index')
        except Enroll.DoesNotExist:
            messages.error(request, 'Enrolled info not found')
            return redirect('enroll.index')
    else:
        messages.error(request, 'Invalid request')
        return redirect('enroll.index')
