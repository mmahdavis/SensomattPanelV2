"""Docstring."""
from django.db import models


class Nurse(models.Model):
    """Docstring."""

    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    shift = models.CharField(max_length=2, choices=(('D', 'Day'), ('N', 'Night'), ('LN', 'Late Night')), null=False)
    personalid = models.IntegerField(null=False, blank=False, unique=True)
    profileimg = models.ImageField(upload_to='profileimg', null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=30, null=False, blank=False, unique=True)
    password = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        """Docstring."""
        return str(self.name)


class Token(models.Model):
    """Docstring."""

    token = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        """Docstring."""


class Patient(models.Model):
    """Docstring."""

    name = models.CharField(max_length=50, null=False, blank=False)
    history = models.CharField(max_length=1000, null=True, default=None)
    description = models.CharField(max_length=1000, null=True)
    transcription = models.CharField(max_length=1000, null=True)
    height = models.IntegerField(null=False, blank=False)
    weight = models.IntegerField(null=False, blank=False)
    age = models.SmallIntegerField(null=False, blank=False)
    nurse = models.ForeignKey(Nurse, on_delete=models.SET_NULL, null=True)
    mobile = models.IntegerField(null=False, blank=False, unique=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), null=False)

    def __str__(self):
        """Docstring."""
        return str(self.name)


class Bed(models.Model):
    """Docstring."""

    bedtype = models.IntegerField(choices=((1, 'red'), (2, 'yellow'), (3, 'green'), (4, 'gray')), default=4)
    name = models.CharField(max_length=20, null=False, blank=False, default='NoName Bed')
    imgstatus = models.ImageField(upload_to='bedsstatus', null=True, blank=True)
    imganalyze = models.ImageField(upload_to='bedsanalyze', null=True, blank=True)
    suggestions = models.CharField(max_length=500, null=True)
    patient = models.OneToOneField(Patient, on_delete=models.SET_NULL, null=True)
    nurse = models.ForeignKey(Nurse, on_delete=models.SET_NULL, null=True)

    statustype = models.IntegerField(choices=((1, 'red'), (2, 'yellow'), (3, 'green')), default=3)
    generalstatus = models.CharField(max_length=1000, null=True)
    patientimg = models.ImageField(upload_to='patientimg', null=True, blank=True)
    risks = models.CharField(max_length=500, null=True)
    alerts = models.CharField(max_length=500, null=True)

    def __str__(self):
        """Docstring."""
        return str(self.name)


class Bed_History(models.Model):
    """Docstring."""

    bed = models.ForeignKey(Bed, on_delete=models.CASCADE, default="")
    patientname = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    enterdate = models.DateField()
    exitdate = models.DateField(null=True)
    nurse = models.ForeignKey(Nurse, on_delete=models.DO_NOTHING)
    sickness = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        """Docstring."""
        return str(self.enterdate) + str(self.exitdate) + " bed number: " + str(self.bed)


class Notifications(models.Model):
    """Docstring."""

    bed = models.ForeignKey(Bed, on_delete=models.CASCADE, default=0)
    notificationtype = models.IntegerField(choices=((1, 'red'), (2, 'yellow'), (3, 'green'), (4, 'blue')), default=4)
    sendtime = models.TimeField()
    senddate = models.DateField()
    donetime = models.TimeField(null=True, default=None)
    donedate = models.DateField(null=True, default=None)
    msg = models.CharField(max_length=1000)
    nurse = models.ForeignKey(Nurse, on_delete=models.DO_NOTHING)

    def __str__(self):
        """Docstring."""
        return str(self.senddate) + " nurse name: " + str(self.nurse)
