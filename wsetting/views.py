from django.http import HttpRequest
from django.views.decorators.http import require_POST
from wsetting import models
from wallet_service.settings import RATE_LIMIT
import MESSAGE
from repository import json_respose
from ratelimit.decorators import ratelimit


@require_POST
@ratelimit(key='ip', rate=RATE_LIMIT, block=True)
@json_respose
def transaction_limit(request: HttpRequest) -> [dict, str]:
    tl = models.TransactionLimit()
    if 'high' not in request.POST.keys():
        raise Exception('high:  ' + MESSAGE.REQUIRED)
    tl.high = float(request.POST.get('high'))
    if 'low' not in request.POST.keys():
        raise Exception('low:  ' + MESSAGE.REQUIRED)
    tl.low = float(request.POST.get('low'))
    tl.save()
    message = MESSAGE.SET_TRANSACTION_LIMIT
    data = tl.to_dict()
    return data, message


@require_POST
@ratelimit(key='ip', rate=RATE_LIMIT, block=True)
@json_respose
def expiry_date(request: HttpRequest) -> [dict, str]:
    ed = models.ExpiryDate()
    if 'day' not in request.POST.keys():
        raise Exception('day:  ' + MESSAGE.REQUIRED)
    ed.day = request.POST.get('day')
    if 'pocket_name' not in request.POST.keys():
        raise Exception('pocket_name:  ' + MESSAGE.REQUIRED)
    ed.pocket_name = request.POST.get('pocket_name')
    ed.save()
    message = MESSAGE.SET_EXPIRY_DATE
    data = ed.to_dict()
    return data, message
