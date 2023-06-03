print("Welcome to Body-Mass Index Calculation")

#Your Datas
weight = input("Enter Your Weight = ")
height = input("Enter Your Height (cm form) = ")

if not bool(weight) or not bool(height):
    print("Incorrect entry !!!")
    exit()

weight = float(weight)
height = float(height)

height = height/100

result = weight/(height**2)

print("Weight : {}\nHeight : {} (m)\nYour Body-Mass Index = {}".format(weight,height,result))




if result < 18.5:
    print("Weak")

elif result >= 18.5 and result < 25:
    print("Normal")

elif result >= 25 and result <= 30:
    print("Overweight")

elif result > 30:
    print("Obese")





