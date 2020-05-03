"""
Two options for quarantine boredem.
You can play tic tac toe or forgot english and only speak in Pig Latin.

I remeber when I was a kid I could never figure out how to speak pig latin.
So I thought why not create a code to translate it for me.
However I didnt know if this was enough for my final so I just thought I would add it
in for fun. 
Something fun to learn during quarantine.
"""


ay = 'ay'
way = 'way'
consonant = ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','Y','V','X','Z')
vowel = ('A','E','I','O','U')
pig_latin_str =''
Intro_Message = input('Enter a sentence to translate to Pig Latin: ')
words = Intro_Message.split()

for players_word in words:
    print(players_word)
# getting first letter and making sure its a string and setting it to uppercase
    first_letter = players_word[0]
    first_letter = str(first_letter)
    first_letter=first_letter.upper()

    if first_letter in consonant:
        length_of_word = len(players_word)
        move_first_letter = players_word[1:length_of_word]
        pig_latin=move_first_letter+first_letter+ay
        pig_latin_str=pig_latin_str+' '+pig_latin
    elif first_letter in vowel:
        pig_latin=players_word+way
        pig_latin_str=pig_latin_str+' '+pig_latin
    else:
        print('?')

print(pig_latin_str)