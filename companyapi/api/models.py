from django.db import models

# Creating Company Model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)  # Auto-incremented primary key
    name = models.CharField(max_length=50)  # Company name field
    location = models.CharField(max_length=50)  # Location field
    about = models.TextField()  # About text field
    type = models.CharField(
        max_length=100,
        choices=(
            ("IT", "IT"),  # Choice: IT
            ("Non IT", "Non IT"),  # Choice: Non IT
            ("Mobile Phones", "Mobile Phones"),  # Choice: Mobile Phones
        ),
    )  # Type field with predefined choices
    added_data = models.DateTimeField(auto_now=True)  # Auto-updated datetime field
    active = models.BooleanField(default=True)  # Active status field
    # We can take an Image field also for future scope

    def __str__(self):
        return self.name + ' Location:' + self.location  # String representation of the Company model


## Relation of the Models One to many


'''
Employee Models
'''
class Employee(models.Model):
    name = models.CharField(max_length=50)  # Employee name field
    email = models.CharField(max_length=50)  # Email field
    address = models.CharField(max_length=200)  # Address field
    phone = models.CharField(max_length=10)  # Phone field
    about = models.TextField(max_length=50)  # About text field
    position = models.CharField(
        max_length=50,
        choices=(
            ('Manager', 'Manager'),  # Choice: Manager
            ('Project Leader', 'PL'),  # Choice: Project Leader
            ('Software Developer', 'SD'),  # Choice: Software Developer
        ),
    )  # Position field with predefined choices

    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # Foreign key relationship with Company model

    def __str__(self):
        return self.name  # String representation of the Employee model
