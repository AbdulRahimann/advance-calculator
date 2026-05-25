#################################
##     ADVANCE CALCULATOR      ##
#################################

class AdvancedCalculator:

    def add(self,a,b): #addition
        return a+b
    
    def subraction(self,a,b): #subraction
        return a-b

    def multiplication(self,a,b): #multiplication
        return a*b
    
    def division(self,a,b): #division
        try:
            return a/b
        except ZeroDivisionError:
            return "division by zero is not possible"
        
    def find_square_root(self,n): #square root
        if n<0:
            return "square root of negetive number is not possible"
        else:
            return n**0.5
        
    def find_factorial(self,n): #factorial
        if n==0:
            return 1
        else:
            return n*self.find_factorial(n-1)
        
    def find_power(self,base, exponent): #finding power
        return base**exponent
    
    def calculate_simple_intrest(self,principal, rate, time):
        return (principal*rate*time)/100
    
    def calculate_compound_intrest(self,principal, rate, time): 
        a=principal*(1+rate/100)**time
        return a-principal

    def find_n_th_root(self,A, n,e=1e-6):
        if A<0 and n%2==0:
            return "even root of negetive number is not possible"
        x=A/n

        while True:
            prev=x

            x=((n-1)*x+A/(x**(n-1)))/n

            if abs(prev-x)<e:
                break
        return x

    def compute_log_base_a_of_b(a, b):
        
        

if __name__=='__main__':
    c=AdvancedCalculator()
    while True:
        print("\n1.addition")
        print("2.subtraction")
        print("3.multiplication")
        print("4.division")
        print("5.find square root")
        print("6.find factorial")
        print("7.find power")
        print("8.calculate simple intrest")
        print("9.calculate compound intrest")
        print("10.n th root")
        print("11.compute log base a of b")
        print("12.exit")

        choice=int(input("\nenter your choice:"))
       
        if choice==1:
            a=int(input("enter first number:"))
            b=int(input("enter second number:"))
            print("\nresult:",c.add(a,b))

        elif choice==2:
            a=int(input("enter first number:"))
            b=int(input("enter second number:"))
            print(f"\nresult:{c.subraction(a,b)}")

        elif choice==3:
            a=int(input("enter first number:"))
            b=int(input("enter second number:"))
            print(f"\nresult:{c.multiplication(a,b)}")

        elif choice==4:
            a=int(input("enter first number:"))
            b=int(input("enter second number:"))
            print(f"\nresult: {c.division(a,b)}")

        elif choice==5:
            a=int(input("enter a number:"))
            print(f"result :{c.find_square_root(a)}")

        elif choice ==6:
            a=int(input("enter a number:"))
            print(f"result: {c.find_factorial(a)}")

        elif choice ==7 :
            a=int(input("enter base:"))
            b=int(input("enter exponent:"))
            print(f"result : {c.find_power(a,b)}")

        elif choice ==8:
            principal=int(input("enter principal amount:"))
            rate=float(input("enter intrest rate:"))
            time=int(input("enter time in years:"))
            print(f"the simple intrest is:{c.calculate_simple_intrest(principal,rate,time)}")

        elif choice ==9:
            principal=int(input("enter principal amount:"))
            rate=float(input("enter intrest rate:"))
            time=int(input("enter time in years:"))
            print(f"the compound intrest is :{c.calculate_compound_intrest(principal,rate,time)}")

        elif choice ==10:
            A=int(input("enter a number:"))
            n=int(input("enter the root:"))
            print(f"result: {c.find_n_th_root(A,n)}")

        elif choice ==11:
            break

        else:
            print("wrong command")






