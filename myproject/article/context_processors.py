from django.utils import timezone

def article(request):
    return {
        'today':timezone.now(),
    }