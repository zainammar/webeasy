from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem


# Product list
def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product_list.html', {'products': products})


# Product detail
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})


# Add to cart (session)
@login_required(login_url='login')
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart = request.session.get('cart', {})

    quantity = int(request.POST.get('quantity', 1))

    cart[str(product.id)] = cart.get(str(product.id), 0) + quantity
    request.session['cart'] = cart

    return redirect('cart_detail')


# View cart
@login_required(login_url='login')
def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        item_total = product.price * quantity
        total += item_total

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })

    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


# Checkout → Save to Database (FINAL CART FOR ADMIN)
@login_required(login_url='login')
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart_detail')

    total = 0
    order = Order.objects.create(
        user=request.user,
        total_price=0
    )

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        item_total = product.price * quantity
        total += item_total

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.price
        )

    order.total_price = total
    order.save()

    # Clear session cart
    request.session['cart'] = {}

    return redirect('product_list')



@login_required(login_url='login')
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart_detail')

    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        item_total = product.price * quantity
        total += item_total

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })

    # When user confirms order
    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            total_price=total
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['product'].price
            )

        # Clear session cart
        request.session['cart'] = {}

        return redirect('product_list')

    return render(request, 'shop/checkout.html', {
        'cart_items': cart_items,
        'total': total
    })
