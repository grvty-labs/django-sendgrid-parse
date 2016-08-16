from django.db import transaction
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Attachment
from .forms import EmailForm
from .signals import message_received


@csrf_exempt
@require_POST
@transaction.atomic
def sendgrid_email_receiver(request):
    try:
        form = EmailForm(request.POST)
        if form.is_valid():
            form.instance.save()
            attachments_list = list()
            for i in range(1, form.cleaned_data['attachments'] + 1):
                attachments_list.append(
                    Attachment(number=i, file=request.FILES['attachment%d' % i],
                               email=form.instance)
                )

            Attachment.objects.bulk_create(attachments_list)
            message_received.send(sender=None, email=form.instance)
            return HttpResponse(status=200)

        return HttpResponse(status=400)

    except:
        print("Unexpected error: {}".format(sys.exc_info()[0]))
        return HttpResponse(status=500)
