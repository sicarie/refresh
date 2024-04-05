#!/usr/bin/Python

'''
NOTES:

  Punctuation must not be touched. if a word is 6 characters long, and a "." is behind it,
  it counts as 6 characters so it must not be flipped, but if a word is 7 characters long,
  it must be flipped but the "." must stay at the end of the word.
  -----------------------------------------------------------------------------------------
  Only the first transformation applies to a given word, for example 'companions,'
  will be 'snoinapmoc,' and not 'SNOINAPMOC,'.
  -----------------------------------------------------------------------------------------
  As for special characters like apostrophes or dashes, they count as normal characters,
  so e.g 'sand-colored' must be transformed to 'deroloc-dnas'.
'''

'''
convert every word backwards that is:
longer than 6 characters
OR
has 2 or more 'T' or 't' in it
'''
def checkWordLength(line):
    #split line by spaces
    words = line.split(' ')
    revd = ''
    tmp = ''
    print("reversing: '" + line + "'")
    for i in words:
        if (((len(i) > 6) or ('TT' in i) or ('tt' in i)) and (',' not in i)):
            #reverse
            tmp = i[::-1]
            revd += tmp + ' '
        else:
            revd += i + ' '
    return revd.strip()
#end checkWordLength()

'''
convert every word uppercase that is:
exactly 2 characters long
OR
before a comma
'''
def uppercase(line):
    uppered = ''
    return uppered
#end uppercase()

'''
convert every word to a "0" that is:
exactly one character long
'''
def zero(line):
    zed = ''
    return zed
#end zero

def main():
    line = 'Short longers s baTTy boop longetty.'
    print(checkWordLength(line))
    uppercase(line)
    zero(line)

main()
