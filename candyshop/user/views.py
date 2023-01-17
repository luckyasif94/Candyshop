from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from user.models import Product, Review, Orders


def index(request):
    pro = Product.objects.all() #select * from table
    context = {'pro':pro}
    return render(request,"index.html",context)


def productDetails(request,id):
    pro = Product.objects.get(id=id)  # select * from exam where id =id
    rev = Review.objects.filter(product_id=id)
    return render(request, 'detail.html', {'pro': pro,'rev': rev})


def reviewProcess(request,proid):
    review = request.POST.get('review')
    name = request.POST.get('name')
    email = request.POST.get('email')

    pro = Product.objects.get(id=proid)

    r = Review()
    r.review = review
    r.name = name
    r.email = email
    r.product = pro
    r.save()
    return HttpResponse("<script>alert('Thanks for the review!!!!');window.location='/details/"+str(proid)+"';</script>")


def checkout(request,proid):
    pro = Product.objects.get(id=proid)
    total = pro.price + 40
    return render(request, "checkout.html",{'pro': pro,'total': total})


def checkoutProcess(request,proid):
    firstname = request.POST.get('fname')
    lastname = request.POST.get('lname')
    email = request.POST.get('email')
    mobile = request.POST.get('mobile')
    address1 = request.POST.get('address1')
    address2 = request.POST.get('address2')
    country = request.POST.get('country')
    city = request.POST.get('city')
    state = request.POST.get('state')
    zip = request.POST.get('zip')

    pro = Product.objects.get(id=proid)

    o = Orders()
    o.firstname = firstname
    o.lastname = lastname
    o.email = email
    o.mobile = mobile
    o.addressline1 = address1
    o.addressline2 = address2
    o.country = country
    o.city = city
    o.state = state
    o.zipcode = zip
    o.product = pro
    o.save()

    return HttpResponse(
        "<script>alert('Order Placed!!!!');window.location='/details/"+str(proid)+"';</script>")