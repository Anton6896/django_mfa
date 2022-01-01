from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .codes.forms import CodeForm
from django.contrib.auth import get_user_model
from . import utils


@login_required
def home_view(request):
    return render(request, 'index.html', {})


def auth_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            request.session['user_pk'] = user.pk
            return redirect('verify_view')

    return render(request, 'auth.html', {'form': form})


def verify_view(request):
    form = CodeForm(request.POST or None)

    if request.session['user_pk']:
        user = get_user_model().objects.get(pk=request.session['user_pk'])
        verification_code = user.verification_code.code

        if not request.POST:
            sms_msg = f"{user.username} enter this code : {verification_code}"
            res = utils.twilio_send_sms(sms_msg, user.phone_number)
            print(res)

        if form.is_valid():
            code_from_form = form.cleaned_data.get('code')

            if str(verification_code) == str(code_from_form):
                login(request, user)
                return redirect('home_view')
            else:
                return redirect('auth_view')

    return render(request, 'verify.html', {'form': form})


def verified_view(request):
    return render(request, 'verified_user.html', {})
