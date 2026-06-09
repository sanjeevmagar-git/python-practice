# 4 types of room Hotel booking.

#single:
#1 to 3 nights  → Rs 1000 per night
#above 3 nights → Rs 800 per night

#double:
#1 to 3 nights  → Rs 1500 per night
#above 3 nights → Rs 1200 per night

#suite:
#1 to 3 nights  → Rs 3000 per night
#above 3 nights → Rs 2500 per night

#deluxe:
#1 to 3 nights  → Rs 5000 per night
#above 3 nights → Rs 4000 per night

room = input("Enter types of room (Single/Double/Suite/Deluxe): ")
if room != "Single" and room != "Double" and room != "Suite" and room != "Deluxe" :
    print (room,": Invalid room type !")
else :
    nights = int(input("Enter number of nights:" ))
    if nights <=0 :
        print (nights,("Invalid night type ! "))
    else:
        if room == "Single":
            if nights <= 3 :
                price = 1000
            else:
                price = 800
        elif room == "Double" :
             if nights <= 3 :
                price = 1500
             else:
                price = 1200
        elif room == "Suite" :
              if nights <= 3 :
                price = 3000
              else:
                price = 2500
        else :
               if nights <= 3 :
                price = 5000
               else:
                price = 4000
        total = price * nights
        print (total,": Is your total price for", nights,"nights.")
            
        