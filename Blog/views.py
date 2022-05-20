from unicodedata import name
from django.shortcuts import render,redirect
from pymongo import MongoClient 

mongoclient = MongoClient("mongodb://127.0.0.1:27017/Dj")
db=mongoclient.Dj
userCollection=db.User


# Create your views here.
def login(request):
    if request.method=="POST":
        number=request.POST['number']
        name=request.POST['name']
        userCollection.insert_one({"number":number, "name":name})
    return render(request, "login.html")



def homePage(request):
    userDatas=list(userCollection.find())
   
    return render(request,"homePage.html",{"datas":userDatas})

def delete(request,number):
    print(number," ............................................")
    userCollection.delete_one({"number":number})
    return redirect('homePage')