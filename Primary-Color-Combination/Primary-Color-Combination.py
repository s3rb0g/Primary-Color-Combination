def verify(primary_color):
    note = 0
    if primary_color.lower() == 'red':
        note += 1
    elif primary_color.lower() == 'blue':
        note += 2
    elif primary_color.lower() == 'green':
        note += 4
    else:
        print('\n' + primary_color + ' is not a primary color.\n')
        exit()
    return note
        
def combine(color):
    mix = ""
    if color == 2:
        mix = "Red"
    elif color == 3:
        mix = "Violet"
    elif color == 5:
        mix = "Yellow"
    elif color == 4:
        mix = "Blue"
    elif color == 6:
        mix = "Cyan"
    elif color == 8:
        mix = "Green"
    return mix
  
print('\nEnter the colors you want to mix.')
first_color = input('Enter first color: ')
second_color = input('Enter second color: ')

num = verify(first_color) + verify(second_color)
result = combine(num)

print('\n' + first_color + ' + ' + second_color + ' = ' + result + '\n')
