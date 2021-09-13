import phonenumbers
from phonenumbers import geocoder, carrier,timezone

def check(MN):
    track_number = phonenumbers.parse(MN, "CH")
    print("Carrier : " + carrier.name_for_number(track_number, 'en'))
    print("Region : "+ geocoder.description_for_number(track_number , 'en'))
    print("TimeZone : "+ timezone.time_zones_for_number(track_number))

def inp():
    phone_number = phonenumbers.parse(input())
    if phonenumbers.is_valid_number(phone_number):
        check(phone_number)
    else:
        print("Please enetr a vaild number.")
        return inp()    