import phonenumbers
from phonenumbers import  carrier, geocoder, timezone

mobileNo = input("Enter the mobile number with country code 'e.g. +918X6XXXXXX0' :  ")
mobileNo = phonenumbers.parse(mobileNo)

print("Time zone: ", timezone.time_zones_for_geographical_number(mobileNo))
print("Service provider: " , carrier.name_for_number(mobileNo, "en"))
print(geocoder.description_for_number(mobileNo, "en"))
print("Valid or not : ", phonenumbers.is_valid_number(mobileNo))


