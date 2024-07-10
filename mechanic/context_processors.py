from mymodels.models import Notification

def notifications(request):
    if request.user.is_authenticated:
        user_notifications = Notification.objects.filter(user=request.user, read=False)
        return {'notifications': user_notifications}
    return {'notifications': []}