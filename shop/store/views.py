from random import randint
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView
from .forms import *
from django.contrib.auth import login, logout
from django.contrib import messages



class ProductList(ListView):
    model = Product
    context_object_name = 'categories'
    extra_context = {
        'title': 'Store "Totembo"'
    }
    template_name = 'store/product_list.html'

    def get_queryset(self):
        categories = Category.objects.filter(parent=None)
        return categories


class CategoryView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'store/category_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        main_category = Category.objects.get(slug=self.kwargs['slug'])
        context['category'] = main_category
        context['title'] = f'{main_category.title}'
        return context

    def get_queryset(self):
        sort_field = self.request.GET.get('sort')
        type_field = self.request.GET.get('type') # Subcategoriyani oladi !

        if type_field:
            products = Product.objects.filter(category__slug=type_field)
            return products
        main_category = Category.objects.get(slug=self.kwargs['slug'])
        subcategories = main_category.subcategories.all()
        products = Product.objects.filter(category__in=subcategories)

        if sort_field:
            products = products.order_by(sort_field)
        return products


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        product = Product.objects.get(slug=self.kwargs['slug'])
        context['title'] = f'{product.title}'
        products =Product.objects.all()
        data =[]
        for i in range(4):
            random_index = randint(0, len(products) -1)
            p = products[random_index]
            if p not in data:
                data.append(p)
        context['products'] = data
        context['reviews'] = Review.objects.filter(product=product)

        if self.request.user.is_authenticated:
            context['review_form'] = ReviewForms()

        return context

def save_review(request, product_id):
    form = ReviewForms(data=request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.author = request.user
        product = Product.objects.get(pk=product_id)
        review.product = product
        review.save()
    else:
        pass
    return redirect('product_detail',product.slug)

def login_registration(request):
    context = {
        'title': 'Login And Registration',
        'login_form': LoginForm(),
        'register_form': RegistrationForm(),
        'hide_alerts': True,  # base.html alertlarini o'chiradi
    }
    return render(request, 'store/login_register.html', context)

def user_login(request):
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request,'You are now logged in!')
        return redirect('product_list')
    else:
        messages.error(request,'Please correct the error below.')
        return redirect('login_registration')


def user_logout(request):
    logout(request)
    messages.warning(request,'You are now logged out!')
    return redirect('login_registration')



def register(request):
    form = RegistrationForm(data=request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'You are now logged in!')
        return redirect('product_list')
    else:
        messages.error(request, 'Please correct the error below.')
        return redirect('login_registration')
