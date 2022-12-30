name = input('hi welcome to c2cmart what is your name?: ')
print(f'Hi {name}, nice to meet you!')

while True:
  questions = input('Do you have any/other questions about this store regarding our hours, locations, product availability, prices, or any complaints?: ')
  
  if questions == 'no':
    print(f'ok have a nice rest of your day {name}!')
    break
 
  if questions =='yes':
    print('provided responses: hours, locations, product availability, prices, complaints')
    Res = input('What questions do you have about the store?: ')
    if Res == "hours":
      print('We are open all seven days of the week from 9am to 5pm on weekdays and 9am to 7pm on weekends!')
    
    elif Res == 'locations':
      print('We currently have only three stores in the U.S but we do have a website that can ship to anywhere if you wanna order from there instead!')
    
    elif Res == 'product availability':
      print('we have a range of things from clothings to electronics and we have recently stocked up on everything execpt for the ps5s')
    
    elif Res =='prices':
      print('we guartneed the best prices around and will even price match for you!')
    
    elif Res == 'complaints':
      print('Unfortuntly you need to file a complaint through our email so sorry')

    else: 
      print("sorry I didn't quite hear you may you repeat your question again?(please type/spell your responses in exactly the way in provided responses)")

