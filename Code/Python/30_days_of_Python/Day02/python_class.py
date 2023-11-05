class employee:

    def __init__(self, first_name, last_name, age, profile, employee_level, brand_name, team, ctc):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profile = profile
        self.employee_level = employee_level
        self.brand_name = brand_name
        self.team = team
        self.ctc = ctc

    
def main():
    
    RPL37 = employee("Rutik","Patil",22,"Quality assurance engineer","Associate","Simulia","Automation",750000)
    print(RPL37.brand_name)

if __name__ == "__main__":
    main()