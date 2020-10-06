from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import Product,Contact
# Create your views here.
# def index (request):
#     products=Product.objects.all()
#     n=len(products)
#     nslides=n//4+ceil((n//4)-(n//4))
#     params={'no_of_slides':nslides,'range':range(nslides),'product':products}
#     return render(request,"index.html",params)
def index (request):
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={items['category'] for items in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nslides=n//4+ceil((n//4)-(n//4))
        allProds.append([prod,range(1,nslides),nslides])
    params={'allProds':allProds}
    return render(request,"index.html",params)


def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)


    return render(request, 'prodView.html', {'product':product[0]})


def about (request):
    return render(request, "about.html")
def contact(request):
    thank=False
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        msg=request.POST.get('msg','')
        contact=Contact(name=name,email=email,phone=phone,msg=msg)
        contact.save()
        thank=True
    return render(request,"contact.html",{'thank':thank})

def searchmatch(query,item):
    if query in item.desc.lower() or query in item.product_name.lower():
        return True
    else:
        return False

def search (request):
    query=request.GET.get('search')
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={items['category'] for items in catprods}
    for cat in cats:
        prodtmp=Product.objects.filter(category=cat)
        prod=[item for item in prodtmp if searchmatch(query,item)]
        n = len(prod)
        nslides=n//4+ceil((n//4)-(n//4))
        if len(prod)!=0:
            allProds.append([prod,range(1,nslides),nslides])
            params={'allProds':allProds,'msg':""}
        if len(allProds)==0 or len(query)<4:
            params={'msg':'Please enter valid text'}
    return render(request,"search.html",params)