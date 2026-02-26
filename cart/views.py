from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from medicines.models import Medicine
from .models import Cart, CartItem


@login_required
def add_to_cart(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, item_created = CartItem.objects.get_or_create(
        cart=cart,
        medicine=medicine
    )

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')


@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/view_cart.html', {'cart': cart})


@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(CartItem, pk=pk)
    item.delete()
    return redirect('view_cart')