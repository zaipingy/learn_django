from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from myapp.models import Event, Guest


def index(request):
    # return HttpResponse('hello, user')
    return render(request, 'index.html')


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        # if username == 'admin' and password == 'admin':
        if user is not None:
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user', username, 3600)
            request.session['user'] = username
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})


@login_required
def event_manage(request):
    event_list = Event.objects.order_by('id')
    # username = request.COOKIES.get('user')
    username = request.session.get('user', '')
    paginator = Paginator(event_list, 2)
    page = request.GET.get('page')
    # num = []
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    # for contact in contacts:
    #     num.append(Guest.objects.filter(event__name__contains=contact, sign=1).count())
    return render(request, 'event_manage.html', {"user": username,
                                                 "events": contacts,
                                                 # "num": num,
                                                 })


@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('name', '')
    num = Guest.objects.filter(event__name__contains=search_name,sign=1).count()
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, 'event_manage.html', {'user': username,
                                                 'events': event_list,
                                                 'num': num})


@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'guest_manage.html', {'user': username,
                                                 'guests': contacts})


@login_required
def search_realname(request):
    username = request.session.get('user', '')
    search_realname = request.GET.get("realname", "")
    # 注意这里需要将过滤器的名称也修改为realname__contains
    guest_list = Guest.objects.filter(realname__contains=search_realname)
    return render(request, "guest_manage.html", {"user": username,
                                                 "guests": guest_list})


@login_required
def sign_index(request, eid):
    event = get_object_or_404(Event, id=eid)
    guest_num = len(get_list_or_404(Guest, event=event))
    guest_sign_num = Guest.objects.filter(event=event, sign=1).count()
    username = request.session.get('user', '')
    return render(request, 'sign_index.html', {'user': username,
                                               'event': event,
                                               'guest_num': guest_num,
                                               'guest_sign_num': guest_sign_num,
                                               })



@login_required
def sign_index_action(request, eid):
    username = request.session.get('user', '')
    event = get_object_or_404(Event, id=eid)
    guest_num = Guest.objects.filter(event_id=eid).count()
    guest_sign_num = Guest.objects.filter(event_id=eid, sign=1).count()
    phone = request.POST.get('phone', '')
    print(phone)
    result = Guest.objects.filter(phone=phone)  # 根据用户输入的手机号查询在Guest表中的记录
    if not result:  # 如果用户输入的手机号在Guest表不存在，则提示用户“phone error.”
        return render(request, 'sign_index.html', {'event': event,
                                                   'user': username,
                                                   'hint': 'phone error.',
                                                   'guest_num': guest_num,
                                                   'guest_sign_num': guest_sign_num,
                                                   })
    result = Guest.objects.filter(phone=phone,
                                  event_id=eid)  # 通过用户输入的手机号和对应的发布会id查找Guest表，则说明手机号与发布会不匹配，提示用户“event id or phone error.”
    if not result:
        return render(request, 'sign_index.html', {'event': event,
                                                   'user': username,
                                                   'hint': 'event id or phone error.',
                                                   'guest_num': guest_num,
                                                   'guest_sign_num': guest_sign_num,
                                                   })
    result = Guest.objects.get(phone=phone, event_id=eid)  # 还是通过用户输入的手机号和发布会id获取数据对象
    if result.sign:  # 从数据对象中获取sign字段的值，如果为真（1），则说明嘉宾已经签到过了，提示用户“user has sign in.”
        return render(request, 'sign_index.html', {'event': event,
                                                   'user': username,
                                                   'hint': '%s has sign in.' % username,
                                                   'guest_num': guest_num,
                                                   'guest_sign_num': guest_sign_num,
                                                   })
    else:  # 否则，说明嘉宾未签到，修改签到状态为1并提示用户“sign in success”，同时显示嘉宾的姓名和手机号
        Guest.objects.filter(phone=phone, event_id=eid).update(sign='1')
        return render(request, 'sign_index.html', {'event': event,
                                                   'user': username,
                                                   'hint': 'sign in success!',
                                                   'guest': result,
                                                   'guest_num': guest_num,
                                                   'guest_sign_num': guest_sign_num,
                                                   })


@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response
