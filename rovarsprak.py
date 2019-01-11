import os
import time

#consonant list with both upper and lowercase letters
consonant_lower_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's'
                       ,'t', 'v', 'x', 'z']
consonant_list = [consonant.upper() for consonant in consonant_lower_list] + consonant_lower_list

#decode function that will counter the encoding algorithm
def decode(user_input):
    decoded_text=list(user_input)
    for i in range(len(decoded_text)):
        for x in range(len(consonant_list)):
            if decoded_text[i] == consonant_list[x]:
                #counter algorithm removes the duplicate consonant and the 'o'
                decoded_text[i + 1] = ''
                decoded_text[i + 2] = ''
    return ''.join(decoded_text)

#encode function that will encode the string with provided algorithm
def encode(user_input):
    encoded_text = list(user_input)
    for i in range(len(encoded_text)):
        for x in range(len(consonant_list)):    
            if encoded_text[i] == consonant_list[x]:
                #algorithm will take the consonant, duplicate it and add a 'o' between the consonant that was duplicated
                encoded_text[i] = encoded_text[i] + 'o' + encoded_text[i].lower()
    return ''.join(encoded_text)

#auto detection if the string provided is encrypted or not
def is_encoded(user_input):
    try:
        decode(user_input)
        is_encoded_text = list(user_input)
        for i in range(len(is_encoded_text)):
            for x in range(len(consonant_list)):
                if is_encoded_text[i + 1] == 'o' and is_encoded_text[i + 2] == is_encoded_text[i]:
                    return True
                else:
                    return False
    except IndexError:
        return False

#Useless function that just adds some stuff for users to follow along the program
def styling_func(sequence, user_input):
    user_input = str(sequence)
    if user_input.upper() == 'ENCODING':
        print(f"Encoding not found!")
    elif user_input.upper() == 'DECODING':
        print(f"Encoding found!")
    time.sleep(1)
    print(f"Starting {sequence} sequence!")
    time.sleep(1.5)
    os.system("cls")
    meme_string = user_input
    for i in range(0, 6):
        print(meme_string)
        meme_string = meme_string + '.'
        time.sleep(len(user_input) * 0.015)
        os.system("cls")

os.system("cls")
user_input = input("Input string to encode / decode: ")

#ask if the user wants a file to save the results
write_to_file = input("Would you like to create a text file with the results? (Y/N): ")

#if the auto detection fails to find any encryption it will run the encryption on the string provided
if is_encoded(user_input) == False:
    styling_func('Encoding', user_input)
    encoded_text = encode(user_input)
    decoded_text = ''
    enc_or_dec = "ENCODED: "
    print(f"ORIGINAL: {user_input}\nENCODED: {encoded_text}")
#if the auto detection successfully finds a encryption it will run the decryption on the string provided
elif is_encoded(user_input) == True:
    styling_func('Decoding', user_input)
    decoded_text = decode(user_input)
    encoded_text = ''
    enc_or_dec = "DECODED: "
    print(f"ORIGINAL: {user_input}\nDECODED: {decoded_text}")

#check if the user wanted to create a file to save results
if write_to_file.upper() == 'Y':
    #create a file and write the results to that file
    f = open("results.txt", 'w')
    f.write(f"--RESULTS--\n{enc_or_dec}{''.join(encoded_text)}{''.join(decoded_text)}")
    print("\nFILE WITH RESULTS CREATED IN CURRENT DIRECTORY! (results.txt)")

print("\nOperation successfully completed!")