
#!/usr/bin/python3
# GeekTechStuff (original)
# Modified by Timo Kosse


“””
To find out more about the Vigenère Cipher please visit: https://geektechstuff.com/2019/12/25/vigenere-cipher/
“””


def vigenere_enc():
    alphabet = “abcdefghijklmnopqrstuvwxyz”
    input_string = “”
    enc_key = “”
    enc_string = “”

    # Vraagt om encryptie sleutel
    enc_key = input(“Please enter encryption key: “)
    enc_key = enc_key.lower()

    # Neemt een text van de user
    input_string = input(“Please enter a string of text: “)
    input_string = input_string.lower()

    # berekent de lengte van de text
    string_length = len(input_string)

    # Maakt een expanded key die langer wordt gemaakt dan de ingevoerde text
    expanded_key = enc_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        # Herhaald de encryptie sluitel en plakt deze achteraan
        expanded_key = expanded_key + enc_key
        expanded_key_length = len(expanded_key)

    key_position = 0

    for letter in input_string:
        if letter in alphabet:
            # Berekend van elke letter de waarde in het alfabet
            position = alphabet.find(letter)

            # Gaat alle cijfers bijlangs
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            # Past het orgineel aan op het getal
            new_position = position + key_character_position
            if new_position > 26:
                new_position = new_position – 26
            new_character = alphabet[new_position]
            enc_string = enc_string + new_character
        else:
            enc_string = enc_string + letter
        return(enc_string)


def vigenere_dec():
    alphabet = “abcdefghijklmnopqrstuvwxyz”
    input_string = “”
    dec_key = “”
    dec_string = “”

    # Vraagt om encryptie sleutel
    dec_key = input(“Please enter encryption key: “)
    dec_key = dec_key.lower()

    # Neemt een text van de user
    input_string = input(“Please enter a string of text: “)
    input_string = input_string.lower()

    # berekent de lengte van de text
    string_length = len(input_string)

    # Maakt een expanded key die langer wordt gemaakt dan de ingevoerde text
    expanded_key = dec_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        # Herhaald de encryptie sluitel en plakt deze achteraan
        expanded_key = expanded_key + dec_key
        expanded_key_length = len(expanded_key)

    key_position = 0

    for letter in input_string:
        if letter in alphabet:
            # Berekend van elke letter de waarde in het alfabet
            position = alphabet.find(letter)
            # Gaat alle cijfers bijlangs
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            # Past het orgineel aan op het getal
            new_position = position – key_character_position
            if new_position > 26:
                new_position = new_position + 26
            new_character = alphabet[new_position]
            dec_string = dec_string + new_character
        else:
            dec_string = dec_string + letter
    return(dec_string)

# Testen
print(vigenere_enc())
print(vigenere_dec())
