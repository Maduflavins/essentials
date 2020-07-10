from django.shortcuts import render
from django.shortcuts import render
from .models import OrderItem
from .forms import OrederCreateForm
from cart.cart import Cart

# Create your views here.

def order_create(request):
    cart = cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],price=item['price'],
                quantity=item['quantity'])

            #clear the cart
            cart.clear()
            return render(request, 'orders/order/created.htnl', {'order': order})

    else:
        form = OrederCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
