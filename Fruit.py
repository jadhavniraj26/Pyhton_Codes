a=1
price={"Apple":200,"Banana":50}
stock={"Apple":20,"Banana":10}
total=0
while a==1:

  print("Fruit Management System")
  choice=int(input("\nPress 1 for Adding Fruits to the system \nPress 2 for dicarding rotten fruits \nPress 3 for Purchase of Fruits \nPress 4 for Finding Total price of all fruits \nPress 5 for Displaying info of Fruits\n"))

  if choice==1:
      ch=int(input("\nPress 1 for adding New fruits \nPress 2 for adding existing fruit\n"))
      if ch==1:
           l1=int(input("Enter the number of Fruits you want to enter= "))
           for i in range(l1):
                  fruit=input("Enter the Name of the Fruit\n")
                  st=int(input("Enter the quantity of the Fruit= \n"))
                  pr=int(input("Enter the Price of the Fruit= \n"))
                  price[fruit]=fruit
                  price[fruit]=pr
                  stock[fruit]=st
                  print("Name and Price of Fruit:",price)
                  print("Name and Stock of Fruit",stock)
                    
      else :
          l1=int(input("Enter the number of Fruits you want to enter= \n"))
          for i in range(l1):
            fruit=input("Enter the Name of the Fruit= \n")
            if price.keys==fruit:

                 st=int(input("Enter the quantity of the Fruit= \n"))
                 stock[fruit]=stock[fruit]+st
                 print(price)
                 print(stock)
            else :
                print("Entered Fruit doesn't exist in Inventory")   

  elif choice==2:
    l1=int(input("Enter the number of Fruits you want to dicard= \n"))
    #print(price)
    for i in range(l1):
            fruit=input("Enter the Name of the Fruit= \n")
            if price.keys==fruit:
              print("Existing Quantity of the Fruit "+fruit,stock[fruit])
              st=int(input("Enter the quantity of the Fruit to be discarded= \n"))
            
              if stock[fruit]<st:
                  print("Dicard Quantity exceeds Existing Quantity")
              else:    
                  stock[fruit]=stock[fruit]-st
                  print("Remaining stock of fruit "+fruit,stock[fruit],"kg")
                  print(stock)
            else: 
                print("Entered Fruit doesn't exist in Inventory")     

  elif choice==3:
    print("Purchase")
    l2=int(input("Enter the Number of Fruits you want to make purchase of = \n"))
    for i in range(l2):
          fruit=input("Enter the Name of the fruit= \n")
          if price.keys==fruit:

             print("Existing Quantity of the Fruit "+fruit,stock[fruit],"kg")
             st=int(input("Enter the quantity of purchase\n"))
             amt=0
             temp=0
             if stock[fruit]<st:
                  print("Entered quantity of the fruit is not available\n")
             else:
                  stock[fruit]=stock[fruit]-st
                  amt=price[fruit]*st
                  
                  print("Total price of purchase= \n",amt)
                  print("Remaining stock of fruit "+fruit,stock[fruit],"kg")
                  print(stock) 
          else :
                print("Entered Fruit doesn't exist in the Inventory")

                
  elif choice==4:
      print("Total Amount of the all fruits in the Inventory:\n") 
      for fruit in price:
        money= price[fruit]*stock[fruit]
        print("Total of Amount of "+fruit+"=",money)
        total=total + money
      print("The total Amount of fruit= \n", total)

  elif choice==5:

    print("All Fruits and their price in the Inventory:\n")
    for i in price:
      print ("Name of Fruit= "+i+" Price=₹",price[i],"Quantity=",stock[i],"kg\n")
               
  else:
    print("Invalid Input")
    #print(price,stock)
