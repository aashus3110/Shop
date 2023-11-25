from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from app.models import Product , Orders , OrderUpdate
import json
from django.core.mail import send_mail
from django.http import HttpResponse



def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    prod = Product.objects.all()
    context = {'prod': prod} 
    return render(request, 'index.html' , context)


def handeLogin(request):
    if request.method == "POST":
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            return render(request, 'Login.html')
    return render(request, 'Login.html')


def handleSignUp(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if len(username) < 6:
            messages.error(
                request, " Your user name must be under 6 characters")
            return redirect('apps')
        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('apps')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('apps')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.save()
        messages.success(
            request, " Your account has been successfully created")
        
        subject = "Thanks for register your site"
        message = "Hello " + myuser.first_name + "!! \n" + \
        "Your email is " + myuser.email + "!! \n" +"Register in our website " \
        "& Your username is " + myuser.username + "!! \n" + \
        "Thank you for visiting our website"
        from_email = 'imking3110@gmail.com'
        to_list = [myuser.email]
        send_mail(
            subject,
            message,
            from_email,
            to_list,
        )
        return redirect('apps')
    else:
        return HttpResponse("404 - Not found")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')



def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'quickview.html', {'product':product[0]})



def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'tracker.html')

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        
        return render(request, 'checkout.html', {'thank':thank, 'id': id})
    return render(request, 'checkout.html')



def search(request):
    query = request.GET['query']
    if len(query)>75:
        allprod = Productobjects.none()
    else:
        allprodprice = Product.objects.filter(price__icontains=query)
        allproddetail = Product.objects.filter(detail__icontains=query)
        allprodname = Product.objects.filter(name__icontains=query)
        allprod = allprodname.union(allproddetail , allprodprice)
    if allprod.count() == 0:
        messages.warning(
            request, "No search results found. Please refine your query")
    params = {'allprod' : allprod, 'query' : query}
    return render(request, 'search.html' , params)
