import phonenumbers

from phonenumbers import geocoder, carrier
my_number = "+33778685057"
ch_number = phonenumbers.parse(my_number,"CH")
print(geocoder.description_for_number(ch_number, "en"))

service_number =  phonenumbers.parse(my_number, "RO")

print(carrier.name_for_number(service_number, "en")) 