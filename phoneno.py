import phonenumbers
from phonenumbers import geocoder, carrier

#number="+1888888888"
number="+9155555555555"
ctryno=phonenumbers.parse(number,"CH")  # CH COUNTRY HISTORY
print(geocoder.description_for_number(ctryno,'en'))
#from phonenumber import carrier
service_number=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))