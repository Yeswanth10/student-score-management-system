from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def read(request):
    name=request.POST['name']
    python=int(request.POST['python'])
    java=int(request.POST['java'])
    mysql=int(request.POST['mysql'])
    html=int(request.POST['html'])
    django=int(request.POST['django']) 
    operation=request.POST['operation']
    print(name,python,java,mysql,html,django,operation)
    if operation=="TOTAL":
        result=python+java+mysql+html+django
    elif operation=="AVERAGE":
        result=(python+java+mysql+html+django)/5
    elif operation=="GRADE":
        total=(python+java+mysql+html+django)/5
        if total>=90:
            result="A"
        elif total>=80:
            result="B"
        elif total>=70:
            result="C"
        elif total>=60:
            result="D"
        else:
            result="F"
    elif operation=="STATUS":
        total=(python+java+mysql+html+django)/5
        if total>=60:
            result="PASS"
        else:
            result="FAIL"
    
    return render(request, 'home.html', {'name':name, 'python':python, 'java':java, 'mysql':mysql, 'html':html, 'django':django, 'result':result})
    
    



