'''
Class Variables and Class mathods
'''
class Bank:
    bank_name = "Global Trust Bank"  # Class variable

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name


if __name__ == "__main__":
    # Create initial instances
    branch1 = Bank()
    branch2 = Bank()
    
    print("Initial names:")
    print(f"Branch 1: {branch1.bank_name}")  
    print(f"Branch 2: {branch2.bank_name}")  
    
    # Change bank name using class method
    Bank.change_bank_name("Worldwide Financial Group")
    
    # Create new instance after name change
    branch3 = Bank()
    
    print("\nAfter name change:")
    print(f"Branch 1: {branch1.bank_name}")  
    print(f"Branch 2: {branch2.bank_name}")   
    print(f"New Branch 3: {branch3.bank_name}") 
