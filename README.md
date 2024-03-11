
Morse Code File Transfer

This Python script facilitates data transfer using Morse code, intended to be interpreted by a decoder on a separate device. 
The decoded data can then be recompiled into the original file, enabling data transfer without the need for WiFi or physical transfer methods.

Overview

This script takes a file as input, converts it into Morse code audio signals, and plays them. 
The Morse code can be captured by a decoder on another device, which then decodes it back into base64 data. 
This base64 data can be recompiled into the original file.

How It Works

Input File: Provide the path to the input file. This could be any type of file (e.g., text, image, audio).

Hexdump: The script displays the hexdump of the input file. This gives a hexadecimal representation of the file's contents.

Base64 Conversion: The file is converted into base64 format, reducing the characters and time required for transmission.

Morse Code Generation: The base64 data is encoded into Morse code. Each character in the base64 data corresponds to a Morse code sequence.

Audio Playback: The Morse code is played as audio signals. Each Morse code sequence is represented by a combination of dots, dashes, and pauses.

Decoding: On the receiving end, the Morse code is captured and decoded back into base64 data.

Reconstruction: Finally, the base64 data is recompiled into the original file.

Limitations and Work in Progress

Case Sensitivity: Currently, upper and lower case characters are represented with the same sound in Morse code. This may cause ambiguity during decoding and is an area of ongoing improvement.
Usage
Clone the repository.
Ensure you have Python installed on your system.
Run the script and follow the prompts to provide the input file path.
