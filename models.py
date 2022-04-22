from django.db import models

# Create your models here.
PAYCODE_CASH= "CASH"
PAYCODE_CARD = "CARD"
PAYCODE_PAYPAL = "PAYPAL"
PAYCODE_CHEQUE = "CHEQUE"

PAYCODE_CHOICES =(
    (PAYCODE_CASH, 'cash'),
    (PAYCODE_CARD, 'card'),
    (PAYCODE_PAYPAL, 'PayPal'),
    (PAYCODE_CHEQUE, 'cheque'),


)
class Room(models.Model):
    name=models.CharField(max_length=100)
    tele=models.IntegerField(max_length=10)
    adress=models.TextField(max_length=100)
    country=models.TextField()
    payment_status=models.BooleanField()
    payment_mode = models.CharField( "Payment Method", max_length=20, choices=PAYCODE_CHOICES, blank=False,
                                         null=False )
    total_cost=models.IntegerField()



class Reservation(models.Model):
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    room = models.ForeignKey( Room, on_delete=models.CASCADE )

