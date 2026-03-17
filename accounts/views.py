from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SimpleSignupForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SimpleSignupForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from shop.models import Order
from .models import Profile
from django.shortcuts import render
@staff_member_required
def customer_orders(request):

    search_query = request.GET.get('search')

    # Get users
    users = User.objects.all()

    # Apply search filter
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

    # Total orders (ALL orders in system)
    total_orders = Order.objects.count()

    return render(request, "accounts/customer_orders.html", {
        "data": data,
        "total_orders": total_orders,
        "search_query": search_query or ""
    })

@staff_member_required
def admin_users_orders(request):
    users = User.objects.all().select_related()
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


def signup(request):
    if request.method == 'POST':
        form = SimpleSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = SimpleSignupForm()

    return render(request, 'accounts/signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SimpleSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = SimpleSignupForm()
    return render(request, 'accounts/signup.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from shop.models import Order
from .models import Profile
from django.shortcuts import render

@staff_member_required
def customer_orders(request):

    users = User.objects.all()

    data = []

    for user in users:
        profile = Profile.objects.filter(user=user).first()
        orders = Order.objects.filter(user=user)

        data.append({
            "user": user,
            "profile": profile,
            "orders": orders
        })

    return render(request, "accounts/customer_orders.html", {"data": data})