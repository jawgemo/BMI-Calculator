name = input( 'Hi!,What is your name?: ')
print( 'Hi ' + name + '!')
brith_year = input ('What is your birth year?: ')
age = 2023 - int(brith_year)
print(f' age: {age}')
height_cm = input('What is your height in CM?: ')
height_m =float(height_cm) / 100
print(f' height: {height_m}' f' m')
weight_kg= input('What is your weight in KG?: ')
print(f' weight: {weight_kg}' f' kg')
BMI = int(weight_kg) / (int(height_cm)/100)**2
print(f'BMI: {BMI}')
if age == 16:
    if BMI <= 18.5:
        print('You are underweight')
    elif BMI <= 24.9:
        print('You are healthy')
    elif BMI <= 29.9:
        print('You are overweight')
    else:
        print('You are obese')
if age ==17:
    if BMI <=18.5:
        print('You are underweight')
    if BMI >=18.5 and BMI <=24.9:
        print('You are healthy')
    if BMI >=25 and BMI<=29.9:
        print('You are overweight')
    if BMI>=30:
        print('You are obese')
