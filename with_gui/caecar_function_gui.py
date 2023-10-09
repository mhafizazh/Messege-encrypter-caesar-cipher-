alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']


def encrypt(original_text, number_shift):
    encrypt_txt = ''
    for char in original_text:
        if char in alphabet:
            original_position = alphabet.index(char)
            encrypt_position = original_position + number_shift
            encrypt_txt += alphabet[encrypt_position]
        else:
            encrypt_txt += char
        if encrypt_position > 26:
            encrypt_position = encrypt_position % 26
    print(encrypt_txt)
    return encrypt_txt


def decoded(encrypted_text, number_shift):
    unencrypted_txt = ''
    for char in encrypted_text:
        if char in alphabet:
            encrypted_position = alphabet.index(char)
            unencrypted_position = encrypted_position - number_shift
            if unencrypted_position < 0:
                unencrypted_position = unencrypted_position + 26
            unencrypted_txt += alphabet[unencrypted_position]
        else:
            unencrypted_txt += char
    print(unencrypted_txt)
    return unencrypted_txt



# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# caecar(text, shift, direction)}
