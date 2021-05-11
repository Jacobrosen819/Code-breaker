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

Code_breaker.text_input()