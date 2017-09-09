class Account:
    def __init__(self,id=0,balance=100,annual_interest_rate=0):
        self.__id=id
        self.__balance=balance
        self.__annual_interest_rate=annual_interest_rate
    def get_balance(self):
        return self.__balance
    def set_balance(balance):
        self.__balance=balance
    def set_id(id):
        self.__id=id
    def get_id(self):
        return self.__id
    def get_annual_interest_rate():
        return annual_interest_rate
    def set_annual_interest_rate(annual_interest_rate):
        self.__annual_interest_rate=annual_interest_rate
    def get_monthly_interest_rate(self):
        return self.__annual_interest_rate/1200
    def get_monthly_interest(self):
        return self.__balance*self.get_monthly_interest_rate()
    def withdraw(self,amount):
        self.__balance=self.__balance-amount
    def deposit(self,amount):
        self.__balance=self.__balance+amount    

def main():
    a=Account(1122,20000,4.5)
    a.withdraw(2500)
    a.deposit(3000)
    print("ID is: ",a.get_id())
    print("The Balance is: ",a.get_balance())
    print("Monthly interest rate is: ",a.get_monthly_interest_rate())
    print("Monthly interest is: ",a.get_monthly_interest())

main()