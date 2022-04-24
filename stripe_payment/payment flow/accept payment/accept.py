import stripe
stripe.api_key = 'sk_test_51Kj4D3SGHZPyWBbWDpw0YrepoanDuOLa4rhuvwoxxqJK9bf4x1kXgz0aQZNa049JXCsqcMiqSokQg7VRFJHTU7IR00cRbb3539'










# create a product and price , put that id in this 
# and user id in later bracket
#  
session = stripe.checkout.Session.create(
    
  line_items=[{
    'price': 'price_1KmfRSSGHZPyWBbWUceUI0KN',
    'quantity': 1,
  }],
  mode='payment',
  success_url='https://example.com/success',
  cancel_url='https://example.com/failure',
  payment_intent_data={
    'application_fee_amount': 123,
    'transfer_data': {
      'destination': 'acct_1Kj4P2SBNXT5FcJa',
    },
  },
)