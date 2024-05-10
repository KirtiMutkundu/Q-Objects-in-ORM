from django.shortcuts import render

from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.

def display_Dept(request):
    DPT=Dept.objects.all()

    DPT=Dept.objects.filter(dname__startswith='s')
    d={'DPT':DPT}
    return render(request,'display_dept.html',d)

def display_Emp(request):
    EPT=Emp.objects.all()

    EPT=Emp.objects.filter(ename__startswith='k', ename__endswith='g')
    EPT=Emp.objects.filter(Q(ename__startswith='k') | Q(job__endswith='t'))
    EPT=Emp.objects.filter(Q(deptno='10') | Q(deptno='20'))
    EPT=Emp.objects.filter(hiredate__range=('1996-01-01','2024-12-12'))
    EPT=Emp.objects.filter(mgr__isnull=True)

    d={'EPT':EPT}
    return render(request,'display_emp.html',context=d)

def display_Salgrade(request):
    SPT=Salgrade.objects.all()
    SPT=Salgrade.objects.filter(range (lowsal__gte=100 ))
    d={'SPT':SPT}
    return render(request,'display_salgrade.html',context=d)
