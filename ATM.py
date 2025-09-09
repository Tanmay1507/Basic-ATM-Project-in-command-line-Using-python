import random
import openpyxl
import pandas

//hello world//
print("   ")
print("   ") 
print("Wellcome to the bank".center(30,'-') ) 
print("   ")
print("MANU".center(30, '-'))
while True:
  print("1.Creat new account")
  print("2.Log-in ")
  print("3.Info")
  print("4.EXIT")
  first_ch= int(input("Enter CHOICE: "))
  if first_ch==1:
   print("Creat New Account".center(30,'-') )
   print("   ")
   name = input("Enter your name* : ")
   city = input("Enter City* : ")
   phone =int(input("Enter your phone number :"))
   balance = int(input("Enter Opening Balance* : "))
   while True:
       pin1 = input("Enter pin*")
       pin2 = input("Confirm pin")
       if pin1 == pin2:
         print("PIN SET SUCCESSFULLY!!")
         account=random.choice
         print(account)
         print(pin1)
         break
       else:
        print("PIN NOT MATCHING")
  elif first_ch==2:
    login_account=input("Enter your account noumber :-")
    login_password=input("Enter your password : ")

    while True:
        print("   ")
        print("   ")
        print("   ")

        print("MANU".center(30,'-'))
        print("1.INFO")
        print("2.DEPOSITE")
        print("3.WITHDRAW")
        print("4.EXIT")
        ch = int(input("Enter CHOICE: "))
        if ch == 1:
           print()
           pin = input("Enter your pin: ")
           if pin == pin1:
                  print("INFO".center(30,'-'))
                  print("Name: ",name)
                  print("City: ",city)
                  print("Balance: ",balance)
           else: print("INVALID PIN")
        elif ch == 2:
          print()
          pin = input("Enter your pin: ")
          if pin == pin1:
             print("DEPOSITE".center(30,'-'))
             amount = int(input("Enter Amt to Deposite: "))
             balance+=amount
             print("DEposite Successfull | Current Balance :₹",balance)
          else: print("INVALID PIN")
        elif ch == 3:
         print()
         pin = input("Enter your pin: ")
         if pin == pin1:
          print("WITHDRAW".center(30,'-'))
          amount = int(input("Enter Amt to Withdraw: "))
          if amount > balance:
           print("Insufficient Balance!!")
          else:
           balance-=amount
           print("Withdraw Successfull | Current Balance:₹",balance)
         else:
          print("INVALID PIN")
        elif ch == 4:
             break
        else:
         print()
         print("WRONG INPUT")
    print("Thank you visit again !!!".center(30,'-'))

    print("")
