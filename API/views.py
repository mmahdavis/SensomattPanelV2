"""Docstring."""
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from models.models import Bed, Patient, Nurse, Notifications, Bed_History
import json
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User


# ------------------------------ need change

@csrf_exempt
def notification(request, token):
    """Docstring."""
    x = []
    # enterdate = i.enterdate.strftime('%A, %d, %B, %Y')
    try:
        notification = Notifications.objects.filter(nurse=token)
        for i in notification:
            sendtime = i.sendtime.strftime('%f, %A')
            senddate = i.senddate.strftime('%A, %d, %B, %Y')
            if i.donedate is set:
                donetime = i.donetime.strftime('%f, %A')
                donedate = i.donedate.strftime('%A, %d, %B, %Y')
                x.append({"bedid": i.bed.id, "NotificationType": i.notificationtype, "IsDone": True, "SendTime": str(sendtime), "Senddate": str(senddate), "DoneTime": str(donetime), "Donedate": str(donedate), "Msg": i.msg})
            else:
                x.append({"bedid": i.bed.id, "NotificationType": i.notificationtype, "IsDone": False,  "SendTime": str(sendtime), "Senddate": str(senddate), "DoneTime": None, "Donedate": None, "Msg": i.msg})
        data = json.dumps(x)
        return HttpResponse(data)
    except Exception as e:
        return HttpResponse(e.args)


# ------------------------------ need change

@csrf_exempt
def numberofbed(request, token):
    """Docstring."""
    x = []
    try:
        numofbed = Bed.objects.all()
        for i in numofbed:
            x.append({"bedid": i.id, "patientid": i.patient.id, "bedtype": i.bedtype, "bedname": i.name})
        data = json.dumps(x)
        return HttpResponse(data)
    except Exception as e:
        return HttpResponse(e.args)


# ------------------------------ need change

@csrf_exempt
def patientinfo(request, token, patientId):
    """Docstring."""
    try:
        patientinfo = Patient.objects.get(id=patientId)
        # return HttpResponse(patientinfo.height)
        bmi = patientinfo.height / patientinfo.weight
        x = {"name": patientinfo.name, "history": patientinfo.history, "description": patientinfo.description, "transcription": patientinfo.transcription, "BMI": bmi}
        data = json.dumps(x)
        return HttpResponse(data)
    except Exception as e:
        return HttpResponse(e.args)


# ------------------------------ need change

@csrf_exempt
def patientstatus(request, token, bedId):
    """Docstring."""
    try:
        i = Bed.objects.get(id=bedId)
        x = {"status_type": i.statustype, "general_status": i.generalstatus, "image_patient_url": i.patientimg.url, "risks": i.risks, "alerts": i.alerts}
        data = json.dumps(x)
        return HttpResponse(data)
    except Exception as e:
        return HttpResponse(e.args)


# ------------------------------ need change

@csrf_exempt
def bedanalyses(request, token, bedId):
    """Docstring."""
    try:
        i = Bed.objects.get(id=bedId)
        x = {"image_status_url": i.imgstatus.url, "image_analyses_url": i.imganalyze.url}
        data = json.dumps(x)
        return HttpResponse(data)
    except Exception as e:
        return HttpResponse(e.args)


# ------------------------------ need change

@csrf_exempt
def suggestions(request, token, bedId):
    """Docstring."""
    try:
        i = Bed.objects.get(id=bedId)
        x = {"suggestions": i.suggestions}
        data = json.dumps(x)
        return HttpResponse(data)
    except Exception as e:
        return HttpResponse(e.args)


# ------------------------------ need change

@csrf_exempt
def bedhistory(request, token):
    """Docstring."""
    x = []
    try:
        bedhistory = Bed_History.objects.all()
        for i in bedhistory:
            enterdate = i.enterdate.strftime('%A, %d, %B, %Y')
            if i.exitdate is set:
                x.append({"isExited": False, "PatientName": i.patientname.name, "EnterDate": str(enterdate), "ExitDate": None})
            else:
                exitdate = i.exitdate.strftime('%A, %d, %B, %Y')
                x.append({"isExited": True, "PatientName": i.patientname.name, "EnterDate": str(enterdate), "ExitDate": str(exitdate)})
        data = json.dumps(x)
        return HttpResponse(data)
    except Exception as e:
        return HttpResponse(e.args)


# ------------------------------ need change

@csrf_exempt
def dashboard(request, token):
    """Docstring."""
    try:
        i = Nurse.objects.get(personalid=token)
        x = {"Name": i.name, "WorkTime": i.shift, "personnelid": i.personalid, "ProfilePhoto_url": i.profileimg.url}
        data = json.dumps(x)
        return HttpResponse(data)
    except Exception as e:
        return HttpResponse(e.args)
