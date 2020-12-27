from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ShowForm
from .models import Show
# Create your views here.

def index(request): 
    return render(request, 'index.html')


def shows(request,id=None):
    if id:
        sid=id
    else:
        sid = request.GET.get('id', '')
    if sid:
        show = Show.objects.get(id=sid)
        context={"show":show}
        return render(request,"showsingle.html",context)
    shows=Show.objects.all()
    context={"shows":shows}
    return render(request,"show.html",context)


def deleteshow(request):
    sid = request.GET.get('id', '')
    Show.objects.filter(id=sid).delete()
    return redirect("shows")

def addnew(request):
    if request.method == 'POST':
        show = ShowForm(request.POST)
        if show.is_valid():
            shows=Show.objects.filter(Title__iexact=request.POST['Title'])
            if shows:
                messages.success(request, "Title must be unique" )
                return render(request, "addnew.html", {'form': show})
            show=show.save()
            return redirect('/shows/?id='+str(show.id))#render(request,"showsingle.html",context)
        else:
            return render(request,"addnew.html",{'form':show})
    form=ShowForm()
    return render(request,"addnew.html",{'form':form})

def editshow(request):
    sid = request.GET.get('id', '')
    show= Show.objects.get(id=sid)

    if request.method=='POST':
        show = ShowForm(request.POST)
        if show.is_valid():
            shows = Show.objects.filter(Title__iexact=request.POST['Title'])
            # print('shows', shows)
            if shows:
             id=shows[0].id
             if id!=int(sid):
                messages.success(request, "This Title is already Exist")
                return render(request,"editshow.html",{'form':show})
            oldshow=Show.objects.get(id=sid)
            show = ShowForm(request.POST,instance=oldshow)
            show=show.save()
            # print(show.id)
            return redirect('/shows/?id=' + str(sid))
        else:
            return render(request,"editshow.html",{'form':show})
    form = ShowForm(initial={'id':show.id,'Title': show.Title, 'Network': show.Network, 'Description': show.Description,
                             'Release_date': show.Release_date})
    return render(request,"editshow.html",{'form':form})


