from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_GET
from wsetting import models
from wallet.models import Wallet


@require_GET
def setMinimax(request: HttpRequest):
    last_minmax = models.MaxMiN.objects.first()
    if last_minmax is None:
        minmax = models.MaxMiN()
    else:
        minmax = last_minmax
    minmax.minimum = float(request.GET.get('minimum'))
    minmax.maximum = float(request.GET.get('maximum'))
    minmax.save()
    return HttpResponse('ok')


@require_GET
def block(request: HttpRequest):
    wlt = Wallet.objects.filter(pk=request.GET.get('wallet_id')).first()
    wlt.is_block = True
    wlt.save()
    return HttpResponse('ok')


@require_GET
def unblock(request: HttpRequest):
    wlt = Wallet.objects.filter(pk=request.GET.get('wallet_id')).first()
    wlt.is_block = False
    wlt.save()
    return HttpResponse('ok')
