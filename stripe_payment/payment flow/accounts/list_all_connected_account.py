# 5. 
import stripe
stripe.api_key = "sk_test_51Kj4D3SGHZPyWBbWDpw0YrepoanDuOLa4rhuvwoxxqJK9bf4x1kXgz0aQZNa049JXCsqcMiqSokQg7VRFJHTU7IR00cRbb3539"

val= stripe.Account.list()
print(val)