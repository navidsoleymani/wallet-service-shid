from django.db.models.query import QuerySet
from functools import wraps
from django.http import JsonResponse


def paginator(query_set: QuerySet, page_number: int, object_per_page: int) -> dict:
    q_list = query_set
    if page_number is None:
        page_number = 1
    if object_per_page is None:
        object_per_page = 2

    start = (page_number - 1) * object_per_page
    stop = min(start + object_per_page, len(q_list))
    data = {}
    for i in range(start, stop):
        data[f'{i + 1}'] = q_list[i].to_dict()
    return {
        'count': query_set.count(),
        'num_pages': int(query_set.count() / object_per_page) + 1,
        'object_list': data,
    }


def json_respose(func):
    @wraps(func)
    def wrap(request, *args, **kwargs):
        try:
            data, message = func(request, *args, **kwargs)
            return JsonResponse(
                {
                    'success': True,
                    'message': message,
                    'data': data
                }
            )
        except Exception as ex:
            return JsonResponse(
                {
                    'success': False,
                    'message': ex.args,
                    'data': {}
                }
            )

    return wrap
