
room = input("Enter room type (single/double): ")

if room != "single" and room != "double": 
    print("Invalid room type") 
else:
    nights = int(input("Enter number of nights: "))
   
    if nights <= 0:
        print("Invalid number of nights") 
    else:
        if room == "single":
            if nights <= 3:
                price = 1000
            else:
                price = 800
        else:  # double
            if nights <= 3:
                price = 1500
            else:
                price = 1200
         
        total = price * nights
        print("Total bill:", total)