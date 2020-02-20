from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from .forms import RequestCreationForm
from .models import Request
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.core.mail import send_mail

def index(request):
    if request.user.is_authenticated:
        return redirect('c-home')
    return render(request,'employer/index.html')
@login_required
def home(request):
    #Post request after submission of form
    if request.method=='POST':
        r_form=RequestCreationForm(request.POST)
        if r_form.is_valid():
            r_form.save()
            try:
                send_mail(
                'Request created',
                'Request has been created',
                request.user.email,
                ['shubham.harin@gmail.com'],
                fail_silently=False,
                )
            except:
                print("Failed to send Mail")    
            return redirect('c-home')
    #Normal Page        
    r_form=RequestCreationForm()
    r_data=Request.objects.all()
    #Pagination of requests
    page = request.GET.get('page', 1)
    paginator = Paginator(r_data, 10)
    try:
        requests = paginator.page(page)
    except PageNotAnInteger:
        requests = paginator.page(1)
    except EmptyPage:
        requests = paginator.page(paginator.num_pages)

    context={
        'r_form':r_form,
        'r_data':r_data,
        'requests':requests
    }
    return render(request,'employer/home.html',context)

def register(request):
    context={}
    return render(request,'employer/register.html',context)

class RequestDetailView(DetailView):
    model = Request
    
class RequestUpdateView(UpdateView):
    model = Request
    fields = '__all__'
    def get_success_url(self):
        return reverse('request-detail', kwargs={'pk' : self.object.pk})
    
    '''def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False'''

class RequestDeleteView(DeleteView):
    model = Request
    success_url = '/corporate/home'

    def test_func(self):
        #post = self.get_object()
        #if self.request.user == post.author:
        #   return True
        return True#False
    