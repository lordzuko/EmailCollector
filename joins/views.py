from django.conf import settings
from django.shortcuts import render,HttpResponseRedirect,Http404
from .forms import EmailForm
from .forms import JoinForm
from .models import Join
import  uuid

def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""

    return ip

def get_ref_id():
    ref_id = str(uuid.uuid4())[:11].replace("-",'').lower()
    try:
        id_exists = Join.objects.all().get(ref_id=ref_id)
        get_ref_id()
    except:
        return ref_id

def home(request):

    try:
        referer = request.session['referer']
        obj = Join.objects.get(id=referer)
    except:
        obj = None


    form = JoinForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        new_join,created = Join.objects.get_or_create(email=email)
        if created:
            new_join.ip_address = get_ip(request)
            #add my referer to db
            if not obj == None:
                new_join.refered_by = obj
            new_join.ref_id = get_ref_id()
            new_join.save()

            #Recieve the list of users refered by obj
            # print Join.objects.filter(refered_by=obj)
            # print obj.referer.all()

        return HttpResponseRedirect('/%s' %new_join.ref_id)
        # new_join = form.save(commit=False)
        # new_join.ip_address = get_ip(request)
        # new_join.save()

    context = {
        'form': form,
    }
    template = "home.html"
    return render(request, template, context)


def share(request, ref_id):
    '''
        share function takes the ref_id and outputs the
        numbers of friends it refered
    '''
    try:
        #get the referer's  from ref_id
        referer = Join.objects.get(ref_id=ref_id)
        print referer
        #get the list of friends ferered by this referer
        #friends_refered = Join.objects.get(refered_by=referer)
        print Join.objects.filter(refered_by=referer)
        count = Join.objects.filter(refered_by=referer).count()
        ref_url = settings.SHARE_URL+"%s" %(referer.ref_id)
    except:
        raise Http404


    context = {
        'ref_id':referer.ref_id,
        'count': count,
        'ref_url': ref_url,
    }
    template = "share.html"
    return render(request, template, context)
