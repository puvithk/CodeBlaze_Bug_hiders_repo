from django.shortcuts import render,redirect
import cv2 
import numpy as np
import face_recognition as fr
from .models import Accountdetails 
import random as r 
from .form import UploadForm

def language(request):
    try:
        cap = cv2.VideoCapture(0)
        _,img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        my_face_encoding = fr.face_encodings(img)[0]
        for i in range(1,3):
            know_face = fr.load_image_file(f'CodeBlaze_bug_hiders\bankMachine\static\img\img{i}.jpg')
            result = fr.compare_faces([ my_face_encoding[ i ]] , know_face)
            if result[0] == True:
                all_user_details = Accountdetails.objects.all()[i]
                return render(request, 'home.html',{"all_user_details" : all_user_details})
        for user_detail in all_user_details:
            print(user_detail)
    except:
        pass
    return render(request, 'language.html')

def home(request):

    
    return render(request,"home.html")

def submit(request):
    return render(request,"home.html")


def submit_form(request):
    return render(request,'home.html')

def withdrw(request):
    return render(request,'deposit.html')
def upload(request):
    form1 = UploadForm(request.POST)
    if form1.is_valid():
        form1.save()
        return redirect(submit)
    return render(request,'createAcc.html',{'forms': form1})
def aiBot(request):
    return render(request,'aibot.html')