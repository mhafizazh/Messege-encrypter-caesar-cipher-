import caecar_function
from art import logo

print(logo)

program_run = True

while program_run == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caecar_function.caecar(text, shift, direction)
    answer = input("type 'y' to restart, type 'n' close program")
    if answer == 'y':
        program_run = True
    elif answer == 'n':
        program_run = False
        print('thanks')
    else:
        print('invalid input')


