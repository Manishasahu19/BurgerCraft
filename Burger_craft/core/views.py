from django.shortcuts import render, get_object_or_404, redirect
from .models import Burger

# 1. Homepage View
def home(request):
    all_burgers = Burger.objects.all()
    return render(request, 'core/home.html', {'burgers': all_burgers})

# 2. Detail Page View
def product_detail(request, pk):
    single_burger = get_object_or_404(Burger, pk=pk)
    return render(request, 'core/detail.html', {'burger': single_burger})

# 3. Add to Cart View
def add_to_cart(request, pk):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        
        if str(pk) in cart:
            cart[str(pk)] += quantity
        else:
            cart[str(pk)] = quantity
            
        request.session['cart'] = cart
        return redirect('detail', pk=pk)

# 4. Cart Page View
def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    grand_total = 0
    
    for burger_id, quantity in cart.items():
        try:
            burger = Burger.objects.get(id=int(burger_id))
            total_price = burger.price * quantity
            grand_total += total_price
            cart_items.append({
                'burger': burger,
                'quantity': quantity,
                'total_price': total_price
            })
        except Burger.DoesNotExist:
            pass
            
    context = {
        'cart_items': cart_items,
        'grand_total': grand_total
    }
    return render(request, 'core/cart.html', context)

# 5. Plus / Minus Quantity Update View
def update_cart_qty(request, pk, action):
    cart = request.session.get('cart', {})
    burger_id = str(pk)
    
    if burger_id in cart:
        if action == 'increase':
            cart[burger_id] += 1
        elif action == 'decrease':
            cart[burger_id] -= 1
            if cart[burger_id] <= 0:
                del cart[burger_id]
                
    request.session['cart'] = cart
    return redirect('cart_detail')

# 6. Remove Item View
def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    burger_id = str(pk)
    
    if burger_id in cart:
        del cart[burger_id]
        
    request.session['cart'] = cart
    return redirect('cart_detail')

# 7. About Page View
def about(request):
    return render(request, 'core/about.html')

# 8. Checkout View (Dhyan se check karein ye line)
def checkout(request):
    cart = request.session.get('cart', {})
    grand_total = 0
    
    for burger_id, quantity in cart.items():
        try:
            burger = Burger.objects.get(id=int(burger_id))
            grand_total += burger.price * quantity
        except Burger.DoesNotExist:
            pass
            
    if not cart:
        return redirect('cart_detail')
        
    return render(request, 'core/checkout.html', {'grand_total': grand_total})

# 9. Payment Success View
def payment_success(request):
    if 'cart' in request.session:
        del request.session['cart']
    return render(request, 'core/success.html')