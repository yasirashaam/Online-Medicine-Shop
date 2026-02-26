from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem
from .models import Order, OrderItem

@login_required
def place_order(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    if not cart.items.exists():
        return redirect('home')  # No items in cart

    total = sum(item.subtotal() for item in cart.items.all())
    order = Order.objects.create(user=request.user, total_price=total)

    for item in cart.items.all():
        OrderItem.objects.create(
            order=order,
            medicine=item.medicine,
            quantity=item.quantity,
            price=item.medicine.price
        )
        # Reduce stock
        item.medicine.stock_quantity -= item.quantity
        item.medicine.save()

    # Clear cart
    cart.items.all().delete()

    return redirect('order_success', order_id=order.id)


@login_required
def order_success(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/order_success.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})