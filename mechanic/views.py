from django.shortcuts import render,redirect
from mymodels.models import Request, Mechanic
from django.contrib.auth.password_validation import validate_password, MinimumLengthValidator, CommonPasswordValidator
from django.contrib import messages
from .forms  import CustomUserChangeForm
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives,EmailMessage
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from mymodels.models import *
import threading


# Create your views here.


class EmailThread(threading.Thread):
    '''Use this class to send emails on different thread so that application does not hold memory and CPU resoucees
        while waiting for the SMTP server to respond 
    '''
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=False)



@login_required
def dashboard(request):
    myrequests = Request.objects.all()
    return render(request,"mechanic/dashboard.html",{myrequests:myrequests})


@login_required
def user_info_update(request):
    info_form = Mechanic(instance=request.user)
    if request.method == 'POST':
        info_form = CustomUserChangeForm(request.POST,request.FILES,instance=request.user)
        if info_form.is_valid():
            info_form.save()
            messages.success(request, 'information set successfully')
            if not request.user.date_joined:
                return redirect('mechanic:password_update')
            return redirect(request.META.get('HTTP_REFERER', '/'))
            
        messages.error(request, 'Update failed. Please try again')
    context = {'info_form':info_form}
    return render(request,'mechanic/user_info_update.html',context)
    
@login_required
def profile(request):
    return render(request,"mechanic/profile.html")


class RequestPasswordResetEmail(View):
   
    def get(self,request):

        return render(request,'mechanic/password_reset.html')

    def post(self,request):
        
        email = request.POST['email']

        context = {'values':request.POST,}

        current_site=get_current_site(request)
        try:
            user = Custom_User.objects.filter(email=str(email))
            print(user[0])
            if user:
                email_contents ={
                'user':user[0],
                'domain':current_site.domain,
                'uidb64': urlsafe_base64_encode(force_bytes(user[0].pk)),
                'token':PasswordResetTokenGenerator().make_token(user[0]),
                }
                link = reverse('mechanic:new-password',kwargs = {'uidb64': email_contents['uidb64'], 'token': email_contents['token']})

                email_subject = 'Invoice Tracker: Password Reset Request'
                reset_url = 'http://'+current_site.domain+link

                merge_data = { 
                                    
                            'Account':user[0],
                        
                            'reset_link':reset_url
                        }
                               
                text_body = render_to_string("mechanic/passwordresetmail.txt", merge_data)
                html_body = render_to_string("mechanic/passwordResetMail.html", merge_data)
                # print(f'sending mail to {user[0].email}')
                msg = EmailMultiAlternatives(email_subject,text_body, from_email="helpdesk@psiug.org",
                        to=[user[0].email])
                msg.attach_alternative(html_body, "text/html")
                EmailThread(msg).start()
                messages.success(request, 'Password reset link has been sent, Check your email')

                return render(request,'mechanic/password_reset.html',context)
            else:
                messages.error(request, f"Account with specified email does not exist")
                return render(request,'mechanic/password_reset.html',context)
        except Exception as e:
            messages.error(request, f"Contact Systems Administrator: \n\n {e}")
            return render(request,'mechanic/password_reset.html',context)
        


@login_required
def password_update(request):
    if request.method == 'POST':        
        old_password = request.POST.get("old_password")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        try:
            validate_password(password1, user=request.user, password_validators=[MinimumLengthValidator(), CommonPasswordValidator()])
            user = authenticate(username=request.user, password=old_password)
            if user == request.user:
                if password1 == password2:
                    actual_user = request.user
                    actual_user.set_password(password1)
                    actual_user.save()
                    messages.success(request,"Login with your new password")
                    return redirect("mymodels:logout_view")
                else:
                    messages.error(request,"the re-ented password doesn't match")
                    return redirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request,"wrong old password")
                return redirect(request.META.get('HTTP_REFERER'))

        except Exception as e:
            for err in e:
                messages.error(request, err)
            return redirect(request.META.get('HTTP_REFERER'))     
    return render(request,'mechanic/password_update.html')


def read_all_notifications(request):
    user = request.user
    notification = Notification.objects.filter(user=user, read=False)
    for notifi in notification:
        notifi.is_read = True
        notifi.save()
    return redirect(request.META.get('HTTP_REFERER'))


class PasswordReset(View):

    def get(self, request, uidb64, token):

        context = {
            'uidb64':uidb64,
            'token':token 
                   }
        try:
            user_id=force_str(urlsafe_base64_decode(uidb64))

            print(user_id)

            user = Custom_User.objects.get(pk=user_id)
            
            if not PasswordResetTokenGenerator().check_token(user, token):
                messages.info(request, "Password Reset Link already used. Please request for new link")
                return redirect('mymodels:login_view')
        except Exception as e:
            messages.info(request,"Password Reset Failed.")
            
            return render(request, 'mechanic/set-new-password.html', context)

        return render(request, 'mechanic/set-new-password.html', context)
    
    def post(self, request, uidb64, token):
        context = {
            'uidb64':uidb64,
            'token':token 
                   }

        password = request.POST['password']
        password2 = request.POST['password1']
#
# Add more password checks on complexity. 
        if password != password2:
            messages.error(request, "Passwords do not match")
            return render(request, 'mechanic/set-new-password.html', context)
        if len(password) < 6:
            messages.error(request, "Password should be longer than 6 Characters")
            return render(request, 'mechanic/set-new-password.html', context)
        
        try:
            user_id=force_str(urlsafe_base64_decode(uidb64))
            user = Custom_User.objects.get(pk=user_id)
            print(user.last_name)
            print(password)
            user.set_password(password)
            user.save()
            messages.success(request,"Your Password has been reset successfully")
            return redirect('mechanic:login_view')
        except Exception as e:
            messages.info(request,"Password Reset Failed. Contact Head Of Finance or Systems Administrator")
            print(f'Error is {e}')
            return render(request, 'mechanic/set-new-password.html', context)

