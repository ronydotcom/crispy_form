from django.shortcuts import render, redirect 
from crispy_app.models import*
from crispy_app.forms import*

def home_page(request):
    return render(request, 'home.html')

def product_list(request):
    product_data = ProductModel.objects.all()

    context={
        'product_data': product_data
    }
    return render(request, 'product.html', context)

def add_product(request):
    if request.method=='POST':
        form_data=ProductForm(request.POST,request.FILES)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.total_price=data.product_price*data.qty
            data.save()
            return redirect('product_list')
        
    form_data=ProductForm()
    context={
        'form_data': form_data
    }
    return render(request, 'addproduct.html', context)


def edit_product(request,p_id):
    product_data=ProductModel.objects.get(id=p_id)
    if request.method=='POST':
        form_data=ProductForm(request.POST,request.FILES,instance=product_data)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.total_price=data.product_price*data.qty
            data.save()
            return redirect('product_list')
    form_data=ProductForm(instance=product_data)
    context={
        'form_data': form_data
    }
    return render(request, 'editproduct.html', context)