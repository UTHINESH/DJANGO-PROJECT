from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Products
# from .models import Profile
from .models import User as user1
from .forms import UserFrom,CreateUserForm,Loginform
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login




# Create your views here.
def myapp(request):
    myusers=user1.objects.all().values()
    myproducts=Products.objects.all().values()
    # myprofile=Profile.objects.all().values()
    template=loader.get_template('index.html')
    context={
        'userlist':myusers,
        'productlist':myproducts,
        # 'profilelist':myprofile,
    }
    return HttpResponse(template.render(context,request))

def prod_details(request,id):
    product=Products.objects.get(p_id=id)
    template2=loader.get_template('prod_details.html')
    context={
        'product':product,
    }
    return HttpResponse(template2.render(context,request))



# def profile(request,id):
#     profile=Profile.objects.get(profile_id=id)
#     template=loader.get_template('image.html')
#     context={
#         'profile':profile,
#     }
#     return HttpResponse(template.render(context,request))

# def userlogin(request):
#     # return HttpResponse("this is a login page is yet to be built....")
#     template3=loader.get_template('login.html')
#     return HttpResponse(template3.render())



#create a user

def createUser(request):

    form = UserFrom()
    
    if request.method == 'POST':
        form = UserFrom(request.POST)

        if form.is_valid():
            form.save()
            # return HttpResponse('your User is created')
            return redirect('home')


    context ={'form': form}

    template4=loader.get_template('create-user-form.html')
    return HttpResponse(template4.render(context,request))

    # return render(request,'user-form.html',context=context)




# update a user


def updateUser(request,pk):

    task=user1.objects.get(user_id=pk)

    form= UserFrom(instance=task)

    if request.method == 'POST':

        form = UserFrom(request.POST,instance=task)

        if form.is_valid():
            form.save()
            # return HttpResponse('your User is created')
            return redirect('home')
        


    context ={'form': form}
    return render(request,'update-user.html',context=context)

  


# detete a  user



def deleteUser(request,pk):

    task=user1.objects.get(user_id=pk).name
    
    
    if request.method == 'POST':

        task.delete()

        return redirect('home')
    
    context={'object':task}
        
    return render(request,'delete-user.html',context=context)













   
# Create a super user


def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():

            # current_user =form.save(commit=False)

            form.save()

            return HttpResponse("User Register!")

    context = {'form':form}

    return render(request,'register.html',context=context)


# login a django user

def my_login(request):
    
    form = Loginform()

    if request.method == 'POST':

        form = Loginform(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')


            user =authenticate(request,username=username,password=password)

            if user is not None:

                auth.login(request, user)

                return HttpResponse('You have logged in!')


    context ={'form' : form}

    return render(request,'my-login.html',context=context)