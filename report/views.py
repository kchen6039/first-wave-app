from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Report

# Create your views here.

def post_list(request):
    reports = Report.objects.filter(started_date__lte=timezone.now()).order_by('started_date')
    return render(request, 'report/post_list.html', {'reports': reports})

def post_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'report/post_detail.html', {'report': report})
