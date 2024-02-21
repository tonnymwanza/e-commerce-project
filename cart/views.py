from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from . forms import CartItemsForm
from . forms import UserForm
from . forms import ProfileForm
from django.contrib import messages
from . models import CartItem, Product
from django.contrib.auth.decorators import login_required
import random
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)

@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

@login_required(login_url='login')
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')

@login_required(login_url='login')
def checkout(request):
    cart = CartItem.objects.all()
    form = CartItemsForm()
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    if request.method == 'POST':
        form = CartItemsForm(request.POST or None)
        if form.is_valid():
            obj = CartItem.objects.create(
                firstname = form.cleaned_data.get('firstname'),
                lastname = form.cleaned_data.get('lastname'),
                phone_number = form.cleaned_data.get('phone_number'),
                email = form.cleaned_data.get('email'),
                address1 = form.cleaned_data.get('address1'),
                address2 = form.cleaned_data.get('address2'),
                city = form.cleaned_data.get('city'),
                country = form.cleaned_data.get('country'),
                postal_code = form.cleaned_data.get('postal_code')
            )
            return redirect('confirmation')
        else:
            # forms = forms.errors
            messages.error(request, 'problem encountered try again')
    context = {
        'form': form,
        'cart': cart,
        'total_price': total_price
        }
    return render(request, 'checkout.html', context)

@login_required(login_url='login')
def profile(request):
    profileform = ProfileForm(instance=request.user)
    userform = UserForm(instance=request.user)
    if request.method == 'POST':
        profileform = ProfileForm(data=request.POST, instance=request.user)
        userform = UserForm(data=request.POST, instance=request.user)
        if profileform.is_valid() and userform.is_valid():
            profileform.save()
            userform.save()
            messages.success(request, 'profile updated successfully')
        else:
            messages.error(request, 'error encountered during profile updating')
    context = {
        'profileform': profileform,
        'userform': userform
    }
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def confirmation(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    cart = CartItem.objects.all()
    random_no = random.randrange(10000, 1000000)
    context = {
        'total_price': total_price,
        'cart': cart,
        'cart_items': cart_items,
        'random_no': random_no,

    }
    return render(request, 'confirmation.html', context)