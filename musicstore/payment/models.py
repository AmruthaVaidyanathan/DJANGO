Skip to content
Why GitHub? 
Enterprise
Explore 
Marketplace
Pricing 
Search

Sign in
Sign up
cityuseattle
/
amazon-apprenti-2019-2
110
 Code Issues 0 Pull requests 0 Actions Projects 0 Security Insights
Join GitHub today
GitHub is home to over 40 million developers working together to host and review code, manage projects, and build software together.

amazon-apprenti-2019-2/CS260/AmandaChavez/Module9/hop/musicstore/payment/models.py
 achavez-apprenti Submitting CS260-HP09.
06937a7 on Nov 6, 2019
37 lines (25 sloc)  1.17 KB
  
from django.db import models

# Create your models here.
class Payment(models.Model):
    card_number = models.BigIntegerField(unique=True)
    card_type = models.CharField(max_length=30)
    billing_address = models.CharField(max_length=1000)

    objects = models.Manager()

    class Meta: 
        ordering = ['-card_number']
        
def create_process(_card_number, _card_type, _billing_address):
    payment = Payment(card_number=_card_number, card_type=_card_type, billing_address=_billing_address)

    # Validation - Ensure the instance values comply with those of the model definition
    # Rasie ValidationError if the test failed
    payment.full_clean()
    
    # Create the record in the target database
    payment.save()

def fetch_all_pmt_methods_process():
    # Return a dict of payment methods
    return Payment.objects.in_bulk()

def fetch_payment_method_process(_id):
    return Payment.objects.get(id=_id)

def edit_process(_id, _card_number, _card_type, _billing_address):
    Payment.objects.filter(id=_id).update(card_number=_card_number, card_type=_card_type, billing_address=_billing_address)

def delete_process(_id):
    Payment.objects.filter(id=_id).delete()
    
    

