from django.shortcuts import render,redirect
from django.contrib import messages
from .apps import DetectConfig
from .models import Person
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
import pickle
per=Person()
def home(request):
    if request.method=="POST":
        per.x=request.POST['pfname']
        per.y=request.POST['pgen']
        per.z=int(request.POST['page'])
        per.em=request.POST['pemail']
        per.x=per.x.capitalize()
        per.y=per.y.upper()
        if per.y=='M':
            per.x='Mr.'+per.x
        else:
            per.x='Mrs.'+per.x
        return render(request,'predict.html',{'c':per})
    else:
        return render(request,'index.html')
def start(request):
    if request.method=="POST":
        a=int(request.POST['op1'])
        b=int(request.POST['op2'])
        c=int(request.POST['op3'])
        d=int(request.POST['op4'])
        e=int(request.POST['op5'])
        f=int(request.POST['op6'])
        g=int(request.POST['op7'])
        h=int(request.POST['op8'])
        i=int(request.POST['op9'])
        l=[a,b,c,d,e,f,g,h,i]
        ans=DetectConfig.mdl.predict([l])
        if(ans[0]==2):
            per.s="you are safe"
            per.anss="NEGATIVE"
            ctx = {
                    'user': per.x,
                    'gen':per.y,
                    'age':per.z,
                    'emaill':per.em,
                    'ans':"NEGATIVE",
                    'status':"you are safe"
                }
            message = get_template('gmail.html').render(ctx)
            msg = EmailMessage(
                'Cancer Prediction',
                message,
                'breast.cancer.predict@gmail.com',
                [per.em],
            )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()
            print('mail sent')
            return render(request,'just.html',{'c':per})
        else:
            per.s="we are very sorry to sat that"
            per.anss="POSITIVE"
            ctx = {
                    'user': per.x,
                    'gen':per.y,
                    'age':per.z,
                    'emaill':per.em,
                    'ans':"POSITIVE",
                    'status':"we are very sorry to say that"
                    
                }
            message = get_template('gmail.html').render(ctx)
            msg = EmailMessage(
                'Cancer Prediction',
                message,
                'breast.cancer.predict@gmail.com',
                [per.em],
            )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()
            print('mail sent')    
            return render(request,'just.html',{'c':per})
    else:
        return render(request,'predict.html')
def about(request):
    return render(request,'about.html')
 
            