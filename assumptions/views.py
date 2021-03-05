from django.shortcuts import render
from django.http import HttpResponse
from .models import Assumptions,Absenteeis_and_Defective,Cost_Assumptions,Salary_growth_and_Incentives,Financial



def create_assumption(request):
    if request.method=='POST' and 'btnform1' in request.POST:
        No_of_years=request.POST.get('No_of_years')
        No_of_working_hrs_per_day=request.POST.get('No_of_working_hrs_per_day')
        Working_minutes_per_day = request.POST.get('Working_minutes_per_day')
        No_of_working_days_per_month = request.POST.get('No_of_working_days_per_month')
        Total_no_of_production_days_per_year = request.POST.get('Total_no_of_production_days_per_year')
        No_of_shifts_per_day = request.POST.get('No_of_shifts_per_day')
        Exchange_rate = request.POST.get('Exchange_rate')
        if bool(No_of_working_hrs_per_day) is True:
            Attendance_Time_hrs_perday=int(No_of_working_hrs_per_day)+1
        else:
            No_of_working_hrs_per_day=0
            Attendance_Time_hrs_perday=0
        if bool(No_of_years) is True:
            x=int(No_of_years)
            list1=list(range(1,x+1))
            context={'list1':list1}
        else:
            No_of_years=0
            list1=list(range(0,1))
            context={'list1':list1}

        a=Assumptions(No_of_years=No_of_years,No_of_working_hrs_per_day=No_of_working_hrs_per_day,Attendance_Time_hrs_perday=Attendance_Time_hrs_perday,
                      Working_minutes_per_day=Working_minutes_per_day,No_of_working_days_per_month=No_of_working_days_per_month,
                      Total_no_of_production_days_per_year=Total_no_of_production_days_per_year,No_of_shifts_per_day=No_of_shifts_per_day,
                      Exchange_rate=Exchange_rate)
        a.save()

        return render(request,'aform.html',context)
    else:
        return render(request,'aform.html')


def create_Absenteeis_and_Defective(request):
    print('btnform2' in request.POST)
    if request.method=='POST' and 'btnform2' in request.POST:
        a=Absenteeis_and_Defective()
        a.Sewing=request.POST.get('Sewing')
        a.Cutting = request.POST.get('Cutting')
        a.Finishing = request.POST.get('Finishing')
        a.Cutting_Output_as_percentage_of_Sewing_Output = request.POST.get('Cutting_Output_as_percentage_of_Sewing_Output')
        a.Finishing_Output_as_percentage_of_Sewing_Output = request.POST.get('Finishing_Output_as_percentage_of_Sewing_Output')
        a.Extra_Sewing_Machines_Required = request.POST.get('Extra_Sewing_Machines_Required')
        a.Cutting_Loss=request.POST.get('Cutting_Loss')
        a.Year1=request.POST.get('Year1')
        a.Year2=request.POST.get('Year2')
        a.Year3=request.POST.get('Year3')
        print('this is a',a)
        # a=Absenteeis_and_Defective(Sewing=Sewing,Cutting=Cutting,
        #               Finishing=Finishing,Cutting_Output_as_percentage_of_Sewing_Output=Cutting_Output_as_percentage_of_Sewing_Output,
        #               Finishing_Output_as_percentage_of_Sewing_Output=Finishing_Output_as_percentage_of_Sewing_Output,Extra_Sewing_Machines_Required=Extra_Sewing_Machines_Required,
        #               Cutting_Loss=Cutting_Loss,Year1=Year1,Year2=Year2,Year3=Year3)
        a.save()

        return render(request,'aform.html')
    else:
        return render(request,'aform.html')


def create_Cost_Assumptions(request):
        if request.method=='POST':
            a=request.POST.get('a')
            b = request.POST.get('b')
            c = request.POST.get('c')
            d = request.POST.get('d')
            e = request.POST.get('e')
            f = request.POST.get('f')
            g=request.POST.get('g')
            h=request.POST.get('h')
            i=request.POST.get('i')
            j=request.POST.get('j')
            k = request.POST.get('k')
            l = request.POST.get('l')
            m = request.POST.get('m')
            n = request.POST.get('n')
            o = request.POST.get('o')
            p = request.POST.get('p')
            q = request.POST.get('q')
            r = request.POST.get('r')
            s = request.POST.get('s')
            t = request.POST.get('t')
            u = request.POST.get('u')
            v = request.POST.get('v')

            ch=Cost_Assumptions(a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h,i=i,j=j,
                               k=k,l=l,m=m,n=n,o=o,p=p,q=q,r=r,s=s,t=t,u=u,v=v)

            ch.save()

            return render(request,'aform.html')
        else:
            return render(request,'aform.html')