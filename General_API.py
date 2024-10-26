import requests

country_name = input("Enter the name of the country: ")
response = requests.get(f'https://restcountries.com/v3.1/name/{country_name}')
data = response.json()  # it will return the JSON format data -> similar to python Dictionary -> returns list or dictionary
# print(data[0].keys())

print(f"Capital of the {country_name} is {data[0]['capital'][0]}")
