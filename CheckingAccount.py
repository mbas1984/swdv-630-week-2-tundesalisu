class CheckingAccount:
    def __init__(self, name, address,accountNumber,balance):
        self.name = name
        self.address = address
        self.__accountNumber = accountNumber
        self.__balance = balance



    
    def withdraw(self,amount):
        self.__balance -=amount
        
    def deposit(self,amount):
        self.__balance += amount
        
    def __str__(self):
        return f"{self.name} address is {self.address} with account number #{self.__accountNumber} and Balance ${self.__balance}  "


def main():
  account1 = CheckingAccount("Bob Joe","123 krispy road",2345678,4000)
  print(account1)
  account1.withdraw(2000)
  print(account1)
  account1.deposit(10000)
  print(account1)
 
  
main()