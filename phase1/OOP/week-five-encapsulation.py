class Bank:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        self._branch = "East st. branch"
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print(f"Entered amount is {amount}. Please enter valid amount.")
        
    
# b = Bank("Ravi", 12000)

# print(b.get_balance())
# b.deposit(3000)
# print(b.get_balance())

# # print(b.__balance)
# print(b._Bank__balance)  #name mangling

class School:

    def __init__(self, reg_id):
        self.name = "MIL Public School"
        self._reg_id = reg_id
        self.__no_staff = 90
        self.__total_stds = 376
        self.rank = "2nd"
        self.pass_count = 345
    
    def get_school_name(self):
        return self.name

    def _get_no_of_staff(self):
        return self.__no_staff
    
    def __get_total_stds(self):
        return self.__total_stds

    def set_overall_pass_count(self, new_pass_count):
        if new_pass_count <=  self.__total_stds:
            self.pass_count = new_pass_count
            return self.pass_count
        else:
            return f"Please enter correct value! you have entered {new_pass_count}"

    def get_overall_result(self):
        return (self.pass_count/self.__total_stds)*100
    
    
class Classes(School):

    def __init__(self, class_name, reg_id):
        super().__init__(reg_id)
        # self.no_classes = no_classes
        self.class_name = class_name
    
    def __get_no_of_std_per_class(self):

        class_details = {
            "1st class": 45,
            "2nd Class": 39,
            "3rd Class": 44,
            "4th Class": 41,
            "5th Class": 55,
            "6th Class": 33,
            "7th Class": 30,
            "8th Class": 44,
            "9th Class": 45
        }

        return class_details[self.class_name]
    

c = Classes("1st Classs", 122345)

# print(c._School__get_total_stds())
# print(c._get_no_of_staff())
# c.set_overall_pass_count(376)
# print(c.get_overall_result())


