from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    

class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

class Size(models.Model):
    size = models.CharField(max_length=10, choices=[
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    ])

    def __str__(self):
        return self.get_size_display() 


class Products(models.Model):
    # Basic product information
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField('Original Price', max_digits=10, decimal_places=2)
    disprice = models.DecimalField('Discount Price', max_digits=10, decimal_places=2, null=True, blank=True)

     # Flipkart URL
    flipkart_url = models.URLField(max_length=500, blank=True, null=True)  # Add this field

    # Additional product details
    size =  models.ManyToManyField(Size, related_name='products', blank=True) 
    color =models.CharField(max_length=50)
    colors = models.ManyToManyField('Color', related_name='products') 
    material = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)

    # Relationships
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='products', blank=True)

    # Stock and availability
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)

    # Images
    image = models.ImageField(upload_to='product_images/')

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def is_discounted(self):
        return self.disprice is not None and self.disprice < self.price


class ProductImage(models.Model):
    # Linking image to a specific product
    product = models.ForeignKey(Products, related_name='images', on_delete=models.CASCADE)

    # Image file
    image = models.ImageField(upload_to='product_images/')

    # Image description or alt text
    alt_text = models.CharField(max_length=255, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.product.name}"
