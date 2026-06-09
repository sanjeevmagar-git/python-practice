
movie = input("Enter movie type (standard/premium:")

if movie != "standard" and movie != "premium" :
    print (movie,": Invalid movie type !")
else:
    tickets = int(input("Enter numbers of tickets: "))
    
    if tickets <= 0:
        print (tickets,"Invalid tickets type !")    
    else:
        if movie == "standard" :
            if tickets <=3 :
               price = 50
            else:
               price = 40
        else: # premium
            if tickets <=3:
                price = 100
            else:
                price = 80
    
        total = tickets * price
        print ("Total price:",total,"Rs")
