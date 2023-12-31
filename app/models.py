from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

STATE_CHOICES= (
    ('Andaman & Nicobar Islands' , 'Andaman & Nicobar Islands' ),
    ('Andhra Pradesh' , 'Andhra pradesh'),
    ('Arunachal Pradesh' , 'Arunachal Pradesh'),
    ('Assam' , 'Assam'),
    ('Bihar' , 'Bihar'),
    ('Chandigath','Chandigath'),
    ('Chatishgath' , 'Chatishgath'),
    ('Dadra & Nagar Haveli' , 'Dadra & Nagar Haveli'),
    ('Daman & Diu' , 'Daman & Diu'),
    ('Delhi' , 'Delhi'),
    ('Goa' ,'Goa'),
    ('Gujarat' , 'Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh' ,'Himachal Pradesh'),
    ('Jammu & Kashmir' , 'Jammu & Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Lakshadweep','Lakshadweep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharastra' , 'Maharastra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland' , 'Nagaland'),
    ('Odisha' , 'Odisha'),
    ('Puducherry','Puducherry'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim' , 'Sikkim'),
    ('Tamil Nadu' , 'Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh' , 'Uttar Pradesh'),
    ('West Bengal','West Bengal'),
)

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) # many to one relantionship by user
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=50)
    
    def __str__(self):
        return str(self.id)
    
CATEGORY_CHOICE=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','TopWear'),
    ('BW','BottomWear'),
)



class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICE,max_length=2)
    product_image = models.ImageField(upload_to='productimg')
    
    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)  # 0 or more then 0
    
    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancle','Cancle')
)

class Orderplaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=80,choices=STATUS_CHOICES,default='Pending')