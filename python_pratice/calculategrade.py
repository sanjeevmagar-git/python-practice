# Here is my to calcute grade of students :

 # 90 and above  → A
# 80 to 89      → B
# 70 to 79      → C
# 60 to 69      → D
# below 60      → F

a = input(" Enter your name: ")
b = int(input(" Enter your student id no : "))
if b > 100 :
   print (a, b, " Sorry invalid id no.")
else:
    c = float(input(" Enter your percentage : "))
    if c > 100 :
       print (a, b, c, " Sorry invalid id no.")
    else :
       if c >= 90 :
        print  (" Congratulation !!",a,", student id no",b,( "you have got ' A ' grade. Excellent."))
       elif c >= 80 :
        print (" Congratulation !!",a,", student id no",b,( "you have got ' B ' grade. Very good. " ))
       elif c >= 70 :
        print (" Congratulation !!",a,", student id no",b,( "you have got ' C ' grade. Good. "))
       elif c >= 60 :
         print (" Congratulation !!",a,", student id no",b,( "you have got ' D ' grade. Average. "))
       else :
        print (" Congratulation !!",a,", student id no",b,( "you have got ' F ' grade. Try to improve. "))