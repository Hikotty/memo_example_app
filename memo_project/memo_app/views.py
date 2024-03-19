from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Memo
import time
from .forms import MemoForm

# Create your views here.

def is_alive(request):
    return HttpResponse("Memo app is alive")

def memo_list(request):
    memos = Memo.objects.all()
    return render(request, 'memo_list.html', {'memos':memos})

def html_test(request):
    params = {
        'title':"Welcome memp app",
        'time':str(time.ctime())
    }
    return render(request, "index.html",params)

def memo_detail(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    if request.method == "POST":
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            messages.success(request, 'registred')
            return redirect('memo_list')
    else:
        form = MemoForm(instance=memo)
    return render(request, 'memo_detail.html', {'form':form, 'memo':memo})