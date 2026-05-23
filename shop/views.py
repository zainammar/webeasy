from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem, Category # <-- Make sure Category is imported!

from django.shortcuts import render, redirect
from .forms import PaymentProofForm

def upload_payment_proof(request):
    if request.method == "POST":
        form = PaymentProofForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            # 🔥 THIS IS WHERE REDIRECT GOES
            return redirect('shop:success_page')

    else:
        form = PaymentProofForm()

    return render(request, "shop/uploadpaymentproff.html", {'form': form})


def success_page(request):
    return render(request, "shop/success.html")
# Product list
def product_list(request, category_slug=None): # <-- Added category_slug for filtering
    category = None
    categories = Category.objects.all() # <-- Fetch ALL categories here
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/product_list.html', {
        'category': category,
        'categories': categories, # <-- Pass categories to the template
        'products': products
    })

# Product detail
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    # We'll also pass categories here if you want them on product detail pages
    categories = Category.objects.all()
    return render(request, 'shop/product_detail.html', {
        'product': product,
        'categories': categories # <-- Pass categories to product_detail as well
    })

# Add to cart (session)
@login_required(login_url='login')
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart = request.session.get('cart', {}) # <-- Ensure this is `{}`

    quantity = int(request.POST.get('quantity', 1))

    cart[str(product.id)] = cart.get(str(product.id), 0) + quantity
    request.session['cart'] = cart

    return redirect('shop:cart_detail')

# View cart
@login_required(login_url='login')
def cart_detail(request):
    cart = request.session.get('cart', {}) # <-- Ensure this is `{}`
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
    
    categories = Category.objects.all() # <-- Pass categories to cart_detail
    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'total': total,
        'categories': categories # <-- Pass categories
    })

# Checkout (first instance of checkout)
@login_required(login_url='login')
def checkout(request):
    cart = request.session.get('cart', {}) # <-- Ensure this is `{}`
    if not cart:
        return redirect('shop:cart_detail')

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

    return redirect('shop:product_list')
@login_required(login_url='login')
def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('shop:cart_detail')

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

    # POST = place order
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

        request.session['cart'] = {}

        return redirect('shop:product_list')

    categories = Category.objects.all()

    return render(request, 'shop/checkout.html', {
        'cart_items': cart_items,
        'total': total,
        'categories': categories
    })