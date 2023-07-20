from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render, redirect




# Create your views here.
def index(request):
    users = models.User.objects.all()
    user_list = {'users': users}

    return render(request,'social_app/index.html',context=user_list)


def beeps(request):
    all_beeps = models.Beeps.objects.all().order_by('-created_at')
    beeps_dict = {"beeps":all_beeps}
    return render(request,'social_app/beeps.html', context=beeps_dict)

@login_required(login_url="/login")
def addbeeps(request):
    if request.POST:
        message = request.POST["message"]
        created_at = timezone.now()
        models.Beeps.objects.create(username=request.user, message=message, created_at=created_at)

        return redirect(reverse('social:beeps'))
    else:
        return render(request,'social_app/addbeeps.html')


def myaccount(request):
    self_beeps = models.Beeps.objects.filter(username=request.user).order_by('-created_at')
    countBeeps = len(self_beeps)
    self_dict = {"self_beeps": self_beeps,"countBeeps": countBeeps}
    return render(request, 'social_app/myaccount.html', context=self_dict)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


