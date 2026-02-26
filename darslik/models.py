from django.db import models
import uuid
# Create your models here.



class Universitet(models.Model):
    nom = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    students_count = models.SmallIntegerField(default=0)
    director_name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='university-images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nom}, {self.students_count}"

    class Meta:
        verbose_name = "Universitet"
        verbose_name_plural = "Universitetlar"
        ordering = ['-created_at', 'nom']



class Teacher(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    experience_year = models.PositiveSmallIntegerField(default=0)
    salary = models.PositiveBigIntegerField(default=0)
    groups_count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.name} {self.salary}"
    


class Student(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    gpa = models.FloatField(default=0)
    age = models.PositiveSmallIntegerField(default=0)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.age}"
    


















# class TestModel(models.Model):
#     ism = models.CharField(max_length=50)
#     age = models.IntegerField(default=15)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     birthday = models.DateField(blank=True, null=True)
#     joined_time = models.TimeField(blank=True, null=True)
#     avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
#     daraja = models.SmallIntegerField(default=12)
#     rezume = models.FileField(upload_to='rezumes/', blank=True, null=True)
#     bio = models.TextField(blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)
#     test_model = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
#     narx = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     id = models.UUIDField(uuid.uuid4, editable=False, unique=True)
#     baho = models.PositiveSmallIntegerField(default=10)
#     quantity = models.PositiveIntegerField(default=1)
#     profile = models.OneToOneField("UserProfile", on_delete=models.CASCADE, blank=True, null=True)
#     fanlar = models.ManyToManyField("Fanlar", blank=True)


"""

-----
BigIntegerField
FloatField
UrlField
DurationField
AutoField
BinaryField
SlugField
JsonField
HStoreField
ArrayField







"""


