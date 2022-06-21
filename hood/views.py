
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD

from hood.models import NeighbourHood,Business
=======
from .models import Business
from django.views.generic  import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from hood.models import NeighbourHood
>>>>>>> d48b1df3f89cf43bfe8cd3a131b2ca78528a3c73
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from .forms import NeighbourForm,ProfileForm,BusinessForm
from django.contrib.auth.decorators import login_required



from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def home (request):
    hoods=NeighbourHood.objects.all()
   
    
    return render(request,'neighbour/home.html',{'hoods':hoods})

def registerpage(request):
    form=CreateUserForm()
    
    if request.method == 'POST':
         form=CreateUserForm(request.POST)
         if form.is_valid():
             form.save()    
             
             user = form.cleaned_data.get('username')
             messages.success(request,'Account has been created for' + user)    
             return redirect('login')    
                   
                   
    context={'form':form}
    return render(request,'neighbour/register.html',context)


def loginpage (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('update')
        else:
            messages.info(request,'Username or Password is incorrect')
             
        
    return render(request,'neighbour/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

def userprofile(request):
    
    
    return render(request,'neighbour/profile.html')
@login_required(login_url='login')
def community(request):
    current_user = request.user
    form = NeighbourForm(request.POST,request.FILES)
    if request.method == 'POST':
            if form.is_valid():
                hood = form.save(commit=False)
                hood.user = request.user
                hood.save()
                
                return redirect ('home')
            else :
                # form = ProfileForm()
                pass
    
    return render(request,'neighbour/community.html',{'form':form})

@login_required(login_url='login')
def update(request):
    
        if request.method == 'POST':
            form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
            if form.is_valid():
                form.save()

            return redirect('home')
        else:
            form=ProfileForm
        return render(request,'neighbour/updateprofile.html',{'form':form})
    
def search(request):
    if request.method == 'GET':
        search=request.GET.get('search')
        if search:
<<<<<<< HEAD
            hoods=NeighbourHood.objects.filter(name__icontains=search)
            return render(request, 'neighbour/search.html',{'hoods':hoods})
        
        
# def view(request,pk):
#     form = NeighbourHood .objects.get(id=pk)
#     return render(request,'neighbour/hood.html',{'form' : form})

def bizz(request):
   
    if request.method == 'POST':
         form = BusinessForm(request.POST,request.FILES)
         if form.is_valid():
                form.save()
                
                return redirect ('search')
    
    else:
        form=BusinessForm()
    return render(request,'neighbour/business.html',{'form':form})


def business_details(request):
    business=Business.objects.all()
    return render(request, 'neighbour/hood.html',{'business':business})


=======
            form=NeighbourHood.objects.filter(name__icontains=search)
            
    return render(request, 'neighbour/search.html',{'form':form})


class BusinessListView(LoginRequiredMixin,ListView):
    model = Business
    template_name= 'estate/home.html'
    context_object_name = 'businesses'


class BusinessDetailView(LoginRequiredMixin,DetailView):
    model = Business

class BusinessCreateView(LoginRequiredMixin,CreateView):
    model = Business
    fields = ['name','email','business_image','location']

    def form_valid(self, form):
        form.instance.business_owner = self.request.user
        return super().form_valid(form)


class BusinessUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Business
    fields = ['name', 'email', 'business_image','location']

    def form_valid(self, form):
        form.instance.business_owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        business = self.get_object()

        if self.request.user == business.business_owner:
            return True
        return False


class BusinessDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Business
    success_url = '/'

    def test_func(self):
        business = self.get_object()


        if self.request.user == business.business_owner:
            return True
        return False
>>>>>>> d48b1df3f89cf43bfe8cd3a131b2ca78528a3c73
