   #ATMMock=File System 
import random
import os
from datetime import datetime

userBalance = 0
curBalance = 0
response = False
userAcct = ""
user_account_number = ""

#Adding new customers
def addNewCustomerToBank(NewcustomerData):
    #*************************
    # check if customer already exists
    #Add newCustomer to account number fil
    #print(NewcustomerData)
    
    filePath = "auth_session/account_number.txt"
    f = open(filePath, "a")
    f.write(NewcustomerData)
    f.close()

print()
# Access the item of a list for main greeting

def MainMenuGreet(user_account_number,first_name, last_name):
    print()
    print("******* Welcome to The Bank *******")
    print()
    
    #date_time = stamp
    date_time = getStamptime()
    print("Date and Time:",date_time)
    
    print()
    print("Account Number: " + str(user_account_number))
    print("Hello, " + str(first_name) + " " +str(last_name))
    print()
#Transaction_Options(user_account_number)

#Customer In Session create
def createInsession(userAcct): 
    sTime = getStamptime()  
    filePath = "auth_session/" + str(userAcct) + ".txt"      
    f = open(filePath,"a")
    f.write(sTime)                                
    f.close()


#define bank menu items
def Transaction_Options(user_account_number):
    print()
    print("These are the available options:")
    print("1. Withdrawal")
    print("2. Cash Deposit")
    print("3. Complaint ")
    print("4. Exit Program" )
    print() 
    selectedOption = int(input('Please select an option: '))
    
    menuOptions(user_account_number, selectedOption)
 

def newAccount():
    random_number = random.randint(1000000, 9999999)
    return (random_number)

#get the new customer info
def newCustomer():
    first_name = input("Enter your first name: ") 
    #validate first_name is all alpha 
    last_name = input("Enter your last name: ")
    #validate last_name is all alpha   
    email = input("Please enter your email: ")
    #validate password meets correct password 
    password = input("Please create your password: ")
    user_account_number = newAccount()
    
    #Format string
    newCustomerData = str(user_account_number) + "," + "'" + str(first_name) + "'"+ "," + "'" + str(last_name) + "'" + "," + "'" + str(email) + "'" + "," + "'" + str(password) +"'"+ "\n"
  
    addNewCustomerToBank(newCustomerData)
    
    MainMenuGreet(user_account_number,first_name, last_name)

    AddNewCustomerBalance(user_account_number,500.00,False)

    createInsession(user_account_number)

    Transaction_Options(user_account_number) 

def AddNewCustomerBalance(user_account_number,userBalance,update):
    
    if(update) == False:
      userBalance = 500.00    #New customer

    balanceInfo = str(user_account_number) + "," + str(userBalance)
    filePath = "auth_session/userBalanceFile.txt"
    f = open(filePath, "a")
    f.write(balanceInfo)
    f.write("\n")
    f.close()   
#***************************

def getStamptime():
    now = datetime.now() # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    return date_time


#Customer In Session delete
def removeInSession(userAcct):
    filePath = "auth_session/" + str(userAcct) + ".txt"
    if os.path.exists(filePath):
       os.remove(filePath)
    else:
       print("Can not delete the file as it doesn't exists")


#*****************************updateCustomerBalanc
def getCustomerBalance(userAcctNumber):
    with open("auth_session/userBalanceFile.txt", "r") as f:
        lines = f.readlines()
        f.close()
        for line in lines:
            parts = line.split(",") # split line into parts
          #print(parts)
            if len(parts) > 1:
                if(str(userAcctNumber) == str(parts[0])):
                  curBalance = (float(parts[1]))                         
                else:
                  curBalance = 0        

    return curBalance

def delete_oldbal(user_account_number):
    
    fname = "auth_session/userBalanceFile.txt"
    f = open(fname)
    output = []

    for line in f:

     if not str(user_account_number) in line:
        
        output.append(line)

        f = open(fname, 'w')

        f.writelines(output)

        f.close()


#****************************************
def UpdateUserBalance (user_account_number, user_Balance, amount,dw):
   
    with open("auth_session/userBalanceFile.txt", "r+") as f:
          lines = f.readlines()
  
          for line in lines:
              line = line.split(",")
              
              if(str(user_account_number) == str(line[0])):
                  curBalance = line[1]  
                  if dw == 'w':
                     newBalance = float(curBalance) - float(amount)
                  elif dw == 'd':    
                      newBalance = float(curBalance) + float(amount)
                  else:
                      print("Invalid value for balance update")

                  delete_oldbal(user_account_number)
                                 
                  
              else:         
                  newBalance = 0           

       
def menuOptions(user_account_number, selectedOption):
    if (selectedOption == 1):  #Withdrawal
        userBalance = getCustomerBalance(user_account_number)
          #Update user balance in userBalance File  
        currency_string4 = "${:,.2f}".format(float(userBalance))
        print("Your current balance: %s" % currency_string4 )
        print()
        withdraw = input("How much would you like to withdraw? ")
        currency_string5 = "${:,.2f}".format(float(withdraw))
        
        if(float(userBalance) < float(withdraw)):
          print()
          print("Sorry but your balance is less than withdrawal")
          print()
          Transaction_Options(user_account_number)
        else:
          print("Withdrawing: %s" %currency_string5)
          print()  
          user_Balance = float(userBalance) - float(withdraw)
          currency_string6 = "${:,.2f}".format(float(user_Balance))
          print("Your new balance: %s" % currency_string6)
          print()
          print("Please take your cash.")
          print()
          dw = "w"

          UpdateUserBalance (user_account_number,userBalance,withdraw,dw)

          AddNewCustomerBalance(user_account_number,user_Balance,True)

        Transaction_Options(user_account_number)
            #********************************
    elif (selectedOption == 2):
          
          userBalance = getCustomerBalance(user_account_number)
          print()     
          currency_string4 = "${:,.2f}".format(float(userBalance))
          print("Your current balance: %s" % currency_string4 )
          print()
          deposit = input("How much would you like to deposit? ")
          currency_string5 = "${:,.2f}".format(float(deposit))
          print("Depositing: %s" %currency_string5)
          print()   

          curBalance = float(userBalance) + float(deposit)
          currency_string6 = "${:,.2f}".format(float(curBalance))
          print("Your new balance: %s" % currency_string6)
          print()
          
          dw = "d"

          UpdateUserBalance(user_account_number, curBalance, deposit,dw)
          
          AddNewCustomerBalance(user_account_number,curBalance,True)

          Transaction_Options(user_account_number)

    elif(selectedOption == 3):
          print()                      
          #What issue will you like to report? 
          complaint = input("What issue will you like to report?")
          # output "Thank you for contacting us"
          print()
          print( "Thank you for contacting us")
          print("Customer Service will be contact you within 3 working days.")
          print()
          Transaction_Options(user_account_number)      

    elif(selectedOption == 4):
          print()
          print("**** Thanks for banking with us. ****")
          print()
          removeInSession(user_account_number)
                   
    else:
          print()
          print("Invalid option selected, please try again")
          Transaction_Options(user_account_number)



newCustomer()

