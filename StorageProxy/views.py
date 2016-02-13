from django.shortcuts import render
from django.views.decorators.http import require_POST, require_safe

from .models import StoredData
from .utils import get_page_num_and_size


@require_safe
def list_all_data(request):
    page_num, page_size = get_page_num_and_size(request.GET, default_page_num=1, default_page_size=20)
    start_index = (page_num - 1) * page_size
    end_index = start_index + page_size
    context = {
        'start_index': start_index,
        'end_index': end_index,
        'page_num': page_num,
        'page_size': page_size,
        'data': StoredData.objects.order_by('-upload_time')[start_index:end_index],
    }
    return render(request, 'StorageProxy/all_data.html', context=context)


@require_safe
def upload_data(request):
    pass


@require_safe
def api_list_data(request):
    page_num, page_size = get_page_num_and_size(request.GET, default_page_num=1, default_page_size=20)


@require_POST
def api_upload_data(request):
    pass
