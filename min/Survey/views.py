from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseNotAllowed
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView,DetailView
from .models import Question,option
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, get_object_or_404

def home(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
                # team = request.user.team
            context = {'team': None}

        else:
            context = {'team': None}

        return render(request, 'home.html', context=context)
    else:
        return HttpResponseNotAllowed('not allowed')


def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'signup.html', context=context)

    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return redirect('signup')

    else:
        return HttpResponseNotAllowed('not allowed')


def login_s(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        form = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context=context)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')

        return redirect('login')

    else:
        return HttpResponseNotAllowed('not allowed')


class Home(ListView):
    queryset = Question.objects.all()
    template_name='home.html'
    paginate_by=5


def SureyDetail(request, pk):
    queryset = option.objects.filter(question=pk)
    queryset2 = Question.objects.get(id=pk)
    total=0
    for e in queryset:
        total=total+e.rate

    context = {
        'object_optin':queryset,
        'object':queryset2,
        'total':total,
    }


    return render(request, 'Surey_detail.html', context)

@login_required(login_url='/signin')
def submit(request , oid) : 
    if request.method == 'GET':
      optn = get_object_or_404(option , id = oid)
      optn.rate += 1  
      optn.save()  
      return redirect('home')
