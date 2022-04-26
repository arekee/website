from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import AddPostForm
from django.utils import timezone
from .models import Basket
from .models import Comment
from .models import Hotel
from .models import Posts
from .models import Signup
from .forms import  AddComment
from django.http import HttpResponse
from .forms import SignupForm
from django.core.mail import EmailMessage

def send_message(request):
    email=EmailMessage("You have registered successfully", "Django", "200103321@stu.sdu.edu.kz",["arsen.toksyn@mail.ru"])
    email.attach_file('C:/Users/User/Desktop/Back end/Project_2/websites/main/static/main/images/turkistan.jpg')
    email.send(fail_silently=False)
    return render(request, 'main/main.html')

def show_post(request, post_slug):
    post=get_object_or_404(Posts, slug=post_slug)
    context={'post':post}
    return render(request,'main/post.html', context=context)

def signup(request):
    if request.method == 'POST':

        form=AddPostForm(request.POST)
        # name = request.POST['name']
        # login = request.POST['login']
        # mail = request.POST['email']
        # phone = request.POST['phone']
        # date = request.POST['birthdate']
        # password = request.POST['password']
        # User = Signup()
        # User.name = name
        # User.login = login
        # User.email = mail
        # User.phone = phone
        # User.password = password
        # User.birthdate = timezone.now()
        # User.save()
        form.save()
        return render(request, 'main/signup.html',
                      {'title':'TIELE',
                       'form':form,
                       })
    else:
        form=AddPostForm()
        return render(request, 'main/signup.html',{'title':'T   IELE','form':form })

def create(request):
    error =''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = ' not valid'
    form = SignupForm()
    data = {
        'form': form,
        'error':error
    }
    return render(request, 'main/create.html', data)

def basket(request):
    tickets = Basket.objects.all()
    hotels = Hotel.objects.all()
    return render(request, 'main/basket.html', {'title:':'It is Basket', 'tickets': tickets , 'hotels': hotels})

def login(request):
    return render(request, 'main/login.html', {'title':'Log in'})

def hotels(request):
    return render(request, 'main/hotels.html', {'title':'Hotels'})
def places(request):
    return render(request, 'main/places.html')
#def signup(request):
    #  return render(request, 'main/signup.html', {'title':'Sign up'})

def main(request):
    comments=Comment.objects.all()
    return render(request,'main/main.html', {'title':'Main page','comments':comments})
def upload(request):
    upload=AddComment()
    if request.method=='POST':
        upload = AddComment(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('main')
        else:
            return HttpResponse("""Error,reload on <a href="{{url : 'main'}}">reload</a>""")
    else:
        return render(request, 'main/upload_form.html', {'upload_form':upload})
def update_Comment(request, comment_id):
        comment_id = int(comment_id)
        try:
            comment_sel = Comment.objects.get(id = comment_id)
        except Comment.DoesNotExist:
            return redirect('main')
        comment_form = AddComment(request.POST or None, instance=comment_sel)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('main')
        return render(request, 'main/upload_form.html', {'upload_form': comment_form})
def delete_Comment(request, comment_id):
    comment_id = int(comment_id)
    try:
        comment_sel= Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return redirect('main')
    comment_sel.delete()
    return redirect('main')