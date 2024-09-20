from shop.models import Category

def global_context(request):
    # Fetch all categories
    categories = Category.objects.all()


    return {
        'categories': categories,  # Will be available as 'categories' in templates
    }