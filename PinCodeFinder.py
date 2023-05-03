import requests
import json
while True:

    city = input("Enter the city name  : ")
    url =f"https://api.postalpincode.in/postoffice/{city}"
    r=requests.get(url)
    # print(r.text)
    pdic= json.loads(r.text)
    first_post_office = pdic[0]
    pchoice = first_post_office["PostOffice"][1]
    print(pchoice["Pincode"])
