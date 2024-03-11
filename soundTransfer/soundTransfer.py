import os
import base64
import pygame
import subprocess
#create a hexdump of the file
def hexdump(file_path):
    with open(file_path, 'rb') as file:
        hex_data = file.read().hex()
        hex_dump = '\n'.join([hex_data[i:i+32] for i in range(0, len(hex_data), 32)])
        print(hex_dump)
        #convert file to base64 to reduce characters and time
def convert_to_base64(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        base64_data = base64.b64encode(data)
        return base64_data.decode('utf-8')
    #function to play the sound 
def play_morse_code(morse_code):
    pygame.mixer.init()
    for char in morse_code: #.wait times can be adjust to increase speed of transfer
        if char == '.':
            pygame.mixer.Sound('dot.wav').play()
            pygame.time.wait(100)  
        elif char == '-':
            pygame.mixer.Sound('dash.wav').play()
            pygame.time.wait(300) 
        elif char == ' ':
            pygame.time.wait(300)
        elif char == '/':
            pygame.time.wait(700) 
            
            #dictionary of all base64 characters
def encode_to_morse_code(base64_data):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '=': '-...-', '+': '.-.-.', '/': '-..-.', '?': '..--..', '.': '.-.-.-', ',': '--..--', ':': '---...',
        ';': '-.-.-.', '(': '-.--.', ')': '-.--.-', '[': '-.--.', ']': '-.--.-', '{': '-.--.', '}': '-.--.-',
        '-': '-....-', '_': '..--.-', '"': '.-..-.', "'": '.----.', '!': '-.-.--', '@': '.--.-.', ' ': '/'
    }
    #take each character in base64 outpu5 and convert to morse
    morse_code = ''
    for char in base64_data:
        if char.upper() in morse_code_dict:
            morse_code += morse_code_dict[char.upper()] + ' '
    return morse_code

if __name__ == "__main__":
    input_file = input("Enter the path to the input file: ")
    if not os.path.exists(input_file):
        print("File not found.")
        exit()

    #Display original hexdump
    print("\nHexdump:")
    hexdump(input_file)

    #Display base64 form
    base64_data = convert_to_base64(input_file)
    print("\nBase64:")
    print(base64_data)

    #base64 encoded into morse code
    morse_code = encode_to_morse_code(base64_data)
    print("\nMorse Code:")
    print(morse_code)

    #Play morse code audio
    play_morse_code(morse_code)
