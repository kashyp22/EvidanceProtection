from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    type=models.CharField(max_length=40)

class Investigator(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=40)
    qualification=models.CharField(max_length=40)
    place=models.CharField(max_length=40)
    city=models.CharField(max_length=40)
    pin=models.CharField(max_length=40)
    adharno=models.CharField(max_length=40)
    photo=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)

class Case(models.Model):
    crime_type=models.CharField(max_length=100)
    summary=models.CharField(max_length=500)
    narration=models.CharField(max_length=500)
    date_reported=models.DateField()
    date_occured=models.DateField()
    place = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    pin = models.CharField(max_length=40)
    post = models.CharField(max_length=40)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    status=models.CharField(max_length=20)
    arrest=models.CharField(max_length=20)
    charges=models.CharField(max_length=20)
    conviction=models.CharField(max_length=20)
    stolen_items=models.CharField(max_length=200)
    file = models.CharField(max_length=100)
    fir=models.CharField(max_length=200)
    INVESTIGATOR= models.ForeignKey(Investigator,on_delete=models.CASCADE)

class victim_or_suspect(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    place = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    pin = models.CharField(max_length=40)
    adharno = models.CharField(max_length=40)
    photo = models.CharField(max_length=100)
    type=models.CharField(max_length=10)
    CASE = models.ForeignKey(Case, on_delete=models.CASCADE)

class Evidance(models.Model):
    CASE=models.ForeignKey(Case,on_delete=models.CASCADE)
    type=models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date_collected=models.DateField()
    collected_by=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    land_mark=models.CharField(max_length=50)
    storage_location=models.CharField(max_length=50)
    filename=models.CharField(max_length=100)

class User(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    place=models.CharField(max_length=40)
    city=models.CharField(max_length=40)
    pin=models.CharField(max_length=40)
    adharno=models.CharField(max_length=40)
    photo=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)

class Complaint(models.Model):
    complaint = models.CharField(max_length=100)
    USER= models.ForeignKey(User,on_delete=models.CASCADE)
    date_reported = models.DateField()
    date_occured = models.DateField()
    place = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    pin = models.CharField(max_length=40)
    post = models.CharField(max_length=40)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=20)

class Feedback(models.Model):
    feedback = models.CharField(max_length=100)
    date = models.DateField()
    USER= models.ForeignKey(User,on_delete=models.CASCADE)

class Chat(models.Model):
    FROM = models.ForeignKey(Login,on_delete=models.CASCADE,related_name="fromid")
    TO = models.ForeignKey(Login,on_delete=models.CASCADE,related_name="toid")
    Chat=models.CharField(max_length=200)
    date=models.DateField()

class Action(models.Model):
    COMPLAINT = models.ForeignKey(Complaint,on_delete=models.CASCADE)
    INVESTIGATOR = models.ForeignKey(Investigator, on_delete=models.CASCADE)
    action=models.CharField(max_length=100)
    date=models.DateField()