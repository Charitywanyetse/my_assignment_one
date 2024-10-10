# question 3

#The volume of a sphere with radius r is (4/3)*pei*r**2
#what is the volume of a sphere with radius 5
#make sure the programme enters the radius from the keyboard and provide the answer in two decimal places.

#Answer

def volumeOfSphere():
    radius=int(input("Enter the radius of a sphere: "))
    pei=int(input("Enter the pei of a triangle: "))
    radius=(4/3) * pei * radius **2

    print(f"The voluma of a sphere {pei} and radius {radius} is {volumeOfSphere:.2f}")

