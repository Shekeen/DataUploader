import hashlib
import re

from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST, require_safe

from .forms import UploadForm
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


def upload_data(request):
    if request.method == 'POST':
        return handle_uploaded_data(request)
    else:
        return upload_page(request)


@require_safe
def upload_page(request):
    context = {
        'form': UploadForm(),
    }
    return render(request, 'StorageProxy/upload.html', context=context)


@require_POST
def handle_uploaded_data(request):
    form = UploadForm(request.POST, request.FILES)
    if not form.is_valid():
        return HttpResponseBadRequest()
    if re.search(r'\s', form.cleaned_data['key']):
        return HttpResponseBadRequest()

    hash = hashlib.sha1()
    size = 0
    for chunk in request.FILES['file'].chunks():
        hash.update(chunk)
        size += len(chunk)
    hexdigest = hash.hexdigest()

    new_data = StoredData(
        key=form.cleaned_data['key'],
        sha1_hexdigest=hexdigest,
        byte_size=size,
        comment=form.cleaned_data['comment'],
    )
    new_data.save()

    return redirect('list-all-data')


@require_safe
def api_list_data(request):
    page_num, page_size = get_page_num_and_size(request.GET, default_page_num=1, default_page_size=20)


@require_POST
def api_upload_data(request):
    pass
