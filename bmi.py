from time import asctime

# prompt user for name
name = str( input( "Enter your name: " ) )

# prompt user for age and convert string to integer
age = int( input( "Enter your age: " ) )

# prompt user for weight in kilograms and
# convert it to floating number
weight = float( input( "Enter your weight in kilogram: " ) )

# prompt user for height in meters(m) and
# convert value to floating number
height = float( input( "Enter your height in meters: " ) )

# function that calculate bmi 
def bmi( height, weight ):
    ''' Calculates bmi '''
    return weight / ( height * height )

# display user information
# name, age, weight, height and bmi
print( "\nHello, " + name.lower().title() )
print( "Here is your results\n" )
print( "Name: " + name.lower().title() )
print( "Age: " + str(age) + " years old" )
print( "Weight: " + str(weight)+ "kg" )
print( "Height: " + str(height)+ "m")
print( "BMI:", "{:.1f}".format(bmi(height,weight)) + "\n" )

# Analysing data given by the user and
# display the result
if bmi(height, weight) < 18.5:
    print( "You are Underweight!" )
elif 18.5 <= bmi(height,weight) <= 24.9:
    print( "You are Normal!, Well Done!" )
elif 25.0 <= bmi(height,weight) <= 29.9:
    print( "You are Overweight!" )
if  bmi(height,weight) >= 30.0:
    print( "You are Obese!" )

# display the bmi value for comparison
print( "\n*********** BMI VALUES ************\n" +
       "* Underweight: less than 18.5     *\n*" +
       " Normal: between 18.5 and 24.9   *\n*" +
       " Overweight: between 25 and 29.9 *\n*" +
       " Obese: 30 or greater            *\n" +
       "***********************************" )

# option to save users information
save_info = input("Would you like to save your results? ")

if save_info.lower() == "yes" or save_info.lower() == "y":
    # save user data into a file
    with open("data.txt", "a") as saved_data:
        saved_data.write("Saved on: " + asctime()+ "\n")
        saved_data.write("Name: " + name.title() + "\n")
        saved_data.write("Age: " + str(age) + " years old\n")
        saved_data.write("Weight: " + str(weight) + "kg\n")
        saved_data.write("Height: " + str(height) + "m\n")
        saved_data.write("BMI: {:.1f}".format(bmi(height,weight)) + "\n\n")
    print("Results Saved\n")

