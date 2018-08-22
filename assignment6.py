# q1. calculate area of a square
def Area():
    radius=float(input("Enter the radius of sphere"))
    area=(4*3.14*(radius**2))
    return area
a=Area()
print("Area of Sphere is :",a)



# q2. print all the perfect numbers between 1 and 1000

def perfect(n):
    c=0
    for j in range(1,n):
        if(n%j==0):
            c=c+j
    if(c==n):
        print(n)
for i in range(1,1001):
    perfect(i)

	
# q3. print multiplication table of a user defined number


def multi_table(n):
    for i in range(1,11):
        print("{}*{}=".format(n,i),(n*i))
n=int(input("enter number"))
multi_table(n)



# q4. calculate power of a number using recursion
a=int(input("enter first no."))
b=int(input("enter second no."))

def pow_(b):
    
    if(b==0):
        return 1
    else:
        return a*pow_(b-1)
    
print(pow_(b))
    
