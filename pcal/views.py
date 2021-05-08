from django.shortcuts import render
from .models import MemPlan, Member
from .forms import MemPcal, MemForm
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect,render


# Create your views here.
class MemberListView(ListView):
    model = Member


class MemberCreateView(CreateView):
    model = Member
    success_url = reverse_lazy('index')
    fields = ('firstName', 'lastName', 'age')


class MemberUpdateView(UpdateView):
    model = Member
    success_url = reverse_lazy('index')
    fields = ('firstName', 'lastName', 'age')


class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy('index')


def adddata(request, **kwargs):
    form = MemPcal()
    member = Member.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = MemPcal(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('Inavlid')

    return render(request, 'pcal/memdata.html', {'form': form, 'member': member})


def getpremium(request, **kwargs):
    data = MemPlan.objects.filter(member_id=kwargs['pk'])
    for d in data:
        if d.componentName == 'Si':
            suminsured = int(d.componentValue)
        if d.componentName == 'rt':
            rate = int(d.componentValue) / 100 * 10
        if d.componentName == 'Tn':
            time = int(d.componentValue)
    pre = suminsured * rate * time

    return render(request, 'pcal/getpremium.html', {'data': data, 'premium': pre})







