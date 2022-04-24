# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = 'sk_test_51Kj4D3SGHZPyWBbWDpw0YrepoanDuOLa4rhuvwoxxqJK9bf4x1kXgz0aQZNa049JXCsqcMiqSokQg7VRFJHTU7IR00cRbb3539'

session = stripe.checkout.Session.create(
  line_items=[{
    'price': '{{PRICE_ID}}',
    'quantity': 1,
  }],
  mode='payment',
  success_url='https://example.com/success',
  cancel_url='https://example.com/failure',
  payment_intent_data={
    'application_fee_amount': 123,
    'transfer_data': {
      'destination': '{{CONNECTED_ACCOUNT_ID}}',
    },
  },
)

# 303 redirect to session.url