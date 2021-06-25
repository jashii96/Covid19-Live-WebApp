from django.http import request
from django.shortcuts import render
from django.urls import path
import datetime
from django.utils import timezone
import json
# Create your views here.

import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "d9cbda2f6dmshc2bba4bd0e71c1ap1ab42fjsnc01c43dd2e87",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

#print(response.text)

def worldview(request):
    noofresults=int(response['results'])
    mylist=[]
    for i in range(noofresults):
        mylist.append(response['response'][i]['country'])
    if request.method == "POST":
        selectedcountry=request.POST['selectedcountry']
        noofresults=int(response['results'])
        for i in range(noofresults):
            if selectedcountry == response['response'][i]['country']:
                new = response['response'][i]['cases']['new']
                active = response['response'][i]['cases']['active']
                critical = response['response'][i]['cases']['critical']
                recovered = response['response'][i]['cases']['recovered']
                total = response['response'][i]['cases']['total']
                deaths = int(total) - int(critical) - int(recovered)
                now1 = timezone.now()
        context = {'selectedcountry':selectedcountry,'mylist':mylist,'new':new,'active':active,'critical':critical,'death':deaths,'recovered':recovered,'total':total,'now1':now1}        
        return render(request,'index.html',context)
    
    mylist=[]
    for i in range(noofresults):
        mylist.append(response['response'][i]['country'])
    cont={'mylist':mylist}
    return render(request,'index.html',cont)