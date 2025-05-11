from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib.auth.models import AbstractUser

WILAYA_CHOICES = [
    ('01', 'أدرار'), ('02', 'الشلف'), ('03', 'الأغواط'), ('04', 'أم البواقي'),
    ('05', 'باتنة'), ('06', 'بجاية'), ('07', 'بسكرة'), ('08', 'بشار'),
    ('09', 'البليدة'), ('10', 'البويرة'), ('11', 'تمنراست'), ('12', 'تبسة'),
    ('13', 'تلمسان'), ('14', 'تيارت'), ('15', 'تيزي وزو'), ('16', 'الجزائر'),
    ('17', 'الجلفة'), ('18', 'جيجل'), ('19', 'سطيف'), ('20', 'سعيدة'),
    ('21', 'سكيكدة'), ('22', 'سيدي بلعباس'), ('23', 'عنابة'), ('24', 'قالمة'),
    ('25', 'قسنطينة'), ('26', 'المدية'), ('27', 'مستغانم'), ('28', 'المسيلة'),
    ('29', 'معسكر'), ('30', 'ورقلة'), ('31', 'وهران'), ('32', 'البيض'),
    ('33', 'إيليزي'), ('34', 'برج بوعريريج'), ('35', 'بومرداس'), ('36', 'الطارف'),
    ('37', 'تندوف'), ('38', 'تيسمسيلت'), ('39', 'الوادي'), ('40', 'خنشلة'),
    ('41', 'سوق أهراس'), ('42', 'تيبازة'), ('43', 'ميلة'), ('44', 'عين الدفلى'),
    ('45', 'النعامة'), ('46', 'عين تيموشنت'), ('47', 'غرداية'), ('48', 'غليزان')
]

class CustomUser(AbstractUser):
    class Meta:
        verbose_name = 'مستخدم'
        verbose_name_plural = 'المستخدمون'

    def __str__(self):
        return self.username

class Product(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    category = models.CharField(max_length=100, verbose_name="الفئة")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    description = models.TextField(verbose_name="الوصف")
    image = CloudinaryField('image')
    stock = models.PositiveIntegerField(default=1, verbose_name="الكمية المتاحة")
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    customer_name = models.CharField(max_length=100, verbose_name="اسم الزبون")
    phone_number = models.CharField(max_length=20, verbose_name="رقم الهاتف")
    wilaya = models.CharField(max_length=50, choices=WILAYA_CHOICES, verbose_name="الولاية")
    commune = models.CharField(max_length=100, verbose_name="البلدية")
    address = models.TextField(verbose_name="العنوان التفصيلي")
    confirmed = models.BooleanField(default=False, verbose_name="تم التأكيد")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'الطلب'
        verbose_name_plural = 'الطلبات'

    def __str__(self):
        return f"طلب #{self.id} - {self.product.name}"