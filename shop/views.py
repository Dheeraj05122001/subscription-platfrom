from django.shortcuts import render, redirect,get_object_or_404
from .models import Product
from django.http import JsonResponse
import stripe
stripe.api_key = "sk_test_51QWwwTLgKEZ8FUNSILqkqMmHvtD6VaxD09dWpObjSlSBlXplUjOf03sCaWcPm65Wc0nbMV75UdKM0UDoL9KP9yrm006zFPtWio"


def product_list(request):
    # products = Product.objects.all()
    products = stripe.Product.list()

    product_data = []
    for product in products['data']:
        price = stripe.Price.list(product=product['id'])
        product_data.append({
            'name': product['name'],
            'description': product['description'],
            'price': price['data'][0]['unit_amount'] / 100,
            'stripe_product_id': product['id'],
            'stripe_price_id': price['data'][0]['id'],
        })
    return render(request, 'shop/product_list.html', {'products': products})

def checkout(request,stripe_product_id):
    product = stripe.Product.retrieve(stripe_product_id)
    price = stripe.Price.list(product=stripe_product_id)['data'][0]
    checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data':
                    {'currency': 'usd',
                    'product_data': {'name': product['name'],
                                     'description':product['description'],},
                    'unit_amount': price['unit_amount'],

                     },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )
    return redirect(checkout_session.url, code=303)

def success(request):
    return render(request, 'shop/success.html')

def cancel(request):
    return render(request, 'shop/cancel.html')