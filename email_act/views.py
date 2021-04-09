from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.conf import settings




User = get_user_model()

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(email=request.POST['email'], password=request.POST['password1'],
                                            instagram=request.POST['instagram'], tiktok=request.POST['tiktok'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('email_act/email_act.html',
                                       {
                                           'user' : user,
                                           'domain': current_site.domain,
                                           'uid': urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
                                           'token': account_activation_token.make_token(user),
                                       })
            mail_subject = "Email Activation"
            user_email = user.email
            email = EmailMessage(mail_subject, message, to=[user_email])
            email.send()
            return HttpResponse(
                '<div style="font-size: 40px; width: 100%; height:100%; display:flex; text-align:center; '
                'justify-content: center; align-items: center;">'
                'Please check out your email to activate your account'
                '</div>'
            )

    return render(request, 'email_act/signup.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password1']

        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/blog')

        else:
            return render(request, 'email_act/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'email_act/login.html')

def logout(request):
    pass

def activate(request, uid64, token):

    uid = force_text(urlsafe_base64_decode(uid64))
    user = User.objects.get(pk=uid)

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/blog')
    else:
        return HttpResponse('Access Denied')


