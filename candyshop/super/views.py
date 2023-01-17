from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from super.models import Login
from user.models import Product, Orders, Review


# Create your views here.
def addproduct(request):
    user = request.session.get('uname')
    if (user == "admin"):
        return render(request,"admin/addproduct.html")
    else:
        return HttpResponse("You are not authorised to view this page")

def addproductProcess(request):
    pname = request.POST.get('n1')
    pprice = request.POST.get('p1')
    pdetails = request.POST.get('d1')
    pstock = request.POST.get('s1')
    pimage1 = request.FILES.get('f11')
    pimage2 = request.FILES .get('f21')

    p = Product()
    p.name = pname
    p.price = pprice
    p.details = pdetails
    p.stock = pstock
    p.image1 = pimage1
    p.image2 = pimage2
    p.save()
    return HttpResponse("<script>alert('successfully added the product');window.location='/admin/addproduct';</script>")

def loginPage(request):
    return render(request,'admin/login.html')

def loginProcess(request):
    uname = request.POST.get('uname')
    pswd = request.POST.get('pass')
    if Login.objects.filter(username=uname, password=pswd).exists():
        loginobj = Login.objects.get(username=uname, password=pswd)
        request.session['uname'] = loginobj.username
        user = loginobj.username

        if (user == "admin"):
            return redirect("products")
        else:
            return HttpResponse("<script>alert('login failed...try again');window.location='/admin/';</script>")

    else:
        return HttpResponse("<script>alert('invalid username and password...try again');window.location='/admin/';</script>")

def products(request):
    user = request.session.get('uname')
    if (user == "admin"):
        pro = Product.objects.all()
        context = {'pro':pro}
        return render(request,'admin/products.html',context)
    else:
        return HttpResponse("You are not authorised to view this page")

def editProduct(request,id):
    user = request.session.get('uname')
    if (user == "admin"):
        edit = Product.objects.get(id = id) #select * from exam where id =id
        return render(request,'admin/editproduct.html',{'edit':edit})
    else:
        return HttpResponse("You are not authorised to view this page")

def deleteProduct(request,id):
    user = request.session.get('uname')
    if (user == "admin"):
        obj = Product.objects.get(id=id)
        obj.delete()
        return HttpResponse("<script>alert('successfully deleted');window.location='/admin/products';</script>")
    else:
        return HttpResponse("You are not authorised to view this page")

def updateProduct(request,id):
    pname = request.POST.get('n1')
    pprice = request.POST.get('p1')
    pdetails = request.POST.get('d1')
    pstock = request.POST.get('s1')
    pimage1 = request.FILES.get('f11')
    pimage2 = request.FILES.get('f21')

    p = Product.objects.get(id=id)
    p.name = pname
    p.price = pprice
    p.details = pdetails
    p.stock = pstock
    p.image1 = pimage1
    p.image2 = pimage2
    p.save()
    return redirect('products')

def viewOrders(request):
    user = request.session.get('uname')
    if (user == "admin"):
        orders = Orders.objects.all()
        context = {'orders':orders}
        return render(request,'admin/orders.html',context)
    else:
        return HttpResponse("You are not authorised to view this page")

def findProduct(request,proid):
    pro = Product.objects.get(id=proid)
    context = {'pro': pro}
    return render(request,'admin/findproduct.html',context)

def approve(request,id,proid):
    o = Orders.objects.get(id=id)
    o.status = "Approved"
    o.save()
    pro = Product.objects.get(id=proid)
    pro.stock = pro.stock - 1
    pro.save()
    return redirect('orders')

def dontapprove(request,id,proid):
    o = Orders.objects.get(id=id)
    o.status = "Not Approved"
    o.save()
    pro = Product.objects.get(id=proid)
    pro.stock = pro.stock + 1
    pro.save()
    return redirect('orders')

def reviews(request):
    user = request.session.get('uname')
    if (user == "admin"):
        rev = Review.objects.all()
        context = {'rev':rev}
        return render(request,'admin/reviews.html',context)
    else:
        return HttpResponse("You are not authorised to view this page")

def logout1(request):
    logout(request)
    return HttpResponse("<script>alert('you are successfully Logged off..');window.location ='/admin/';</script>")