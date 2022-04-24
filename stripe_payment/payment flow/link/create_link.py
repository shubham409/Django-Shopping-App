# these are the links that are used to open stripe website 
# add fill remaining information for the shopkeeper and 
#  fill requiered information
import stripe
stripe.api_key = "sk_test_51Kj4D3SGHZPyWBbWDpw0YrepoanDuOLa4rhuvwoxxqJK9bf4x1kXgz0aQZNa049JXCsqcMiqSokQg7VRFJHTU7IR00cRbb3539"

link= stripe.AccountLink.create(
  account="acct_1Kj4P2SBNXT5FcJa",
  refresh_url="https://example.com/reauth",
  return_url="https://example.com/return",
  type="account_onboarding",
)
print(link)