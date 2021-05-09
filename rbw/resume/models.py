# Create your models here.

from django.db import models


# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email


class Information(models.Model):
    sno = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    jobtitle = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    profile = models.CharField(max_length=500)

    # skills
    skill1 = models.CharField(max_length=50)
    skill2 = models.CharField(max_length=50)
    skill3 = models.CharField(max_length=50)
    skilldesc1 = models.CharField(max_length=150)
    skilldesc2 = models.CharField(max_length=150)
    skilldesc3 = models.CharField(max_length=150)

    # techniques
    tech1 = models.CharField(max_length=15)
    tech2 = models.CharField(max_length=15)
    tech3 = models.CharField(max_length=15)
    tech4 = models.CharField(max_length=15)
    tech5 = models.CharField(max_length=15)
    tech6 = models.CharField(max_length=15)

    # Experience
    job1 = models.CharField(max_length=15)
    job2 = models.CharField(max_length=15)
    job3 = models.CharField(max_length=15)
    job4 = models.CharField(max_length=15)
    comname1 = models.CharField(max_length=15)
    comname2 = models.CharField(max_length=15)
    comname3 = models.CharField(max_length=15)
    comname4 = models.CharField(max_length=15)
    Upto1 = models.CharField(max_length=4)
    fromyear1 = models.IntegerField()
    Upto2 = models.IntegerField()
    fromyear2 = models.IntegerField()
    Upto3 = models.IntegerField()
    fromyear3 = models.IntegerField()
    Upto4 = models.IntegerField()
    fromyear4 = models.IntegerField()
    jt1 = models.CharField(max_length=100)
    jt2 = models.CharField(max_length=100)
    jt3 = models.CharField(max_length=100)
    jt4 = models.CharField(max_length=100)

    # Education
    university = models.CharField(max_length=20)
    degree = models.CharField(max_length=20)
    gpa = models.IntegerField()

    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Information from " + self.firstname + ' - ' + self.email


class Infosecond(models.Model):
    sno = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=25, blank=True)
    lastname = models.CharField(max_length=25, blank=True)
    jobtitle = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    linkedin = models.CharField(max_length=12)
    github = models.CharField(max_length=12)
    codepen = models.CharField(max_length=12)
    codechef = models.CharField(max_length=12)
    careersummary = models.CharField(max_length=500)

    # Experience
    job1 = models.CharField(max_length=15)
    job2 = models.CharField(max_length=15)
    job3 = models.CharField(max_length=15)
    job4 = models.CharField(max_length=15)
    comname1 = models.CharField(max_length=15)
    comname2 = models.CharField(max_length=15)
    comname3 = models.CharField(max_length=15)
    comname4 = models.CharField(max_length=15)
    Upto1 = models.CharField(max_length=4)
    fromyear1 = models.IntegerField()
    Upto2 = models.IntegerField()
    fromyear2 = models.IntegerField()
    Upto3 = models.IntegerField()
    fromyear3 = models.IntegerField()
    Upto4 = models.IntegerField()
    fromyear4 = models.IntegerField()
    jt1 = models.CharField(max_length=100)
    jt2 = models.CharField(max_length=100)
    jt3 = models.CharField(max_length=100)
    jt4 = models.CharField(max_length=100)
    jobachieve1 = models.CharField(max_length=100)
    jobachieve2 = models.CharField(max_length=100)
    jobachieve3 = models.CharField(max_length=100)
    jobachieve4 = models.CharField(max_length=100)
    tech11 = models.CharField(max_length=15)
    tech21 = models.CharField(max_length=15)
    tech31 = models.CharField(max_length=15)
    tech41 = models.CharField(max_length=15)
    tech51 = models.CharField(max_length=15)
    tech61 = models.CharField(max_length=15)
    tech12 = models.CharField(max_length=15)
    tech22 = models.CharField(max_length=15)
    tech32 = models.CharField(max_length=15)
    tech42 = models.CharField(max_length=15)
    tech52 = models.CharField(max_length=15)
    tech62 = models.CharField(max_length=15)
    tech13 = models.CharField(max_length=15)
    tech23 = models.CharField(max_length=15)
    tech33 = models.CharField(max_length=15)
    tech43 = models.CharField(max_length=15)
    tech53 = models.CharField(max_length=15)
    tech63 = models.CharField(max_length=15)
    tech14 = models.CharField(max_length=15)
    tech24 = models.CharField(max_length=15)
    tech34 = models.CharField(max_length=15)
    tech44 = models.CharField(max_length=15)
    tech54 = models.CharField(max_length=15)
    tech64 = models.CharField(max_length=15)

    # skills
    skill1 = models.CharField(max_length=50)
    skill2 = models.CharField(max_length=50)
    skill3 = models.CharField(max_length=50)
    skill4 = models.CharField(max_length=50)

    pb1 = models.CharField(max_length=3)
    pb2 = models.CharField(max_length=3)
    pb3 = models.CharField(max_length=3)
    pb4 = models.CharField(max_length=3)


    # lifeskills
    lifeskill1 = models.CharField(max_length=50)
    lifeskill2 = models.CharField(max_length=50)
    lifeskill3 = models.CharField(max_length=50)
    lifeskill4 = models.CharField(max_length=50)
    lifepb1 = models.CharField(max_length=3)
    lifepb2 = models.CharField(max_length=3)
    lifepb3 = models.CharField(max_length=3)
    lifepb4 = models.CharField(max_length=3)

    #other skills
    other1 = models.CharField(max_length=15)
    other2 = models.CharField(max_length=15)
    other3 = models.CharField(max_length=15)
    other4 = models.CharField(max_length=15)
    other5 = models.CharField(max_length=15)
    other6 = models.CharField(max_length=15)

    # Education
    university = models.CharField(max_length=20)
    degree = models.CharField(max_length=20)
    finalUpto = models.IntegerField()
    finalfromyear = models.IntegerField()
    university2 = models.CharField(max_length=20)
    degree2 = models.CharField(max_length=20)
    finalUpto2 = models.IntegerField()
    finalfromyear2 = models.IntegerField()

    #awards
    award1 = models.CharField(max_length=50)
    award2 = models.CharField(max_length=50)
    awarddesc1 = models.CharField(max_length=150)
    awarddesc2 = models.CharField(max_length=150)

    lang1 = models.CharField(max_length=15)
    lang2 = models.CharField(max_length=15)
    lang3 = models.CharField(max_length=15)
    interest1 = models.CharField(max_length=15)
    interest2 = models.CharField(max_length=15)
    interest3 = models.CharField(max_length=15)


    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Information from " + self.firstname + ' - ' + self.email
