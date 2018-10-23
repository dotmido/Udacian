class Enrollment:
    def __init__(self,enrollstring):
        self.enrollstring = enrollstring
        
class Udacian:

    def __init__(self,name,city,enrollment,nanodegree,status):
        self.name = name
        self.city = city
        self.enrollment = Enrollment('Cohort2')
        self.nanodegree = nanodegree
        self.status = status
        


    def print_udacian(self):
        name = input("What is your name?: ")
        city = input("Located: ")
        enrollment = Enrollment(input("Enrollment?: "))
        nanodegree = input("Which Nanodegree?: ")
        currentstatus = input("Status: ")

        print("This is "+name+" from "+city+" is already "+currentstatus+" in "+enrollment.enrollstring+" "+nanodegree)



if __name__ == '__main__':
    #print to terminal
    udacian1 = Udacian('Mohammed','Riyadh','Full Stack','FSND','Active')
    udacian1.print_udacian()
    del udacian1
    