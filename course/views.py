from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect

from course import models
from course.forms import CreateprogramForm, CreateFeeForm


def index(request):
    programs = models.Program.objects.all()
    return render(request, 'program/index.html', {'programs': programs})


def create(request):
    program = CreateprogramForm()
    fee = CreateFeeForm()
    return render(request, 'program/create.html', {'program': program, 'fee': fee})


def store(request):
    if request.method == 'POST':
        program_valid = CreateprogramForm(request.POST)
        fee_valid = CreateFeeForm(request.POST)

        if program_valid.is_valid() and fee_valid.is_valid():
            fee_desc = request.POST.getlist('fee_desc[]')
            fee_amount = request.POST.getlist('amount[]')

            if len(fee_desc) > 0 and len(fee_amount) > 0:
                with transaction.atomic():
                    program = program_valid.save()
                    for i in range(len(fee_desc)):
                        models.Fee.objects.create(program=program, fee_desc=fee_desc[i], amount=fee_amount[i])
                    messages.success(request, 'program created successfully')
                    return redirect('program.index')
            else:
                messages.warning(request, 'Please add atleast one fee')
                return redirect('program.create')

        else:
            return render(request, 'program/create.html', {'program': program_valid, 'fee': fee_valid})
    else:
        return redirect('program.create')


def edit(request, cid):
    try:
        program = models.Program.objects.get(id=cid)
        fee = models.Fee.objects.filter(program=program)
        program_form = CreateprogramForm(instance=program)
        fee_form = CreateFeeForm(instance=fee.last())
        return render(request, 'program/edit.html', {'program': program_form, 'fee': fee_form, 'fees': fee})
    except models.Program.DoesNotExist:
        return redirect('program.index')


def update(request, cid):
    if request.method == 'POST':
        try:
            program = models.Program.objects.get(id=cid)
            fee = models.Fee.objects.filter(program=program)
            program_form = CreateprogramForm(request.POST, instance=program)
            fee_form = CreateFeeForm(request.POST, instance=fee.last())
            if program_form.is_valid() and fee_form.is_valid():
                fee_desc = request.POST.getlist('fee_desc[]')
                fee_amount = request.POST.getlist('amount[]')

                if len(fee_desc) > 0 and len(fee_amount) > 0:
                    with transaction.atomic():
                        fee.delete()
                        program_form.save()
                        for i in range(len(fee_desc)):
                            models.Fee.objects.create(program=program, fee_desc=fee_desc[i], amount=fee_amount[i])
                        messages.success(request, 'program updated successfully')
                        return redirect('program.index')
                else:
                    messages.warning(request, 'Please add atleast one fee')
                    return redirect('program.edit', cid=cid)
            else:
                return render(request, 'program/edit.html', {'program': program_form, 'fee': fee_form, 'fees': fee})
        except models.Program.DoesNotExist:
            return redirect('program.index')
    else:
        return redirect('program.index')


def delete(request, cid):
    try:
        program = models.Program.objects.get(id=cid)
        program.delete()
        messages.success(request, 'program deleted successfully')
        return redirect('program.index')
    except models.Program.DoesNotExist:
        return redirect('program.index')
