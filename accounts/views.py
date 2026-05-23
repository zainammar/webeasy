from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

from .forms import SimpleSignupForm
from .models import Profile
from shop.models import Order


# =========================
# SIGNUP
# =========================
def signup(request):
    if request.method == 'POST':
        form = SimpleSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # FIXED: correct namespace
            return redirect('shop:product_list')
    else:
        form = SimpleSignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


# =========================
# LOGIN
# =========================
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # FIXED: correct namespace
            return redirect('shop:product_list')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


# =========================
# LOGOUT
# =========================
def user_logout(request):
    logout(request)
    return redirect('login')


# =========================
# ADMIN: CUSTOMER ORDERS
# =========================
@staff_member_required
def customer_orders(request):
    search_query = request.GET.get('search')

    users = User.objects.all()

    if search_query:
        users = users.filter(username__icontains=search_query)

    data = []

    for user in users:
        profile = Profile.objects.filter(user=user).first()
        orders = Order.objects.filter(user=user).order_by('-created_at')

        data.append({
            "user": user,
            "profile": profile,
            "orders": orders
        })

    total_orders = Order.objects.count()

    return render(request, "accounts/customer_orders.html", {
        "data": data,
        "total_orders": total_orders,
        "search_query": search_query or ""
    })


# =========================
# ADMIN: USERS ORDERS
# =========================
@staff_member_required
def admin_users_orders(request):
    users = User.objects.all()
    orders = Order.objects.select_related('user').prefetch_related('orderitem_set')

    user_data = []

    for user in users:
        profile = Profile.objects.filter(user=user).first()
        user_orders = orders.filter(user=user)

        user_data.append({
            'user': user,
            'profile': profile,
            'orders': user_orders
        })

    return render(request, 'admin/users_orders.html', {
        'user_data': user_data
    })