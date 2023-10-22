import string

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

alphabet_uppercase = string.ascii_uppercase
alphabet_lowercase = string.ascii_lowercase

def encrypt(original_text, number_shift):
    encrypt_txt = ''
    for char in original_text:
        if char in alphabet_uppercase:
            original_position = alphabet_uppercase.index(char)
            encrypt_position = original_position + number_shift
            while encrypt_position >= 26:
                encrypt_position = encrypt_position % 26
            encrypt_txt += alphabet_uppercase[encrypt_position]
        elif char in alphabet_lowercase:
            original_position = alphabet_lowercase.index(char)
            encrypt_position = original_position + number_shift
            while encrypt_position >= 26:
                encrypt_position = encrypt_position % 26
            encrypt_txt += alphabet_lowercase[encrypt_position]
        else:
            encrypt_txt += char
    # print(encrypt_txt)
    return encrypt_txt



def decoded(encrypted_text, shift):
    unencrypted_txt = ''
    for char in encrypted_text:
        if char in alphabet_uppercase:
            encrypted_position = alphabet_uppercase.index(char)
            unencrypted_position = encrypted_position - shift
            if unencrypted_position < 0:
                unencrypted_position = unencrypted_position % 26
            unencrypted_txt += alphabet_uppercase[unencrypted_position]
        elif char in alphabet_lowercase:
            encrypted_position = alphabet_lowercase.index(char)
            unencrypted_position = encrypted_position - shift
            if unencrypted_position < 0:
                unencrypted_position = unencrypted_position % 26
            unencrypted_txt += alphabet_lowercase[unencrypted_position]
        else:
            unencrypted_txt += char
    return unencrypted_txt



# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# caecar(text, shift, direction)}
