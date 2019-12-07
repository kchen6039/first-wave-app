from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Report
from .forms import ReportForm
from django.views.generic.edit import FormView
from django.views.generic import ListView

class HomePageView(ListView):
    model = Report
    template_name = 'report/home.html'

# Create your views here.

def post_list(request):
    reports = Report.objects.filter(started_date__lte=timezone.now()).order_by('started_date')
    return render(request, 'report/post_list.html', {'reports': reports})

def post_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'report/post_detail.html', {'report': report})

def post_new(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.author = request.user
            report.created_date = timezone.now()
            report.invest = form.cleaned_data['invest']
            report.withdrew = form.cleaned_data['withdrew']
            report.gain_loss = form.cleaned_data['gain_loss']
            report.face_value = form.cleaned_data['face_value']
            """ for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    img = Report(cover=formfile)
                    img.save() """
            report.cover = form.cleaned_data['cover']
            report.venue = form.cleaned_data['venue']
            report.officer = form.cleaned_data['officer']
            report.text = form.cleaned_data['text']
            report.save()
            return redirect('post_detail', pk=report.pk)
    else:
        form = ReportForm()
    return render(request, 'report/post_edit.html', {'form': form})

def post_edit(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            report = form.save(commit=False)
            report.author = request.user
            report.created_date = timezone.now()
            report.invest = form.cleaned_data['invest']
            report.withdrew = form.cleaned_data['withdrew']
            report.gain_loss = form.cleaned_data['gain_loss']
            report.face_value = form.cleaned_data['face_value']
            report.cover = form.cleaned_data['cover']
            report.venue = form.cleaned_data['venue']
            report.officer = form.cleaned_data['officer']
            report.text = form.cleaned_data['text']
            report.save()
            return redirect('post_detail', pk=report.pk)
    else:
        form = ReportForm(instance=report)
    return render(request, 'report/post_edit.html', {'form': form})