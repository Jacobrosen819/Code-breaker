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
        text_to_decode = text_to_decode.lower()
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
        ceaser_shift0 = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}
        cipher0 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher0 += ceaser_shift0[letter]
            else:
                cipher0 += ' '
        print("0            " + cipher0)
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
                cipher5 += ceaser_shift5[letter]
            else:
                cipher5 += ' '
        print("5            " + cipher5)
        ceaser_shift6 = {'a': 'g', 'b': 'h', 'c': 'i', 'd': 'j', 'e': 'k', 'f': 'l', 'g': 'm', 'h': 'n', 'i': 'o', 'j': 'p', 'k': 'q', 'l': 'r', 'm': 's', 'n': 't', 'o': 'u', 'p': 'v', 'q': 'w', 'r': 'x', 's': 'y', 't': 'z', 'u': 'a', 'v': 'b', 'w': 'c', 'x': 'd', 'y': 'e', 'z': 'f'}
        cipher6 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher6 += ceaser_shift6[letter]
            else:
                cipher6 += ' '
        print("6            " + cipher6)

        ceaser_shift7 = {'a': 'h', 'b': 'i', 'c': 'j', 'd': 'k', 'e': 'l', 'f': 'm', 'g': 'n', 'h': 'o', 'i': 'p', 'j': 'q', 'k': 'r', 'l': 's', 'm': 't', 'n': 'u', 'o': 'v', 'p': 'w', 'q': 'x', 'r': 'y', 's': 'z', 't': 'a', 'u': 'b', 'v': 'c', 'w': 'd', 'x': 'e', 'y': 'f', 'z': 'g'}
        cipher7 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher7 += ceaser_shift7[letter]
            else:
                cipher7 += ' '
        print("7            " + cipher7)
        ceaser_shift8 = {'a': 'i', 'b': 'j', 'c': 'k', 'd': 'l', 'e': 'm', 'f': 'n', 'g': 'o', 'h': 'p', 'i': 'q', 'j': 'r', 'k': 's', 'l': 't', 'm': 'u', 'n': 'v', 'o': 'w', 'p': 'x', 'q': 'y', 'r': 'z', 's': 'a', 't': 'b', 'u': 'c', 'v': 'd', 'w': 'e', 'x': 'f', 'y': 'g', 'z': 'h'}
        cipher8 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher8 += ceaser_shift8[letter]
            else:
                cipher8 += ' '
        print("8            " + cipher8)
        ceaser_shift9 = {'a': 'j', 'b': 'k', 'c': 'l', 'd': 'm', 'e': 'n', 'f': 'o', 'g': 'p', 'h': 'q', 'i': 'r', 'j': 's', 'k': 't', 'l': 'u', 'm': 'v', 'n': 'w', 'o': 'x', 'p': 'y', 'q': 'z', 'r': 'a', 's': 'b', 't': 'c', 'u': 'd', 'v': 'e', 'w': 'f', 'x': 'g', 'y': 'h', 'z': 'i'}
        cipher9 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher9 += ceaser_shift9[letter]
            else:
                cipher9 += ' '
        print("9            " + cipher9)
        ceaser_shift10 = {'a': 'k', 'b': 'l', 'c': 'm', 'd': 'n', 'e': 'o', 'f': 'p', 'g': 'q', 'h': 'r', 'i': 's', 'j': 't', 'k': 'u', 'l': 'v', 'm': 'w', 'n': 'x', 'o': 'y', 'p': 'z', 'q': 'a', 'r': 'b', 's': 'c', 't': 'd', 'u': 'e', 'v': 'f', 'w': 'g', 'x': 'h', 'y': 'i', 'z': 'j'}
        cipher10 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher10 += ceaser_shift10[letter]
            else:
                cipher10 += ' '
        print("10           " + cipher10)
        ceaser_shift11 = {'a': 'l', 'b': 'm', 'c': 'n', 'd': 'o', 'e': 'p', 'f': 'q', 'g': 'r', 'h': 's', 'i': 't', 'j': 'u', 'k': 'v', 'l': 'w', 'm': 'x', 'n': 'y', 'o': 'z', 'p': 'a', 'q': 'b', 'r': 'c', 's': 'd', 't': 'e', 'u': 'f', 'v': 'g', 'w': 'h', 'x': 'i', 'y': 'j', 'z': 'k'}
        cipher11 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher11 += ceaser_shift11[letter]
            else:
                cipher11 += ' '
        print("11           " + cipher11)
        ceaser_shift12 = {'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p', 'e': 'q', 'f': 'r', 'g': 's', 'h': 't', 'i': 'u', 'j': 'v', 'k': 'w', 'l': 'x', 'm': 'y', 'n': 'z', 'o': 'a', 'p': 'b', 'q': 'c', 'r': 'd', 's': 'e', 't': 'f', 'u': 'g', 'v': 'h', 'w': 'i', 'x': 'j', 'y': 'k', 'z': 'l'}
        cipher12 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher12 += ceaser_shift12[letter]
            else:
                cipher12 += ' '
        print("12           " + cipher12)
        ceaser_shift13 = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}
        cipher13 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher13 += ceaser_shift13[letter]
            else:
                cipher13 += ' '
        print("13           " + cipher13)
        ceaser_shift14 = {'a': 'o', 'b': 'p', 'c': 'q', 'd': 'r', 'e': 's', 'f': 't', 'g': 'u', 'h': 'v', 'i': 'w', 'j': 'x', 'k': 'y', 'l': 'z', 'm': 'a', 'n': 'b', 'o': 'c', 'p': 'd', 'q': 'e', 'r': 'f', 's': 'g', 't': 'h', 'u': 'i', 'v': 'j', 'w': 'k', 'x': 'l', 'y': 'm', 'z': 'n'}
        cipher14 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher14 += ceaser_shift14[letter]
            else:
                cipher14 += ' '
        print("14           " + cipher14)
        ceaser_shift15 = {'a': 'p', 'b': 'q', 'c': 'r', 'd': 's', 'e': 't', 'f': 'u', 'g': 'v', 'h': 'w', 'i': 'x', 'j': 'y', 'k': 'z', 'l': 'a', 'm': 'b', 'n': 'c', 'o': 'd', 'p': 'e', 'q': 'f', 'r': 'g', 's': 'h', 't': 'i', 'u': 'j', 'v': 'k', 'w': 'l', 'x': 'm', 'y': 'n', 'z': 'o'}
        cipher15 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher15 += ceaser_shift15[letter]
            else:
                cipher15 += ' '
        print("15           " + cipher15)
        ceaser_shift16 = {'a': 'q', 'b': 'r', 'c': 's', 'd': 't', 'e': 'u', 'f': 'v', 'g': 'w', 'h': 'x', 'i': 'y', 'j': 'z', 'k': 'a', 'l': 'b', 'm': 'c', 'n': 'd', 'o': 'e', 'p': 'f', 'q': 'g', 'r': 'h', 's': 'i', 't': 'j', 'u': 'k', 'v': 'l', 'w': 'm', 'x': 'n', 'y': 'o', 'z': 'p'}
        cipher16 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher16 += ceaser_shift16[letter]
            else:
                cipher16 += ' '
        print("16           " + cipher16)
        ceaser_shift17 = {'a': 'r', 'b': 's', 'c': 't', 'd': 'u', 'e': 'v', 'f': 'w', 'g': 'x', 'h': 'y', 'i': 'z', 'j': 'a', 'k': 'b', 'l': 'c', 'm': 'd', 'n': 'e', 'o': 'f', 'p': 'g', 'q': 'h', 'r': 'i', 's': 'j', 't': 'k', 'u': 'l', 'v': 'm', 'w': 'n', 'x': 'o', 'y': 'p', 'z': 'q'}
        cipher17 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher17 += ceaser_shift17[letter]
            else:
                cipher17 += ' '
        print("17           " + cipher17)
        ceaser_shift18 = {'a': 's', 'b': 't', 'c': 'u', 'd': 'v', 'e': 'w', 'f': 'x', 'g': 'y', 'h': 'z', 'i': 'a', 'j': 'b', 'k': 'c', 'l': 'd', 'm': 'e', 'n': 'f', 'o': 'g', 'p': 'h', 'q': 'i', 'r': 'j', 's': 'k', 't': 'l', 'u': 'm', 'v': 'n', 'w': 'o', 'x': 'p', 'y': 'q', 'z': 'r'}
        cipher18 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher18 += ceaser_shift18[letter]
            else:
                cipher18 += ' '
        print("18           " + cipher18)
        ceaser_shift19 = {'a': 't', 'b': 'u', 'c': 'v', 'd': 'w', 'e': 'x', 'f': 'y', 'g': 'z', 'h': 'a', 'i': 'b', 'j': 'c', 'k': 'd', 'l': 'e', 'm': 'f', 'n': 'g', 'o': 'h', 'p': 'i', 'q': 'j', 'r': 'k', 's': 'l', 't': 'm', 'u': 'n', 'v': 'o', 'w': 'p', 'x': 'q', 'y': 'r', 'z': 's'}
        cipher19 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher19 += ceaser_shift19[letter]
            else:
                cipher19 += ' '
        print("19           " + cipher19)
        ceaser_shift20 = {'a': 'u', 'b': 'v', 'c': 'w', 'd': 'x', 'e': 'y', 'f': 'z', 'g': 'a', 'h': 'b', 'i': 'c', 'j': 'd', 'k': 'e', 'l': 'f', 'm': 'g', 'n': 'h', 'o': 'i', 'p': 'j', 'q': 'k', 'r': 'l', 's': 'm', 't': 'n', 'u': 'o', 'v': 'p', 'w': 'q', 'x': 'r', 'y': 's', 'z': 't'}
        cipher20 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher20 += ceaser_shift20[letter]
            else:
                cipher20 += ' '
        print("20           " + cipher20)
        ceaser_shift21 = {'a': 'v', 'b': 'w', 'c': 'x', 'd': 'y', 'e': 'z', 'f': 'a', 'g': 'b', 'h': 'c', 'i': 'd', 'j': 'e', 'k': 'f', 'l': 'g', 'm': 'h', 'n': 'i', 'o': 'j', 'p': 'k', 'q': 'l', 'r': 'm', 's': 'n', 't': 'o', 'u': 'p', 'v': 'q', 'w': 'r', 'x': 's', 'y': 't', 'z': 'u'}
        cipher21 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher21 += ceaser_shift21[letter]
            else:
                cipher21 += ' '
        print("21           " + cipher21)
        ceaser_shift22 = {'a': 'w', 'b': 'x', 'c': 'y', 'd': 'z', 'e': 'a', 'f': 'b', 'g': 'c', 'h': 'd', 'i': 'e', 'j': 'f', 'k': 'g', 'l': 'h', 'm': 'i', 'n': 'j', 'o': 'k', 'p': 'l', 'q': 'm', 'r': 'n', 's': 'o', 't': 'p', 'u': 'q', 'v': 'r', 'w': 's', 'x': 't', 'y': 'u', 'z': 'v'}
        cipher22 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher22 += ceaser_shift22[letter]
            else:
                cipher22 += ' '
        print("22           " + cipher22)
        ceaser_shift23 = {'a': 'x', 'b': 'y', 'c': 'z', 'd': 'a', 'e': 'b', 'f': 'c', 'g': 'd', 'h': 'e', 'i': 'f', 'j': 'g', 'k': 'h', 'l': 'i', 'm': 'j', 'n': 'k', 'o': 'l', 'p': 'm', 'q': 'n', 'r': 'o', 's': 'p', 't': 'q', 'u': 'r', 'v': 's', 'w': 't', 'x': 'u', 'y': 'v', 'z': 'w'}
        cipher23 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher23 += ceaser_shift23[letter]
            else:
                cipher23 += ' '
        print("23           " + cipher23)
        ceaser_shift24 = {'a': 'y', 'b': 'z', 'c': 'a', 'd': 'b', 'e': 'c', 'f': 'd', 'g': 'e', 'h': 'f', 'i': 'g', 'j': 'h', 'k': 'i', 'l': 'j', 'm': 'k', 'n': 'l', 'o': 'm', 'p': 'n', 'q': 'o', 'r': 'p', 's': 'q', 't': 'r', 'u': 's', 'v': 't', 'w': 'u', 'x': 'v', 'y': 'w', 'z': 'x'}
        cipher24 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher24 += ceaser_shift24[letter]
            else:
                cipher24 += ' '
        print("24           " + cipher24)
        ceaser_shift25 = {'a': 'z', 'b': 'a', 'c': 'b', 'd': 'c', 'e': 'd', 'f': 'e', 'g': 'f', 'h': 'g', 'i': 'h', 'j': 'i', 'k': 'j', 'l': 'k', 'm': 'l', 'n': 'm', 'o': 'n', 'p': 'o', 'q': 'p', 'r': 'q', 's': 'r', 't': 's', 'u': 't', 'v': 'u', 'w': 'v', 'x': 'w', 'y': 'x', 'z': 'y'}
        cipher25 = ''
        for letter in text_to_decode:
            if(letter != ' '):
                cipher25 += ceaser_shift25[letter]
            else:
                cipher25 += ' '
        print("25           " + cipher25)

        return Code_breaker.text_input()

Code_breaker.text_input()