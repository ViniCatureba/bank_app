



from unicodedata import decomposition


class User():
    def __int__(self, Name, Age, CPF,account_num):
        self.name = Name
        self.Age = Age
        self.CPF = CPF
        self.account_num = account_num 

    def Show_ppl_details(self):
        print("------------------------------------- Account details: -------------------------------- ")
        print(f"Name: {self.name}")
        print(f"Account number: {self.account_num}")
        print(f"Age: {self.Age}")
        print(f"CPF: {self.CPF}")



class Bank(User):
    def __init__(self, Name, Age, CPF,account_num):
        super().__init__( Name, Age, CPF,account_num)
        self.balance = 0


    def deposit(self,amount_dep):
        self.amount = amount_dep
        self.balance = self.balance + amount_dep
        print(f"${amount_dep} was succesfully deposited")
        print('Your new balance is {self.balance}')
    def main():



    






        


