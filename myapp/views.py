import random

from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import *


# ------------------- admin

def login(req):
    return render(req,"Login.html")

def login_post(req):
    usname=req.POST['username']
    pas=req.POST['password']
    print(usname,pas)
    check=Login.objects.filter(username=usname,password=pas)
    if check:
        get1=Login.objects.get(username=usname,password=pas)
        req.session['lid']=get1.id
        if get1.type == "admin":
            return HttpResponse("<script>alert('success');window.location='/myapp/adminHome/'</script>")
        elif get1.type == "investigator":
            return HttpResponse("<script>alert('success');window.location='/myapp/InvestigatorHome/'</script>")
        else:
            return HttpResponse("<script>alert('no type');window.location='/myapp/login/'</script>")
    else:
        return HttpResponse("<script>alert('no type');window.location='/myapp/login/'</script>")

def adminHome(req):
    if not req.session['lid']:
        return render(req,'Login.html')
    else:
        return render(req,'Admin/Admin_Home.html')

def ChangePassword(req):
    return render(req,"Admin/admin_ChangePassword.html")

def ChangePassword_post(req):
    olp=req.POST['olp']
    newp=req.POST['newp']
    confirmp=req.POST['cp']
    c=Login.objects.filter(id=req.session['lid'],password=olp)
    if c.exists():
        if newp==confirmp:
            Login.objects.filter(id=req.session['lid'],password=olp).update(password=confirmp)
            return HttpResponse("<script>alert('change password success');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse("<script>alert('not done');window.location='/myapp/ChangePassword/'</script>")
    else:
        return HttpResponse("<script>alert('not done');window.location='/myapp/ChangePassword/'</script>")


def Add_Investigator(request):
    return render(request, "Admin/Add_Investigator.html")

def Add_Investigator_post(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    qualification = request.POST['qualification']
    place = request.POST['place']
    city = request.POST['city']
    pin = request.POST['pin']
    adharno = request.POST['adharno']
    photo = request.FILES['photo']
    print(name)

    lg = Login()
    lg.username = email
    lg.password = random.randint(000, 999)
    lg.type = "investigator"
    lg.save()


    date=datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
    fs=FileSystemStorage()
    fs.save(date,photo)


    bb= Investigator()


    bb.name = name
    print(bb.name)
    bb.email = email
    bb.phone = phone
    bb.qualification = qualification
    bb.place = place
    bb.city = city
    bb.pin = pin
    bb.adharno = adharno
    bb.photo = fs.url(date)
    bb.LOGIN = lg
    bb.save()
    return HttpResponse("<script>alert('Add investigator done');window.location='/myapp/adminHome/'</script>")

def View_Investigator(req):
    data=Investigator.objects.all()
    return render(req,"Admin/View_investigator.html",{"investigators":data})

def View_Investigator_post(req):
    name=req.POST['name']
    data=Investigator.objects.filter(name__icontains=name)
    return render(req,"Admin/View_investigator.html",{"investigators":data})

def Edit_Investigator(req,id):
    data=Investigator.objects.get(id=id)
    return render(req,"Admin/Edit_Investigator.html",{"data":data})

def Edit_Investigator_post(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    qualification = request.POST['qualification']
    place = request.POST['place']
    city = request.POST['city']
    pin = request.POST['pin']
    adharno = request.POST['adharno']
    iid=request.POST['iid']

    data = Investigator.objects.get(id=iid)
    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, photo)
        data.photo=fs.url(date)
        data.save()
    data.name = name
    data.email = email
    data.phone = phone
    data.qualification = qualification
    data.place = place
    data.city = city
    data.pin = pin
    data.adharno = adharno
    data.save()
    return HttpResponse("<script>alert('done');window.location='/myapp/View_Investigator/'</script>")

def delete_Investigator(req,id):
    Investigator.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/myapp/View_Investigator/'</script>")

def View_Case(req):
    data=Case.objects.all()
    print(data)
    return render(req,"Admin/View_Case.html",{"data":data})

def View_Case_post(req):
    fromt=req.POST['fromt']
    to=req.POST['toid']
    data=Case.objects.filter(date_range=[fromt,to])
    return render(req,"Admin/View_Case.html",{"data":data})

def View_Evidane(req):
    data=Evidance.objects.all()
    return render(req,"Admin/View_evidance.html",{"data":data})

def View_Evidance_post(req):
    fromt=req.POST['fromt']
    to=req.POST['toid']
    data=Case.objects.filter(date_range=[fromt,to])
    return render(req,"Admin/View_evidance.html",{"data":data})

def View_Users(req):
    data=User.objects.all()
    return render(req,"Admin/View_users.html",{"users":data})

def View_Users_post(req):
    name=req.POST['fromt']
    data=User.objects.filter(name__icontains=name)
    return render(req,"Admin/View_users.html",{"data":data})

def View_complaints(req):
    data=Complaint.objects.all()
    return render(req,"Admin/View_Complaints.html",{"data":data})

def View_complaints_post(req):
    fromt = req.POST['fromt']
    to = req.POST['toid']
    data = Complaint.objects.filter(date_range=[fromt,to])
    return render(req, "Admin/View_Complaints.html", {"data": data})


def send_reply_get(req,id):
    return  render(req,"Admin/Send_reply.html",{"id":id})


def SendReply_post(req):
    id=req.POST['id']
    reply=req.POST['reply']
    Complaint.objects.filter(id=id).update(reply=reply,status="replied")
    return HttpResponse("<script>alert('success');window.location='/myapp/adminHome/'</script>")


def View_Feedback(req):
    data=Feedback.objects.all()
    return render(req, "Admin/View_feedback.html", {"data": data})

def View_Feedback_post(req):
    fromt = req.POST['fromt']
    to = req.POST['toid']
    data = Feedback.objects.filter(date_range=[fromt,to])
    return render(req, "Admin/View_feedback.html", {"data": data})

def Logout(req):
    req.session['lid'] = ''
    return HttpResponse("<script>alert('success');window.location='/myapp/login/'</script>")



# --------------------------- Investigator -------------------------


def InvestigatorHome(req):
    return render(req,"Investigator/InvestigatorHome.html")

def Investigator_Profile(req):
    data=Investigator.objects.get(LOGIN_id=req.session['lid'])
    return render(req, "Investigator/View_Profile.html", {"investigator": data})


def ADD_Case_get(req):
    data=Investigator.objects.all()
    return render(req,"Investigator/Add_Case.html",{"data":data})

def ADD_Case_Post(request):
    crime_type = request.POST['crime_type']
    summary = request.POST['summary']
    narration = request.POST['narration']
    date_reported = request.POST['date_reported']
    date_occured = request.POST['date_occured']
    place = request.POST['place']
    city = request.POST['city']
    pin = request.POST['pin']
    post = request.POST['post']
    district = request.POST['district']
    state = request.POST['state']
    country = request.POST['country']
    description = request.POST['description']
    status = request.POST['status']
    arrest = request.POST['arrest']
    charges = request.POST['charges']
    conviction = request.POST['conviction']
    stolen_items = request.POST['stolen_items']
    file = request.FILES['file']
    fir = request.FILES['fir']

    Vors=request.POST['Vors']

    date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".pdf"
    fs = FileSystemStorage()
    fs.save(date, file)

    date1 = datetime.now().strftime("%Y%m%d-%H%M%S") + ".pdf"
    fs1 = FileSystemStorage()
    fs1.save(date, fir)

    # Create a new case instance
    case = Case()
    case.crime_type=crime_type
    case.summary=summary
    case.narration=narration
    case.date_reported=date_reported
    case.date_occured=date_occured
    case.place=place
    case.city=city
    case.pin=pin
    case.post=post
    case.district=district
    case.state=state
    case.country=country
    case.description=description
    case.status=status
    case.arrest=arrest
    case.charges=charges
    case.conviction=conviction
    case.stolen_items=stolen_items
    case.file=fs.url(date)
    case.fir=fs1.url(date1)
    case.INVESTIGATOR=Investigator.objects.get(LOGIN_id=request.session['lid'])
    case.save()

    if Vors == "Yes":
        request.session['caseid']=case.id
        c=request.session['caseid']
        return render(request,"Investigator/Add_Victim_or_Sus.html",{"caseid":c})
    else:
        return HttpResponse("<script>alert('Case added success');window.location='/myapp/InvestigatorHome/'</script>")

def Add_Victim_or_sus_post(req):
    name=req.POST['name']
    email=req.POST['email']
    place=req.POST['place']
    city=req.POST['city']
    pin=req.POST['pin']
    adharno=req.POST['adharno']
    photo=req.FILES['photo']
    type=req.POST['type']
    cid=req.POST['cid']
    btn=req.POST['btn1']

    date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, photo)

    data=victim_or_suspect()
    data.name=name
    data.email=email
    data.place=place
    data.city=city
    data.pin=pin
    data.adharno=adharno
    data.photo=fs.url(date)
    data.type=type
    data.CASE_id=cid
    data.save()
    if btn == "Add":
        return HttpResponse("<script>alert('Victim added success');window.location='/myapp/InvestigatorHome/'</script>")
    else:
        return render(req,"Investigator/Add_Victim_or_Sus.html",{"caseid":cid})


def View_Victim(req,id):
    data=victim_or_suspect.objects.filter(CASE_id=id,type="victim")
    return render(req,"Investigator/View_Victim_or_suspect.html",{"data":data})

def View_Suspect(req,id):
    data=victim_or_suspect.objects.filter(CASE_id=id,type="suspect")
    return render(req,"Investigator/View_Victim_or_suspect.html",{"data":data})

def Investigator_View_Case(req):
    data=Case.objects.filter(INVESTIGATOR__LOGIN_id=req.session['lid'])
    return render(req,"Investigator/View_case.html",{"data":data})

def Investigator_View_Case_post(req):
    return render(req,"Investigator/View_case.html")

def Edit_Case_get(req,id):
    data=Case.objects.get(id=id)
    return render(req,"Investigator/Edit_case.html",{"data":data})

def Edit_Case_post(request):
    crime_type = request.POST['crime_type']
    summary = request.POST['summary']
    narration = request.POST['narration']
    date_reported = request.POST['date_reported']
    date_occured = request.POST['date_occured']
    place = request.POST['place']
    city = request.POST['city']
    pin = request.POST['pin']
    post = request.POST['post']
    district = request.POST['district']
    state = request.POST['state']
    country = request.POST['country']
    description = request.POST['description']
    status = request.POST['status']
    arrest = request.POST['arrest']
    charges = request.POST['charges']
    conviction = request.POST['conviction']
    stolen_items = request.POST['stolen_items']
    fir = request.POST['fir']
    id=request.POST['id']

    case = Case.objects.get(id=id)

    if 'file' in request.FILES:
        file = request.FILES['file']
        date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, file)
        case.photo=fs.url(date)
        case.save()

    case.crime_type=crime_type,
    case.summary=summary,
    case.narration=narration,
    case.date_reported=date_reported,
    case.date_occured=date_occured,
    case.place=place,
    case.city=city,
    case.pin=pin,
    case.post=post,
    case.district=district,
    case.state=state,
    case.country=country,
    case.description=description,
    case.status=status,
    case.arrest=arrest,
    case.charges=charges,
    case.conviction=conviction,
    case.stolen_items=stolen_items,
    case.fir=fir,
    case.investigator_id=Investigator.objects.get(LOGIN_id=request.session['lid'])
    case.save()
    return HttpResponse("<script>alert('success');window.location='/myapp/login/'</script>")

def Delete_Case(req,id):
    Case.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('success');window.location='/myapp/login/'</script>")


def Investigator_Add_Evidance(req):
    return render(req,"Investigator/Add_Eviedence.html")


def Investigator_Add_Evidance_post(request):
    type = request.POST['type']
    description = request.POST['description']
    date_collected = request.POST['date_collected']
    collected_by = request.POST['collected_by']
    place = request.POST['place']
    place = request.POST['place']
    land_mark = request.POST['land_mark']
    storage_location = request.POST['storage_location']
    filename = request.POST['filename']
    import json
    from web3 import Web3, HTTPProvider
    blockchain_address = 'http://127.0.0.1:7545'
    web3 = Web3(HTTPProvider(blockchain_address))
    web3.eth.defaultAccount = web3.eth.accounts[0]

    compiled_contract_path = 'D:\\GURUDEVA EVOTING\\Evoting\\project\\build\\contracts\\Evoting.json'
    deployed_contract_address = web3.eth.accounts[5]

    cand_id = request.POST['candid']
    uid = request.POST['lid']


    from datetime import datetime
    date = datetime.now().strftime('%Y-%m-%d')
    time = datetime.now().strftime('%H:%M:%S')
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    vote = contract.functions.addvote(int(cand_id), int(uid), str(date), str(time)).transact()

    return JsonResponse({'status': 'ok'})


def Investigator_Edit_Evidance(req):
    return render(req,"Investigator/Edit_evidance.html")

def Investigator_Edit_Evidance_post(request):
    type = request.POST['type']
    description = request.POST['description']
    date_collected = request.POST['date_collected']
    collected_by = request.POST['collected_by']
    place = request.POST['place']
    place = request.POST['place']
    land_mark = request.POST['land_mark']
    storage_location = request.POST['storage_location']
    filename = request.POST['filename']

    return HttpResponse('''<script>alert("done");window.location="/myapp//"''')

def inves_View_Users(request):
    data=User.objects.all()
    return render(request,"Investigator/View_Users.html",{"data":data})




def View_Complaint_Users(request):
    data=Complaint.objects.filter(status="pending")
    return render(request,"Investigator/View_User_Complaint.html",{"complaints":data})

def View_complaints_Users_post(req):
    fromt = req.POST['fromt']
    to = req.POST['toid']
    data = Complaint.objects.filter(date_range=[fromt,to])
    return render(req, "Investigator/View_User_Complaint.html", {"complaints": data})

def accept_complaint(req,id):
    Complaint.objects.filter(id=id).update(status="accepted")
    return HttpResponse('''<script>alert("accepted");window.location="/myapp/InvestigatorHome/"</script>''')

def reject_complaint(req,id):
    Complaint.objects.filter(id=id).update(status="rejected")
    return HttpResponse('''<script>alert("rejected");window.location="/myapp/InvestigatorHome/"</script>''')



def View_Approved_Complaint_Users(request):
    data=Complaint.objects.filter(status="accepted")
    l=[]
    for i in data:
        value=""
        ac=Action.objects.filter(COMPLAINT_id=i.id)
        if ac.exists():
            value="yes"
            l.append({"id":i.id,
                      "user":i.USER.name,
                      "date_reported":i.date_reported,
                      "date_occured":i.date_occured,
                      "place":i.place,
                      "city":i.city,
                      "pin":i.pin,
                      "post":i.post,
                      "district":i.district,
                      "state":i.state,
                      "country":i.country,
                      "description":i.description,
                      "complaint":i.complaint,
                      "status":i.status,
                      "value":value
                      })
        else:
            value = "no"
            l.append({"id": i.id,
                      "user": i.USER.name,
                      "date_reported": i.date_reported,
                      "date_occured": i.date_occured,
                      "place": i.place,
                      "city": i.city,
                      "pin": i.pin,
                      "post": i.post,
                      "district": i.district,
                      "state": i.state,
                      "country": i.country,
                      "description": i.description,
                      "complaint": i.complaint,
                      "status": i.status,
                      "value": value
                      })
    return render(request, "Investigator/View_Approved_complaint.html", {"data":l})

def View_Approved_Complaint_Users_post(req):
    fromt = req.POST['fromt']
    to = req.POST['toid']
    data = Complaint.objects.filter(date_range=[fromt,to])
    return render(req, "Investigator/View_Approved_complaint.html", {"complaints": data})

def View_Rejected_Complaint_Users(request):
    data=Complaint.objects.filter(status="rejected")
    return render(request, "Investigator/View_Approved_complaint.html", {"complaints":data})


def View_Rejected_Complaint_Users_post(req):
    fromt = req.POST['fromt']
    to = req.POST['toid']
    data = Complaint.objects.filter(date_range=[fromt,to])
    return render(req, "Investigator/View_Rejected_Complaint.html", {"complaints": data})

def Take_Action_get(req,id):
    return render(req,"Investigator/Take_Action.html",{"id":id})

def Take_Action_Post(req):
    cid=req.POST['cid']
    action=req.POST['action']
    data=Action()
    data.date=datetime.now().today()
    data.action=action
    data.COMPLAINT_id=cid
    data.INVESTIGATOR=Investigator.objects.get(LOGIN_id=req.session['lid'])
    data.save()
    return HttpResponse('''<script>alert("done");window.location="/myapp/View_Approved_Complaint_Users/"</script>''')


def View_Action(req,id):
    data=Action.objects.filter(COMPLAINT_id=id)
    return render(req,"Investigator/View_Action.html",{"data":data})



def Edit_Action_get(req,id):
    data=Action.objects.get(COMPLAINT_id=id)
    return render(req,"Investigator/Edit_Action.html",{"data":data})

def Edit_Action_post(req):
    # cid = req.POST['cid']
    action = req.POST['action']
    aid=req.POST['aid']

    data = Action.objects.get(id=aid)
    data.date = datetime.now().today()
    data.action = action
    # data.COMPLAINT_id = cid
    # data.INVESTIGATOR = Investigator.objects.get(LOGIN_id=req.session['lid'])
    data.save()
    return HttpResponse('''<script>alert("done");window.location="/myapp/View_Approved_Complaint_Users/"</script>''')



def delete_action(req,id):
    Action.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert("deleted");window.location="/myapp/View_Approved_Complaint_Users/"</script>''')



def chat1(request, id):
    if request.session['lid']!='':
        request.session["userid"] = id
        cid = str(request.session["userid"])
        request.session["new"] = cid
        qry = User.objects.get(LOGIN=cid)

        return render(request, "Investigator/Chat.html", {'photo': qry.photo, 'name': qry.name, 'toid': cid})
    else:
        return HttpResponse('''<script>alert('You are not Logined');window.location='/myapp/login/'</script>''')


def chat_view(request):
    if request.session['lid']!='':
        fromid = request.session["lid"]
        toid = request.session["userid"]
        qry = User.objects.get(LOGIN=request.session["userid"])
        from django.db.models import Q

        res = Chat.objects.filter(Q(FROM_ID_id=fromid, TO_ID_id=toid) | Q(FROM_ID_id=toid, TO_ID_id=fromid))
        l = []

        for i in res:
            l.append({"id": i.id, "message": i.chat, "to": i.TO_ID_id, "date": i.date, "from": i.FROM_ID_id})

        return JsonResponse({'photo': qry.photo, "data": l, 'name': qry.name, 'toid': request.session["userid"]})
    else:
        return HttpResponse('''<script>alert('You are not Logined');window.location='/myapp/login/'</script>''')


def chat_send(request, msg):
    if request.session['lid']!='':
        lid = request.session["lid"]
        toid = request.session["userid"]
        message = msg

        import datetime
        d = datetime.datetime.now().date()
        chatobt = Chat()
        chatobt.chat = message
        chatobt.TO_ID_id = toid
        chatobt.FROM_ID_id = lid
        chatobt.date = d
        chatobt.time=datetime.datetime.now().time()
        chatobt.save()
    else:
        return HttpResponse('''<script>alert('You are not Logined');window.location='/myapp/login/'</script>''')

    return JsonResponse({"status": "ok"})



def Investigator_ChangePassword(req):
    return render(req,"Investigator/Change_Password.html")

def Investigator_ChangePassword_post(req):
    olp=req.POST['olp']
    newp=req.POST['newp']
    confirmp=req.POST['cp']
    c=Login.objects.filter(id=req.session['lid'],password=olp)
    if c.exists():
        if newp==confirmp:
            Login.objects.filter(id=req.session['lid'],password=olp).update(password=confirmp)
            return HttpResponse("<script>alert('change password success');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse("<script>alert('not done');window.location='/myapp/ChangePassword/'</script>")
    else:
        return HttpResponse("<script>alert('not done');window.location='/myapp/ChangePassword/'</script>")


# def Investigator_View_Complaints(req,id):
#     data=casecomplaint.objects.filter(CASE_id=id)
#     return render(req,"Investigator/View_Approved_complaint.html",{"data":data})
#
#










#===========================  user   ================


def user_signup(req):
    name = req.POST["name"]
    pin=req.POST['pin']
    place=req.POST['place']
    email = req.POST["email"]
    adharno=req.POST['adharno']
    city=req.POST['city']
    phone = req.POST["phone"]
    cpwd = req.POST["cpwd"]
    photo = req.POST["photo"]

    import base64
    date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    abc = base64.b64decode(photo)
    # fs=open("C:\\Users\\aquib\\Downloads\\MentApp1\\MentApp\\media\\user\\" + date,"wb")
    fs=open("C:\\Users\\kashy\\PycharmProjects\\evidanceprotection\\media\\user\\" + date,"wb")



    # fs=open("C:\\Users\\hp\\PycharmProjects\\NSSManagementSystem\\media\\student\\"+date,"wb")
    photopath = '/media/user/' + date
    fs.write(abc)
    fs.close()

    login = Login()
    login.username = email
    login.password = cpwd
    login.type = "user"
    login.save()

    st = User()
    st.name = name
    st.pin = pin
    st.place=place
    st.email=email
    st.adharno=adharno
    # st.country=country
    st.city=city
    st.phone=phone
    # st.email=email
    st.LOGIN=login
    st.photo=photopath
    st.save()
    return JsonResponse({"status": "ok"})


def user_edit_profile(req):
    name = req.POST["name"]
    pin=req.POST['pin']
    place=req.POST['place']
    email = req.POST["email"]
    adharno=req.POST['adharno']
    city=req.POST['city']
    phone = req.POST["phone"]
    photo = req.POST["photo"]
    lid=req.POST['lid']
    print(lid)

    st = User.objects.get(LOGIN_id=lid)

    if len(photo)>0:
        import base64
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        abc = base64.b64decode(photo)
        # fs=open("C:\\Users\\aquib\\Downloads\\MentApp1\\MentApp\\media\\user\\" + date,"wb")
        fs=open("C:\\Users\\kashy\\PycharmProjects\\evidanceprotection\\media\\user\\" + date,"wb")
        photopath = '/media/user/' + date
        fs.write(abc)
        fs.close()
        st.photo = photopath
        st.save()

    # fs=open("C:\\Users\\hp\\PycharmProjects\\NSSManagementSystem\\media\\student\\"+date,"wb")

    st.name = name
    st.pin = pin
    st.place=place
    st.email=email
    st.adharno=adharno
    # st.country=country
    st.city=city
    st.phone=phone
    # st.email=email
    st.save()
    return JsonResponse({"status": "ok"})

def user_login(req):
    name = req.POST['username']
    password = req.POST['password']
    print(name, password)
    lg = Login.objects.filter(username=name, password=password)
    if lg.exists():
        lg2 = Login.objects.get(username=name, password=password)
        lid = lg2.id
        if lg2.type == "user":
            print('ok')
            return JsonResponse({"status": "ok", "lid": str(lid)})
        else:
            return JsonResponse({"status": "no"})
    else:
        return JsonResponse({"status": "no"})



def user_view_profile(request):
    lid = request.POST['lid']
    res = User.objects.get(LOGIN_id=lid)
    return JsonResponse(
        {'status': "ok",
         'name': res.name,
         'place': res.place,
         'photo': res.photo,
         'city': res.city,
         # 'country': res.country,
         'pin': res.pin,
         'adharno': res.adharno,
         # 'state': res.state,
         # 'gender': res.gender,
         'phone': res.phone,
         'email':res.email,
         })


def user_view_investigator(req):
    lid=req.POST['lid']
    I=Investigator.objects.all()
    print(I)
    Inv=[]
    for i in I:
        Inv.append({
                     "id":i.id,
                    "lid":i.LOGIN_id,
                     "name":i.name,
                     "email":i.email,
                     "phone":i.phone,
                     "qualification":i.qualification,
                     "place":i.place,
                     "city":i.city,
                     "pin":i.pin,
                     "adharno":i.adharno,
                     "photo":i.photo,
                     })
    print(Inv)
    return JsonResponse({"status":"ok","data":Inv})


def view_case(req):
    Invid=req.POST['iid']
    case=Case.objects.filter(INVESTIGATOR_id=Invid)
    l=[]
    for i in case:
        l.append({
            "id": i.id,
            "crime_type": i.crime_type,
            "summary": i.summary,
            "narration": i.narration,
            "date_reported": i.date_reported,
            "date_occured": i.date_occured,
            "place": i.place,
            "city": i.city,
            "pin": i.pin,
            "post": i.post,
            "district": i.district,
            "state": i.state,
            "country": i.country,
            "description": i.description,
            "status": i.status,
            "arrest": i.arrest,
            "charges": i.charges,
            "conviction": i.conviction,
            "stolen_items": i.stolen_items,
            "file": i.file,
            "fir": i.fir,
            "investigator": i.INVESTIGATOR.name,
        })

    return JsonResponse({"status": "ok", "data": l})



def view_evidance(req):
    return JsonResponse({"status":"ok"})


def send_own_complaint(req):
    complaint=req.POST['complaint']
    date_occured=req.POST['date_occured']
    place=req.POST['place']
    city=req.POST['city']
    pin=req.POST['pin']
    post=req.POST['post']
    district=req.POST['district']
    state=req.POST['state']
    country=req.POST['country']
    description=req.POST['description']
    lid=req.POST['lid']

    c=Complaint()
    c.complaint=complaint
    c.USER = User.objects.get(LOGIN_id=lid)
    c.date_reported=datetime.now().today()
    c.date_occured=date_occured
    c.place=place
    c.city=city
    c.pin=pin
    c.post=post
    c.district=district
    c.state=state
    c.country=country
    c.description=description
    c.status="pending"
    c.save()
    return JsonResponse({"status":"ok"})



def view_complaint(req):
    lid=req.POST['lid']
    data=Complaint.objects.filter(USER__LOGIN_id=lid)
    l = []
    for i in data:
        l.append({
            "id": i.id,
            "complaint": i.complaint,
            "date_reported": i.date_reported,
            "date_occured": i.date_occured,
            "place": i.place,
            "city": i.city,
            "pin": i.pin,
            "post": i.post,
            "district": i.district,
            "state": i.state,
            "country": i.country,
            "description": i.description,
            "status": i.status,
        })
    return JsonResponse({"status": "ok", "data": l})



def send_feedback(req):
    feedback=req.POST['feedback']
    lid=req.POST['lid']
    c=Feedback()
    c.feedback=feedback
    c.date=datetime.now().today()
    c.USER=User.objects.get(LOGIN_id=lid)
    c.save()
    return JsonResponse({"status":"ok"})



def view_action(req):
    cid=req.POST['cid']
    data=Action.objects.filter(COMPLAINT_id=cid)
    l=[]
    for i in data:
        l.append({
            "id":i.id,
            "action":i.action,
            "date":i.date,
            "investigator":i.INVESTIGATOR.name,
        })
    return JsonResponse({"status":"ok","data":l})


def change_password(req):
    olp = req.POST['olp']
    newp = req.POST['newp']
    confirmp = req.POST['cp']
    c = Login.objects.filter(id=req.session['lid'], password=olp)
    if c.exists():
        if newp == confirmp:
            Login.objects.filter(id=req.session['lid'], password=olp).update(password=confirmp)
            return JsonResponse({"status": "no"})
        else:
            return JsonResponse({"status": "no"})
    else:
        return JsonResponse({"status": "no"})


def chat_send_by_user(request):
    FROM_id=request.POST['from_id']
    TO_id=request.POST['to_id']
    msg=request.POST['message']

    print(FROM_id,TO_id,msg)

    from  datetime import datetime
    c=Chat()
    c.FROM_id=FROM_id
    c.TO_id=TO_id
    c.Chat=msg
    c.date=datetime.now().date()
    c.save()
    return JsonResponse({'status':"ok"})



def chat_view_and(request):
    from_id=request.POST['from_id']
    to_id=request.POST['to_id']
    print(from_id,to_id)
    l=[]
    data1=Chat.objects.filter(FROM_id=from_id,TO_id=to_id).order_by('id')
    data2=Chat.objects.filter(FROM_id=to_id,TO_id=from_id).order_by('id')

    data= data1 | data2
    print(data)

    for res in data:
        l.append({'id':res.id,'from':res.FROM.id,'to':res.TO.id,'msg':res.Chat,'date':res.date})

    print(l)
    return JsonResponse({'status':"ok",'data':l})




# def send_case_complaint(req):
#     caseid=req.POST['caseid']
#     complaint=req.POST['complaint']
#     lid=req.POST['lid']
#     data=casecomplaint()
#     data.CASE_id=caseid
#     data.USER=User.objects.get(LOGIN_id=lid)
#     data.complaint=complaint
#     data.date=datetime.now().today()
#     data.save()
#     return JsonResponse({"status":"ok"})
#







