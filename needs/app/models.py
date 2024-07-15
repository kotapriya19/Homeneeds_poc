from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    quantity = models.CharField(max_length=90,default=1)  # New quantity field

    def __str__(self):
        return f"{self.description} - {self.amount}"

# After modifying the model, make and apply migrations
# Run the following commands in your terminal:
# python manage.py makemigrations
# python manage.py migrate
