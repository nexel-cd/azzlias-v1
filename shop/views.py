from django.shortcuts import render, get_object_or_404
from .models import Products, ProductImage  # Importing both models
from django.core.paginator import Paginator

# View to list all products with pagination
def shop(request):
    products_list = Products.objects.all().order_by('-created_at')  # Order products by newest first
    products_list_count = products_list.count()  # Get the total number of products

    # Set the number of products per page
    paginator = Paginator(products_list, 8)  # Show 8 products per page

    # Get the current page number from the request
    page_number = request.GET.get('page')

    # Get the products for the current page
    page_obj = paginator.get_page(page_number)

    # Pass the page_obj to the context
    context = {'page_obj': page_obj, "products_list_count": products_list_count}
    return render(request, 'allshop.html', context)


# View to display product details and associated images
def product_details(request, pk):
    product = get_object_or_404(Products, id=pk)  # Fetch product by primary key
    images = product.images.all()  # Fetch all images associated with the product (using related_name from ProductImage model)
    context = {
        'product': product,
        'images': images,
    }
    return render(request, 'product_list.html', context)


# View to list products by category with pagination
def shop_category(request, pk):
    products_list = Products.objects.filter(category=pk).order_by('-created_at')  # Fetch all products by category
    products_list_count = products_list.count()  # Get the total number of products in the category

    # Set the number of products per page
    paginator = Paginator(products_list, 8)  # Show 8 products per page

    # Get the current page number from the request
    page_number = request.GET.get('page')

    # Get the products for the current page
    page_obj = paginator.get_page(page_number)

    # Pass the page_obj and count to the context
    context = {'page_obj': page_obj, "products_list_count": products_list_count}
    return render(request, 'allshop_category.html', context)
