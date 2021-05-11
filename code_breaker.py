import random
import re

class Code_breaker:
    def __init__ (self, text_input, affine, atbash, baconian, base64, bifid, ceaser, ceaser_keyed, caeser_rot13, column_trans, column_trans_double, column_trans_ubchi, cryptogram, gronsfeld, morse, numbers, one_time_pad, playfair, railfence, rotate, skip, substitution, vigenere,  vigenere_eyed, vigenere_autokey, all_codes):
        #where users input text to be decrypted
        self.text_input = text_input
        #types of encrytption to be decoded
        self.affline = affine #
        self.atbash = atbash #
        self.baconian = baconian #
        self.base64 = base64 #
        self.bifid = bifid #
        self.ceaser = ceaser #
        self.ceaser_keyed = ceaser_keyed #
        self.caeser_rot13 = caeser_rot13 #
        self.column_trans = column_trans #
        self.column_trans_double = column_trans_double #
        self.column_trans_ubchi = column_trans_ubchi #
        self.cryptogram = cryptogram #
        self.gronsfeld = gronsfeld #
        self.morse = morse #
        self.numbers = numbers #
        self.one_time_pad = one_time_pad #
        self.playfair = playfair #
        self.railfence = railfence #
        self.rotate = rotate #
        self.skip = skip #
        self.substitution = substitution #
        self.vigenere = vigenere
        self.vigenere_eyed = vigenere_eyed #
        self.vigenere_autokey = vigenere_autokey #
        self.all_codes = all_codes #
    def text_input():
        text_to_decode = input ("What is your text to decode? ")
        what_cipher = input ("What type of cipher do you think it is? ")
        if what_cipher == "affine":
            Code_breaker.affine (text_to_decode)
        elif what_cipher == "atbash":
            Code_breaker.atbash (text_to_decode)
        elif what_cipher == "ceaser":
            Code_breaker.ceaser (text_to_decode)
    def affine(text_to_decode):
        print(text_to_decode)
        print(" test passed")
        """
    def atbash(text_to_decode):
        lookup_table = {'a' : 'z', 'b' : 'y', 'c' : 'x', 'd' : 'w', 'e' : 'v',
        'f' : 'u', 'g' : 't', 'h' : 's', 'i' : 'r', 'j' : 'q',
        'k' : 'p', 'l' : 'o', 'm' : 'n', 'n' : 'm', 'o' : 'l',
        'p' : 'k', 'q' : 'j', 'r' : 'i', 's' : 'h', 't' : 'g',
        'u' : 'f', 'v' : 'e', 'w' : 'd', 'x' : 'c', 'y' : 'b', 'z' : 'a'}
        for k,v in lookup_table:
            text_to_decode = text_to_decode.replace(k,v)
        print(text_to_decode)
        """
    def atbash(text_to_decode):
        lookup_table = {'a' : 'z', 'b' : 'y', 'c' : 'x', 'd' : 'w', 'e' : 'v',
        'f' : 'u', 'g' : 't', 'h' : 's', 'i' : 'r', 'j' : 'q',
        'k' : 'p', 'l' : 'o', 'm' : 'n', 'n' : 'm', 'o' : 'l',
        'p' : 'k', 'q' : 'j', 'r' : 'i', 's' : 'h', 't' : 'g',
        'u' : 'f', 'v' : 'e', 'w' : 'd', 'x' : 'c', 'y' : 'b', 'z' : 'a'}
        cipher = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher += lookup_table[letter]
            else:
                cipher += ' '
        print(cipher)
        return Code_breaker.text_input()
    def ceaser(text_to_decode):
        header = "SHIFT         SOLVE"
        print(header)
        ceaser_shift1 = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}
        cipher1 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher1 += ceaser_shift1[letter]
            else:
                cipher1 += ' '
        print("1            " + cipher1)
        ceaser_shift2 = {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l', 'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 'o': 'q', 'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v', 'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a', 'z': 'b'}
        cipher2 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher2 += ceaser_shift2[letter]
            else:
                cipher2 += ' '
        print("2            " + cipher2)
        ceaser_shift3 = {'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h', 'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm', 'k': 'n', 'l': 'o', 'm': 'p', 'n': 'q', 'o': 'r', 'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w', 'u': 'x', 'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b', 'z': 'c'}
        cipher3 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher3 += ceaser_shift3[letter]
            else:
                cipher3 += ' '
        print("3            " + cipher3)
        ceaser_shift4 = {'a': 'e', 'b': 'f', 'c': 'g', 'd': 'h', 'e': 'i', 'f': 'j', 'g': 'k', 'h': 'l', 'i': 'm', 'j': 'n', 'k': 'o', 'l': 'p', 'm': 'q', 'n': 'r', 'o': 's', 'p': 't', 'q': 'u', 'r': 'v', 's': 'w', 't': 'x', 'u': 'y', 'v': 'z', 'w': 'a', 'x': 'b', 'y': 'c', 'z': 'd'}
        cipher4 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher4 += ceaser_shift4[letter]
            else:
                cipher4 += ' '
        print("4            " + cipher4)
        ceaser_shift5 = {'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j', 'f': 'k', 'g': 'l', 'h': 'm', 'i': 'n', 'j': 'o', 'k': 'p', 'l': 'q', 'm': 'r', 'n': 's', 'o': 't', 'p': 'u', 'q': 'v', 'r': 'w', 's': 'x', 't': 'y', 'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c', 'y': 'd', 'z': 'e'}
        cipher5 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher5 += ceaser_shift4[letter]
            else:
                cipher5 += ' '
        print("5            " + cipher5)
        ceaser_shift6 = {'a': 'g', 'b': 'h', 'c': 'i', 'd': 'j', 'e': 'k', 'f': 'l', 'g': 'm', 'h': 'n', 'i': 'o', 'j': 'p', 'k': 'q', 'l': 'r', 'm': 's', 'n': 't', 'o': 'u', 'p': 'v', 'q': 'w', 'r': 'x', 's': 'y', 't': 'z', 'u': 'a', 'v': 'b', 'w': 'c', 'x': 'd', 'y': 'e', 'z': 'f'}
        cipher6 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher6 += ceaser_shift4[letter]
            else:
                cipher6 += ' '
        print("6            " + cipher6)

        return Code_breaker.text_input()

Code_breaker.text_input()