escrow_key = '15390_3B4WBcry6K8i6NinwbutLdzhXOBpkMCsndQkmdvINeGwBTaC7o0AQlg5mc9692fE'
email = "sm091274@gmail.com"
'''
15390_3B4WBcry6K8i6NinwbutLdzhXOBpkMCsndQkmdvINeGwBTaC7o0AQlg5mc9692fE
'''
# adding customer 


import requests

res = requests.post(
  'https://api.escrow.com/2017-09-01/customer',
  auth=(email, escrow_key),
  json={
    "email": "sandeep@test.escrow.com",
    "first_name": "John",
    "middle_name": "Kane",
    "last_name": "Smith",
    "address": {
      "line1": "1829 West Lane",
      "line2": "Apartment 301020",
      "city": "San Francisco",
      "state": "CA",
      "country": "US",
      "post_code": "10203"
    },
    "phone_number": "8885118600"
  }
)
print(res.text)

# getting all the customers 
res = requests.get(
  'https://api.escrow.com/2017-09-01/customer/me',
  auth=(email, escrow_key),
)

print(res.text)














