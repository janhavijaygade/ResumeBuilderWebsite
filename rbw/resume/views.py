from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'resume/index.html')


from .models import Information, Infosecond, Freshers


def form(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        jobtitle = request.POST['jobtitle']
        email = request.POST['email']
        phone = request.POST['phone']
        profile = request.POST['profile']

        skill1 = request.POST['skill1']
        skill2 = request.POST['skill2']
        skill3 = request.POST['skill3']
        skilldesc1 = request.POST['skilldesc1']
        skilldesc2 = request.POST['skilldesc2']
        skilldesc3 = request.POST['skilldesc3']

        tech1 = request.POST['tech1']
        tech2 = request.POST['tech2']
        tech3 = request.POST['tech3']
        tech4 = request.POST['tech4']
        tech5 = request.POST['tech5']
        tech6 = request.POST['tech6']

        job1 = request.POST['job1']
        job2 = request.POST['job2']
        job3 = request.POST['job3']
        job4 = request.POST['job4']
        comname1 = request.POST['comname1']
        comname2 = request.POST['comname2']
        comname3 = request.POST['comname3']
        comname4 = request.POST['comname4']
        Upto1 = request.POST['Upto1']
        Upto2 = request.POST['Upto2']
        Upto3 = request.POST['Upto3']
        Upto4 = request.POST['Upto4']
        fromyear1 = request.POST['fromyear1']
        fromyear2 = request.POST['fromyear2']
        fromyear3 = request.POST['fromyear3']
        fromyear4 = request.POST['fromyear4']

        jt1 = request.POST['jt1']
        jt2 = request.POST['jt2']
        jt3 = request.POST['jt3']
        jt4 = request.POST['jt4']

        university = request.POST['university']
        degree = request.POST['degree']
        gpa = request.POST['gpa']

        if len(firstname) < 2 or len(lastname) < 2 or len(email) < 3 or len(phone) < 10:
            messages.error(request, "Please fill the form correctly")
        else:
            form = Information(firstname=firstname, lastname=lastname, jobtitle=jobtitle, email=email,
                               phone=phone, profile=profile, skilldesc1=skilldesc1, skilldesc2=skilldesc2,
                               skill1=skill1, skill2=skill2, skill3=skill3, skilldesc3=skilldesc3,
                               tech1=tech1, tech2=tech2, tech3=tech3, tech4=tech4,
                               tech5=tech5, tech6=tech6, job1=job1, job2=job2,
                               job3=job3, job4=job4, comname1=comname1, comname2=comname2,
                               comname3=comname3, comname4=comname4, Upto1=Upto1, Upto2=Upto2,
                               Upto3=Upto3, Upto4=Upto4, fromyear1=fromyear1, fromyear2=fromyear2,
                               fromyear3=fromyear3, fromyear4=fromyear4, jt1=jt1, jt2=jt2,
                               jt3=jt3, jt4=jt4, university=university, degree=degree, gpa=gpa,
                               )
            form.save()
            messages.success(request, "Your data has been successfully received")

    return render(request, 'resume/form.html')


from .models import Contact


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "resume/contact.html")


def about(request):
    return render(request, 'resume/about.html')


def finalresume(request):
    data = Information.objects.all()
    examp = {"info": data}
    return render(request, 'resume/finalresume.html', examp)


def form2(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        jobtitle = request.POST['jobtitle']
        email = request.POST['email']
        phone = request.POST['phone']
        linkedin = request.POST['linkedin']
        github = request.POST['github']
        codepen = request.POST['codepen']
        codechef = request.POST['codechef']
        careersummary = request.POST['careersummary']

        job1 = request.POST['job1']
        job2 = request.POST['job2']
        job3 = request.POST['job3']
        job4 = request.POST['job4']
        comname1 = request.POST['comname1']
        comname2 = request.POST['comname2']
        comname3 = request.POST['comname3']
        comname4 = request.POST['comname4']
        Upto1 = request.POST['Upto1']
        Upto2 = request.POST['Upto2']
        Upto3 = request.POST['Upto3']
        Upto4 = request.POST['Upto4']
        fromyear1 = request.POST['fromyear1']
        fromyear2 = request.POST['fromyear2']
        fromyear3 = request.POST['fromyear3']
        fromyear4 = request.POST['fromyear4']
        jt1 = request.POST['jt1']
        jt2 = request.POST['jt2']
        jt3 = request.POST['jt3']
        jt4 = request.POST['jt4']
        jobachieve1 = request.POST['jobachieve1']
        jobachieve2 = request.POST['jobachieve2']
        jobachieve3 = request.POST['jobachieve3']
        jobachieve4 = request.POST['jobachieve4']
        tech11 = request.POST['tech11']
        tech21 = request.POST['tech21']
        tech31 = request.POST['tech31']
        tech41 = request.POST['tech41']
        tech51 = request.POST['tech51']
        tech61 = request.POST['tech61']
        tech12 = request.POST['tech12']
        tech22 = request.POST['tech22']
        tech32 = request.POST['tech32']
        tech42 = request.POST['tech42']
        tech52 = request.POST['tech52']
        tech62 = request.POST['tech62']
        tech13 = request.POST['tech13']
        tech23 = request.POST['tech23']
        tech33 = request.POST['tech33']
        tech43 = request.POST['tech43']
        tech53 = request.POST['tech53']
        tech63 = request.POST['tech63']
        tech14 = request.POST['tech14']
        tech24 = request.POST['tech24']
        tech34 = request.POST['tech34']
        tech44 = request.POST['tech44']
        tech54 = request.POST['tech54']
        tech64 = request.POST['tech64']

        skill1 = request.POST['skill1']
        skill2 = request.POST['skill2']
        skill3 = request.POST['skill3']
        skill4 = request.POST['skill4']

        pb1 = request.POST['pb1']
        pb2 = request.POST['pb2']
        pb3 = request.POST['pb3']
        pb4 = request.POST['pb4']

        lifeskill1 = request.POST['lifeskill1']
        lifeskill2 = request.POST['lifeskill2']
        lifeskill3 = request.POST['lifeskill3']
        lifeskill4 = request.POST['lifeskill4']
        lifepb1 = request.POST['lifepb1']
        lifepb2 = request.POST['lifepb2']
        lifepb3 = request.POST['lifepb3']
        lifepb4 = request.POST['lifepb4']

        other1 = request.POST['other1']
        other2 = request.POST['other2']
        other3 = request.POST['other3']
        other4 = request.POST['other4']
        other5 = request.POST['other5']
        other6 = request.POST['other6']

        university = request.POST['university']
        degree = request.POST['degree']
        finalUpto = request.POST['finalUpto']
        finalfromyear = request.POST['finalfromyear']
        university2 = request.POST['university2']
        degree2 = request.POST['degree2']
        finalUpto2 = request.POST['finalUpto2']
        finalfromyear2 = request.POST['finalfromyear2']

        award1 = request.POST['award1']
        award2 = request.POST['award2']
        awarddesc1 = request.POST['awarddesc1']
        awarddesc2 = request.POST['awarddesc2']

        lang1 = request.POST['lang1']
        lang2 = request.POST['lang2']
        lang3 = request.POST['lang3']
        interest1 = request.POST['interest1']
        interest2 = request.POST['interest2']
        interest3 = request.POST['interest3']

        if len(firstname) < 2 or len(lastname) < 2 or len(email) < 3 or len(phone) < 10:
            messages.error(request, "Please fill the form correctly")
        else:
            form2 = Infosecond(firstname=firstname, lastname=lastname, jobtitle=jobtitle, email=email,
                               phone=phone, linkedin=linkedin, github=github, codepen=codepen, codechef=codechef,
                               careersummary=careersummary, job1=job1, job2=job2,
                               job3=job3, job4=job4, comname1=comname1, comname2=comname2,
                               comname3=comname3, comname4=comname4, Upto1=Upto1, Upto2=Upto2,
                               Upto3=Upto3, Upto4=Upto4, fromyear1=fromyear1, fromyear2=fromyear2,
                               fromyear3=fromyear3, fromyear4=fromyear4, jt1=jt1, jt2=jt2,
                               jt3=jt3, jt4=jt4, jobachieve1=jobachieve1, jobachieve2=jobachieve2,
                               jobachieve3=jobachieve3, jobachieve4=jobachieve4, tech11=tech11, tech21=tech21,
                               tech31=tech31, tech41=tech41, tech51=tech51, tech61=tech61, tech12=tech12,
                               tech22=tech22, tech32=tech32, tech42=tech42, tech52=tech52, tech62=tech62,
                               tech13=tech13, tech23=tech23, tech33=tech33, tech43=tech43, tech53=tech53, tech63=tech63,
                               tech14=tech14, tech24=tech24, tech34=tech34, tech44=tech44, tech54=tech54, tech64=tech64,
                               skill1=skill1, skill2=skill2, skill3=skill3,
                               pb1=pb1, pb2=pb2, pb3=pb3, pb4=pb4,
                               lifeskill1=lifeskill1, lifeskill2=lifeskill2, lifeskill3=lifeskill3,
                               lifeskill4=lifeskill4,
                               lifepb1=lifepb1, lifepb2=lifepb2, lifepb3=lifepb3, lifepb4=lifepb4,
                               other1=other1, other2=other2, other3=other3, other4=other4, other5=other5, other6=other6,
                               university=university, degree=degree, finalUpto=finalUpto, finalfromyear=finalfromyear,
                               university2=university2, degree2=degree2, finalUpto2=finalUpto2,
                               finalfromyear2=finalfromyear2,
                               award1=award1, award2=award2, awarddesc1=awarddesc1, awarddesc2=awarddesc2,
                               lang1=lang1, lang2=lang2, lang3=lang3,
                               interest1=interest1, interest2=interest2, interest3=interest3

                               )
            form2.save()
            messages.success(request, "Your data has been successfully received")

    return render(request, 'resume/form2.html')


def trial(request):
    data = Infosecond.objects.all()
    examp2 = {"info2": data}
    return render(request, 'resume/trial.html', examp2)


def formfreshers(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        linkedin = request.POST['linkedin']
        address = request.POST['address']
        profile = request.POST['profile']


        school = request.POST['school']
        Upto1 = request.POST['Upto1']
        fromyear1 = request.POST['fromyear1']
        college = request.POST['college']
        Upto2 = request.POST['Upto2']
        fromyear2 = request.POST['fromyear2']
        graduation = request.POST['graduation']
        Upto3 = request.POST['Upto3']
        fromyear3 = request.POST['fromyear3']

        lang1 = request.POST['lang1']
        lang2 = request.POST['lang2']
        lang3 = request.POST['lang3']

        projecttitle1 = request.POST['projecttitle1']
        projectskill1 = request.POST['projectskill1']
        desc1 = request.POST['desc1']
        projecttitle2 = request.POST['projecttitle2']
        projectskill2 = request.POST['projectskill2']
        desc2 = request.POST['desc2']
        projecttitle3 = request.POST['projecttitle3']
        projectskill3 = request.POST['projectskill3']
        desc3 = request.POST['desc3']

        tech1 = request.POST['tech1']
        tech2 = request.POST['tech2']
        tech3 = request.POST['tech3']
        tech4 = request.POST['tech4']
        tech5 = request.POST['tech5']
        tech6 = request.POST['tech6']
        tech7 = request.POST['tech7']
        tech8 = request.POST['tech8']

        if len(firstname) < 2 or len(lastname) < 2 or len(email) < 3 or len(phone) < 10:
            messages.error(request, "Please fill the form correctly")
        else:
            formfreshers = Freshers(firstname=firstname, lastname=lastname, email=email, phone=phone,
                                    linkedin=linkedin, address=address, school=school,
                                    Upto1=Upto1,profile=profile
                                    , fromyear1=fromyear1, college=college, Upto2=Upto2, fromyear2=fromyear2
                                    , graduation=graduation, Upto3=Upto3, fromyear3=fromyear3,
                                    lang1=lang1, lang2=lang2, lang3=lang3, projecttitle1=projecttitle1,
                                    projectskill1=projectskill1, desc1=desc1, projecttitle2=projecttitle2,
                                    projectskill2=projectskill2, desc2=desc2, projecttitle3=projecttitle3,
                                    projectskill3=projectskill3, desc3=desc3, tech1=tech1, tech2=tech2,
                                    tech3=tech3, tech4=tech4, tech5=tech5, tech6=tech6, tech7=tech7, tech8=tech8, )
            formfreshers.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'resume/formfreshers.html')


def freshers(request):
    data = Freshers.objects.all()
    examp3 = {"info3": data}
    return render(request, 'resume/freshers.html', examp3)
