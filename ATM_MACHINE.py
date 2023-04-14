#!/usr/bin/env python
# coding: utf-8

# ![SBI%20logo.png](attachment:SBI%20logo.png)

# In[1]:


import getpass as get            ## To hide pin

class Atm:            
    
    
    def __init__(self):
        self.pin=""
        self.balance=0 
        self.wrong_pin_count = 0
        self.display()
        self.menu()
        
        
    def display(self):
        print("****************************************************************************")
        print("*                                                                          *")
        print("*                         WELCOME to SBI ATM                               *")
        print("*                                                                          *")
        print("****************************************************************************")
        
        
    def menu(self):
        try:
            user_input = input("""
                HELLO, PLEASE ENTER YOUR TRANSACTION CHOICE?
                *******************************************        
                    1. ENTER 1 TO CREATE PIN
                    2. ENTER 2 TO DEPOSIT
                    3. ENTER 3 TO WITHDRAW
                    4. ENTER 4 TO CHECK BALANCE
                    5. ENTER 5 to EXIT  
                *******************************************\n   
                          """)
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                
                print("****************************************************************************")
                print("*                                                                          *")
                print("*                         THANKYOU FOR USING ATM                           *")
                print("*                                                                          *")
                print("****************************************************************************") 
                exit()   
            else:
                raise ValueError("\n************INVALID INPUT************")
        except ValueError as e:
            print(str(e))
            self.menu()
            
            
    def create_pin(self):
        try:
            self.pin = str(int(get.getpass("CREATE YOUR PIN: ")))
            if len(self.pin) != 4:
                raise ValueError
            print("\n************PIN SET SUCCESSFULLY************")
            self.continue_or_exit() 
        except ValueError as e:
            print(str("\n************PIN MUST BE 4 DIGITS AND INTEGER************"))
            self.create_pin()
    
    
    def deposit(self):
        if self.pin != "":
            try:
                pin_input = str(int(get.getpass("ENTER YOUR PIN: ")))
                if pin_input == self.pin:
                    amount = int(input("ENTER AMOUNT TO DEPOSIT: "))
                    if amount<100:
                        raise ValueError("\n************AMOUNT SHOULD BE GREATER THAN OR EQUAL TO 100************")
                    elif amount>50000: 
                        raise ValueError("\n************AMOUNT SHOULD BE LESS THAN OR EQUAL TO 50000************")   
                    self.balance += amount
                    print("\n************DEPOSIT SUCCESSFUL************")
                    self.continue_or_exit()
                else:
                    print("\n************INCORRECT PIN************")
                    self.handle_wrong_pin()        
            except ValueError as e:
                print(str(e))
                self.deposit()
        else:
            print("\n************YOU MUST CREATE A PIN BEFORE MAKING A DEPOSIT************")
            self.menu()
            
            
    def withdraw(self):
        if self.pin != "":
            try:
                pin_input = str(int(get.getpass("ENTER YOUR PIN: ")))
                if pin_input == self.pin:
                    amount = int(input("ENTER AMOUNT TO WITHDRAW: "))
                    if amount < 100:
                        raise ValueError("\n************AMOUNT SHOULD BE GREATER THAN OR EQUAL TO 100************")
                    elif amount>25000:
                        raise ValueError("\n************AMOUNT SHOULD BE LESS THAN OR EQUAL TO 25000************")
                        
                    elif amount <= self.balance:
                        self.balance -= amount
                        print("\n************WITHDRAWAL SUCCESSFUL************")
                        self.continue_or_exit() 
                    else:
                        print("\n************INSUFFICIENT BALANCE AND YOUR CURRENT BALANCE IS" ,self.balance,"************")
                        self.continue_or_exit()
                else:
                    print("\n************INCORRECT PIN************")
                    self.handle_wrong_pin()  
            except ValueError as e:
                print(str(e))
                self.withdraw()
        else:
            print("\n************YOU MUST CREATE A PIN BEFORE MAKING A WITHDRAWAL************ ")
            self.menu()
        
        
    def check_balance(self):
        if self.pin != "":
            try:
                pin_input = str(int(get.getpass("ENTER YOUR PIN: ")))
                if pin_input == self.pin:
                    print(f"\n************YOUR BALANCE IS {self.balance}************")
                    self.continue_or_exit()
                else:
                    print("\n************INCORRECT PIN************")
                    self.handle_wrong_pin()     
            except ValueError as e:
                print(str(e))
                self.check_balance()
        else:
            print("\n************YOU MUST CREATE A PIN BEFORE CHECKING YOUR BALANCE************")
            self.menu()
            
            
    def continue_or_exit(self):
        try:
            user_input1 = input("\nENTER 1 TO CONTINUE, or 2 TO EXIT: ")
            if user_input1 == "1":
                self.menu()   
            elif user_input1 == "2":
                print("****************************************************************************")
                print("*                                                                          *")
                print("*                         THANKYOU FOR USING ATM                           *")
                print("*                                                                          *")
                print("****************************************************************************")
                exit()
            else:
                raise ValueError("\n************INVALID INPUT************")
        except ValueError as e:
            print(str(e))
            self.continue_or_exit()
            
            
    def handle_wrong_pin(self):
        self.wrong_pin_count += 1
        if self.wrong_pin_count >= 3:
            print("\nYOU HAVE ENTERED WRONG PIN 3 TIMES. THIS ATM CARD HAS BEEN BLOCKED.\nPLEASE CONTACT CUSTOMER CARE SERVICE.")
        else:
            print(f"\n************YOU HAVE {3 - self.wrong_pin_count} ATTEMPTS REMAINING************")
            self.menu()
           
        


# In[2]:


sbi=Atm()


# In[ ]:




