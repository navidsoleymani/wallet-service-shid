from django.http import HttpRequest
from django.views.decorators.http import require_GET, require_POST
from ratelimit.decorators import ratelimit
from repository import json_respose, paginator
from wallet import models as w_models
from wallet_service.settings import RATE_LIMIT
import MESSAGE


@require_POST
@ratelimit(key='ip', rate=RATE_LIMIT, block=True)
@json_respose
def WalletCreateAPIView(request: HttpRequest) -> [dict, str]:
    wlt = w_models.Wallet()
    wlt.set_default()
    if 'user_id' not in request.POST.keys():
        raise Exception('user_id:  ' + MESSAGE.REQUIRED)
    wlt.user_id = request.POST.get('user_id')
    if 'pocket_name' not in request.POST.keys():
        raise Exception('pocket_name:  ' + MESSAGE.REQUIRED)
    wlt.pocket_name = request.POST.get('pocket_name')
    if 'info' in request.POST.keys():
        wlt.info = request.POST.get('info')
    wlt.save()
    message = MESSAGE.CREATE_WALLET
    data = wlt.to_dict()
    return data, message


@require_GET
@ratelimit(key='ip', rate=RATE_LIMIT, block=True)
@json_respose
def WalletListAPIView(request: HttpRequest):
    queryset = w_models.Wallet.objects.all()
    page_number: int
    if 'page' in request.GET.keys():
        page_number = int(request.GET.get('page'))
    else:
        page_number = 1

    message = MESSAGE.WALLET_LIST
    data = paginator(queryset, page_number, 20)
    return data, message


@require_GET
@ratelimit(key='ip', rate=RATE_LIMIT, block=True)
@json_respose
def WalletPocketNameListAPIView(request: HttpRequest):
    if 'pocket_name' not in request.GET.keys():
        raise Exception('pocket_name:  ' + MESSAGE.REQUIRED)
    queryset = w_models.Wallet.objects.filter(
        pocket_name__exact=request.GET.get('pocket_name'),
    ).all()
    page_number: int
    if 'page' in request.GET.keys():
        page_number = int(request.GET.get('page'))
    else:
        page_number = 1

    message = MESSAGE.WALLET_LIST_POCKET_NAME
    data = paginator(queryset, page_number, 20)
    return data, message


@require_POST
@ratelimit(key='ip', rate=RATE_LIMIT, block=True)
@json_respose
def YourPocketCreateAPIView(request: HttpRequest) -> [dict, str]:
    yp = w_models.YourPocket()
    if 'user_id' not in request.POST.keys():
        raise Exception('user_id:  ' + MESSAGE.REQUIRED)
    yp.user_id = request.POST.get('user_id')
    if 'pocket_name' not in request.POST.keys():
        raise Exception('pocket_name:  ' + MESSAGE.REQUIRED)
    yp.pocket_name = request.POST.get('pocket_name')
    if 'info' in request.POST.keys():
        yp.info = request.POST.get('info')
    yp.set_default()

    yp.save()
    message = MESSAGE.CREATE_YOUR_POCKET
    data = yp.to_dict()
    return data, message


@require_GET
@ratelimit(key='ip', rate=RATE_LIMIT, block=True)
@json_respose
def YourPocketListAPIView(request: HttpRequest):
    queryset = w_models.YourPocket.objects.filter(active__exact=True).all()
    page_number: int
    if 'page' in request.GET.keys():
        page_number = int(request.GET.get('page'))
    else:
        page_number = 1

    message = MESSAGE.YOUR_POCKET_LIST
    data = paginator(queryset, page_number, 20)
    return data, message


@require_GET
@ratelimit(key='ip', rate=RATE_LIMIT, block=True)
@json_respose
def YourPocketPocketNameListAPIView(request: HttpRequest):
    if 'pocket_name' not in request.GET.keys():
        raise Exception('pocket_name:  ' + MESSAGE.REQUIRED)
    queryset = w_models.Wallet.objects.filter(
        pocket_name__exact=request.GET.get('pocket_name'),
    ).filter(active__exact=True).all()
    page_number: int
    if 'page' in request.GET.keys():
        page_number = int(request.GET.get('page'))
    else:
        page_number = 1

    message = MESSAGE.YOUR_POCKET_POCKET_NAME_LIST_
    data = paginator(queryset, page_number, 20)
    return data, message


@require_POST
@ratelimit(key='ip', rate=RATE_LIMIT, block=True)
@json_respose
def TransactionCreateAPIView(request: HttpRequest) -> [dict, str]:
    t = w_models.Transaction()
    if 'owner' not in request.POST.keys():
        raise Exception('owner:  ' + MESSAGE.REQUIRED)
    t.owner = request.POST.get('owner')
    if 'amount' not in request.POST.keys():
        raise Exception('amount:  ' + MESSAGE.REQUIRED)
    t.amount = float(request.POST.get('amount'))
    if 'type' not in request.POST.keys():
        raise Exception('type:  ' + MESSAGE.REQUIRED)
    t.type = request.POST.get('type')
    if request.POST.get('type') == 'wallet':
        if 'wallet_id' not in request.POST.keys():
            raise Exception('wallet_id:  ' + MESSAGE.REQUIRED)
        t.wallet_id = request.POST.get('wallet_id')
    elif request.POST.get('type') == 'your_pocket':
        if 'your_pocket_id' not in request.POST.keys():
            raise Exception('your_pocket_id:  ' + MESSAGE.REQUIRED)
        t.your_pocket_id = request.POST.get('your_pocket_id')
    else:
        raise Exception(MESSAGE.TYPE_IS_NOT_TRUE)

    if 'info' in request.POST.keys():
        t.info = request.POST.get('info')
    t.set_default()
    t.save()
    if t.is_valid:
        pass
    message = MESSAGE.TRANSACTION_TRUE
    data = t.to_dict()

    return data, message


@require_GET
@ratelimit(key='ip', rate=RATE_LIMIT, block=True)
@json_respose
def TransactionListAPIView(request: HttpRequest):
    queryset = w_models.Transaction.objects.get().all()
    page_number: int
    if 'page' in request.GET.keys():
        page_number = int(request.GET.get('page'))
    else:
        page_number = 1

    message = MESSAGE.TRANSACTION_LIST
    data = paginator(queryset, page_number, 20)
    return data, message


@require_GET
@ratelimit(key='ip', rate=RATE_LIMIT, block=True)
@json_respose
def TransactionAppliedListAPIView(request: HttpRequest):
    queryset = w_models.Transaction.objects.filter(applied__exact=True).all()
    page_number: int
    if 'page' in request.GET.keys():
        page_number = int(request.GET.get('page'))
    else:
        page_number = 1

    message = MESSAGE.TRANSACTION_LIST_APPLIED
    data = paginator(queryset, page_number, 20)
    return data, message


@require_GET
@ratelimit(key='ip', rate=RATE_LIMIT, block=True)
@json_respose
def TransactionNotAppliedListAPIView(request: HttpRequest):
    queryset = w_models.Transaction.objects.filter(applied__exact=False).all()
    page_number: int
    if 'page' in request.GET.keys():
        page_number = int(request.GET.get('page'))
    else:
        page_number = 1

    message = MESSAGE.TRANSACTION_LIST_NOT_APPLIED
    data = paginator(queryset, page_number, 20)
    return data, message


@require_GET
@ratelimit(key='ip', rate=RATE_LIMIT, block=True)
@json_respose
def TransactionWalletListAPIView(request: HttpRequest):
    if 'wallet_id' not in request.GET.keys():
        raise Exception('wallet_id:  ' + MESSAGE.REQUIRED)
    queryset = w_models.Transaction.objects.filter(
        wallet_id__exact=request.GET.get('wallet_id'),
    ).filter(applied__exact=True).all()
    page_number: int
    if 'page' in request.GET.keys():
        page_number = int(request.GET.get('page'))
    else:
        page_number = 1

    message = MESSAGE.TRANSACTION_LIST_BY_WALLET
    data = paginator(queryset, page_number, 20)
    return data, message


@require_GET
@ratelimit(key='ip', rate=RATE_LIMIT, block=True)
@json_respose
def TransactionYourPocketListAPIView(request: HttpRequest):
    if 'your_pocket_id' not in request.GET.keys():
        raise Exception('your_pocket_id:  ' + MESSAGE.REQUIRED)
    queryset = w_models.Transaction.objects.filter(
        your_pocket_id__exact=request.GET.get('your_pocket_id'),
    ).filter(applied__exact=True).all()
    page_number: int
    if 'page' in request.GET.keys():
        page_number = int(request.GET.get('page'))
    else:
        page_number = 1

    message = MESSAGE.TRANSACTION_LIST_BY_YOUR_POCKET
    data = paginator(queryset, page_number, 20)
    return data, message


@require_GET
@ratelimit(key='ip', rate=RATE_LIMIT, block=True)
@json_respose
def TransactionOwnerListAPIView(request: HttpRequest):
    if 'owner' not in request.GET.keys():
        raise Exception('owner:  ' + MESSAGE.REQUIRED)
    queryset = w_models.Transaction.objects.filter(
        owner__exact=request.GET.get('owner'),
    ).filter(applied__exact=True).all()
    page_number: int
    if 'page' in request.GET.keys():
        page_number = int(request.GET.get('page'))
    else:
        page_number = 1

    message = MESSAGE.TRANSACTION_LIST_BY_OWNER
    data = paginator(queryset, page_number, 20)
    return data, message
