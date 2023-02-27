while True:
    try:
        bmi_height = float(input("Enter the height of customer in centimeters : "))
        bmi_weight =  float(input("Enter the weight of customer in kilograms : "))
    except ValueError:
        print("Invalid input. Please input numbers.\n")
        exit()
    if bmi_height<=0 or bmi_weight<=0:
        print("Negative values are not accepted")
        continue
    else:
        break
    bmi_height = bmi_height/100

    bmi = bmi_weight / (bmi_height * bmi_height)

    print(bmi)

    if bmi < 18.5:
        print(f"The bmi of the person is {bmi:.2f} and it is Underweight")
    elif bmi >= 18.5 and bmi < 25:
        print(f"The bmi of the person is {bmi:.2f} and it is Normal")
    elif bmi >= 25 and bmi < 30:
        print(f"The bmi of the person is {bmi:.2f} and it is Overweight")
    else:
        print(f"The bmi of the person is {bmi:.2f} and it is Obese")
