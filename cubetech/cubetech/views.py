from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import userForm
from service.models import Data
from news.models import News
from django.core.paginator import Paginator
from enquiry.models import Enquiry

from django.core.mail import send_mail

def home(request):

    #send_mail(
     #   "Testing Mail",
      #  "Here is the message.",
       # "mpmukesh45@gmail.com",
       # ["mukeshrawal8@gmail.com"],
       # fail_silently=False,
    #)

    newsInfo = News.objects.all()
    newData = Data.objects.all().order_by('title')[:2]
    #for a in newData:
        #print(a.title)
        #print(a.description)
    

    data = {
        'nData': newData,
        'newsInfo':newsInfo,
        'title':'Home Page',
        'lang_list':['php', 'java', 'python'],
        'nums':[10,20,30,32,21,12,40],
        'std_details':[
            {'name':'Mukesh', 'phone':'9750505050'},
            {'name':'Rani', 'phone':'8540988777'}
        ]
    }
    return render(request, "index.html", data)


def newsDetails(request, slug):
    newsDetail = News.objects.get(slug_title=slug)

    data = {
        'newsdata': newsDetail,
    }
    return render(request, "newsdetails.html", data)

def about(request):
    return render(request, "index.html")

def division(request):
    if request.method == 'POST':
        m1 = int(request.POST['marks1'])
        m2 = int(request.POST['marks2'])
        m3 = int(request.POST['marks3'])
        m4 = int(request.POST['marks4'])
        m5 = int(request.POST['marks5'])

        total = (m1+m2+m3+m4+m5)
        per = total/5

        if (per > 60 and per <=100):
            div='First Division'

        elif (per > 45 and per <= 60):
            div='Second Division'

        elif (per > 32 and per <= 45):
            div='Third Division'

        else:
            div='Fail'

        data = {
            't':total,
            'p':per,
            'd': div
        }
        return render(request, 'division.html', data)
    return render(request, 'division.html')


def evenOdd(request):
    c =''
    if request.method == 'POST':
        if request.POST['num1'] == '':
            return render(request, 'evenodd.html', {'error':True})
        n = int(request.POST['num1'])
        if n%2 == 0:
            c = 'Even Number'
        else:
            c = 'Odd Number'

    return render(request, 'evenodd.html', {'c':c})

def contact(request):
    khabarData = Data.objects.all()
    
    if request.method=="GET":
        nd = request.GET.get('khabar')
        if nd != None:
            khabarData = Data.objects.filter(title__icontains=nd)



    data = {
        'news':khabarData,
    }
    return render(request, "contact.html",data)

def khabar(request):
    khabarData = News.objects.all()
    paginator = Paginator(khabarData,2)
    page_num = request.GET.get('page')
    finalData = paginator.get_page(page_num)

    totalPage = finalData.paginator.num_pages

    data = {
        'newsData': finalData,
        'lastpage': totalPage,
        'pagelist': [n+1 for n in range(totalPage)]
    }
    return render(request, "khabar.html",data)


def course(request):
    return render(request, "course.html")

def coursedetails(request, courseid):
    return HttpResponse(courseid,"<b>Course details page</b>")

def userform(request):
    total = 0
    fn = userForm()
    data= {'form':fn}
    try:
        #n1 = int(request.GET['val1'])
        #n2 = int(request.GET['val2'])

        n1 = int(request.POST['val1'])
        n2 = int(request.POST['val2'])
        #print(n1+n2)
        total = n1+n2

        data ={
            'form':fn,
            'output':total
        }

        return HttpResponseRedirect('/contact')

    except:
        pass
    #return render(request, "userform.html", {'output':total})
    return render(request, "userform.html", data)

def submitForm(request):
    #return HttpResponse(request)

    total = 0
    data= {}
    try:
       
        n1 = int(request.POST['num1'])
        n2 = int(request.POST['num2'])
        #print(n1+n2)
        total = n1+n2

        data ={
            'n1':n1,
            'n2':n2,
            'output':total
        }

        return HttpResponse(total)

    except:
        pass
    #return render(request, "userform.html", {'output':total})
    return render(request, "userform.html", data)


def enquiry(request):
    if request.method == 'POST':
        name = request.POST['uname']
        email = request.POST['umail']
        address = request.POST['addr']
        en = Enquiry(name=name, email=email, address=address)
        en.save()
        
    return render(request, "user_form.html")
