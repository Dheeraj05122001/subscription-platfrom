## Django Subscription plafrom using Stripe

This project demonstrates how to integrate **Stripe** in a Django application for product checkout using Stripe's **Product Catalog** and **Checkout Session**. Users can view products, initiate a checkout session, and make payments securely through Stripe.

## Features
- Fetch products from Stripe's Product Catalog.
- List products with a "Buy Now" button.
- Use Stripe Checkout to handle payments.
- Redirect users to success or cancel pages after the payment process.

## Technologies Used 

- Python 3.11.4
- Django 5.1.4
- Stripe account for API keys(STRIPE_TEST_SECRET_KEY,STRIPE_TEST_PUBLIC_KEY)

## Setup up Stripe Account
- Create a Stripe account at Stripe.com.
- Navigate to your Dashboard and obtain your Stripe API keys.
- Secret Key 
- Publishable Key 


## Install the django using
- pip install django

## create a project using
- django-admin startproject project_name

## Create an app in this using
- python manage.py startapp app_name

## This project contaning the folder/file
1. my_ecommerce(project folder) 
-  __init__.py
-  settings.py
-  urls.py

2. shop(App folder)
-  migrations
-  templates/shop
-  models.py
-  views.py
-  urls.py

3. manage.py 

## Run the development server using 
-  python manage.py runserver
 
## Add Products to Stripe
-  To add products manually:
-  Log into your Stripe Dashboard.
-  Go to Products and manually create new products with pricing details (including name, description, and price).

## Fetch Products from Stripe in Django
-  The Django app fetches products from the Stripe API using the stripe.Product.list() method and displays them on the Product List page.


