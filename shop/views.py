from django.shortcuts import render, redirect
from .models import Product
import stripe
stripe.api_key = "sk_test_51QWwwTLgKEZ8FUNSILqkqMmHvtD6VaxD09dWpObjSlSBlXplUjOf03sCaWcPm65Wc0nbMV75UdKM0UDoL9KP9yrm006zFPtWio"

def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']

        # Create a product in Stripe
        stripe_product = stripe.Product.create(
            name=name,
            description=description,
        )

        # Create a price for the product
        stripe_price = stripe.Price.create(
            unit_amount=int(float(price) * 100),
            currency='usd',
            product=stripe_product.id,
        )

        # Create and save the new product in your database
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            stripe_product_id=stripe_product.id,
            stripe_price_id=stripe_price.id,
        )
        return redirect('product_list')  #

    return render(request, 'shop/add_product.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def checkout(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        # Create a new Stripe Checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data':
                    {'currency': 'usd',
                    'product_data': {'name': product.name,},
                    'unit_amount': int(product.price * 100),
                     },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )
        return redirect(session.url, code=303)
    return render(request, 'shop/checkout.html', {'product': product})

def success(request):
    return render(request, 'shop/success.html')

def cancel(request):
    return render(request, 'shop/cancel.html')