# CTI-110
# P3HW1 - Color Mixer
# Levy, Anthony
# 2/20/2020
#

# Input first color
# Input second color
# If first color and second color makes a color
# Print color
# Else If second color and third color makes a color
# print color

print('Welcome to Tony\' (Anthony Levy) color mixer program!',
      'This program will let you input two colors and return what color they make.')

# Asking for colors
first_color = input('Enter a color. Red, Yellow, or Blue: ').lower()
second_color = input('Enter a second color: ').lower()

# Red if statement
if first_color == 'red':
    # Getting the second color the user inputs
    if second_color == 'blue':
        print('Mixing Red and Blue makes Purple.')
    elif second_color == 'yellow':
        print('Mixing Red and Yellow makes Orange.')
    elif second_color == 'red':
        print('Mixing Red and Red makes Red.')
    else:
        print('That color does not exist.')
# Blue else if statement
elif first_color == 'blue':
    # Getting the second color the user inputs
    if second_color == 'red':
        print('Mixing Blue and Red makes Purple.')
    elif second_color == 'yellow':
        print('Mixing Blue and Yellow makes Green.')
    elif second_color == 'blue':
        print('Mixing Blue with Blue makes Blue.')
    else:
        print('That color does not exist.')
# Yellow else if statement
elif first_color == 'yellow':
    # Getting the second color the user inputs
    if second_color == 'red':
        print('Mixing Yellow and Red makes Orange.')
    elif second_color == 'blue':
        print('Mixing Yellow and Blue makes Green.')
    elif second_color == 'yellow':
        print('Mixing Yellow and Yellow makes Yellow.')
    else:
        print('That color does not exist.')
else:
    print('That color does not exist.')
