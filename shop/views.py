from django.shortcuts import render, redirect
import stripe
stripe.api_key = "sk_test_51QWwwTLgKEZ8FUNSILqkqMmHvtD6VaxD09dWpObjSlSBlXplUjOf03sCaWcPm65Wc0nbMV75UdKM0UDoL9KP9yrm006zFPtWio"

def product_list(request):
    products = stripe.Product.list()
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