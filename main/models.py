from django.db import models

class Customer(models.Model):
    cid=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    balance=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name

        
class Transaction(models.Model):
    sno = models.AutoField(primary_key=True)
    sender_acc = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sender')
    receiver_acc =models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='receiver' )
    Amount = models.DecimalField(max_digits=14,decimal_places=2)
    status = models.BooleanField()
    date = models.DateTimeField(auto_now=True)

    


