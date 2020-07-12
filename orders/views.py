from django.shortcuts import render
from django.shortcuts import render
from .models import OrderItem
from .forms import OrederCreateForm
from cart.cart import Cart
from django.urls import reverse
from django.shortcuts import render, redirect
from .tasks import order_created

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
            #Implement celery asynchronous sending of emails
            #launch asynchronous task
            order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            #redirect for payment

            return redirect(reverse('payment:process'))

    else:
        form = OrederCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})