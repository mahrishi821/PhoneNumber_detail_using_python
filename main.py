import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number = input("Enter your number with +91(for india) :: ")
print(number)
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")#we use en because the name of company should comee inn english
reg=geocoder.description_for_number(phone,"en")
print("*********************************")
print(phone)
print(time)
print(car)
print(reg)