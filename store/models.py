from django.db import models


class Promotions(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(auto_now_add=True)
    # product_set(because of the many-to-many relationship)


# The 'Product' is to resolve the circular relationship between the `Collection` and the `Product` classes.
# We put `related_name='+'` because Django automatically creates the reverse relationship for us,
# because in the Products class we already have the Collection created
# so Django finds it already there, so we should tell it not to create the reverse by writing `related_name='+'`
class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    description = models.TextField()
    inventory = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotions)


class Customer(models.Model):
    DEFAULT_MEMBERSHIP = 'B'
    MEMBERSHIP_CHOICE = [
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICE, default=DEFAULT_MEMBERSHIP)


class Order(models.Model):
    DEFAULT_PAYMENT_STATUS = 'C'
    PAYMENT_STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Complete'),
        ('F', 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=DEFAULT_PAYMENT_STATUS)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


# One to Many
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
