# question 2 

#Create a programme to calculate the area of a triangle(1/2 * base * height)
#base and height should be entered from the keyboard.

#Answer

def areaOfTriangle():

    base = int(input("Enter the base of a triangle: "))
    height = int(input("Enter the height of the triangle: "))

    area = (1/2) * base * height

    print(f"The area of a triangle of base {base} and height {height} is {area:.2f}") 
