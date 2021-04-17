"""
Task 4
Implement and test a program to input a sentence, apply a code to each character
(except spaces) and output the coded message to the screen.
For example, A becomes Y, B becomes Z, etc and thus Hello World would be coded
as Fcjjm Umpjb.
"""
# This module provides access to some variables used or maintained by the interpreter 
# and to functions that interact strongly with the interpreter. It is always available.
import sys # System-specific parameters and functions. 
import getopt # C-style parser for command line options

text_necodat = "Python is an interpreted, high-level and general-purpose programming language. "


text_original = open("original_text.txt", "w"); text_original.write(text_necodat); text_original.close();

text_coded = open("coded_text.txt", "w")
text_coded.close()





def program_codare(data, key, mode):
    latinAlpha = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ'
    dataNew = ''
    for letter in data:
        # Shift character
        index = latinAlpha.find(letter)
        if index == -1:
            # Character not found
            dataNew = dataNew + letter
        else:
            # Shift it based on key and mode
            new_index = index + key if mode == 1 else index - key
            new_index %= len(latinAlpha)
            dataNew = dataNew + latinAlpha[new_index:new_index+1]
    # Return the ciphered text
    return dataNew

if __name__ == '__main__':
    syntax = 'k:m:i:o:'
    # Default arguments
    key = 1
    mode = 1
    oFile = 'coded_text.txt'
    iFile = 'original_text.txt' 
    try:
        opts, args = getopt.getopt(sys.argv[1:], syntax)
        for o, a in opts:
            if o == '-k':
                key = int(a)
            elif o == '-m':
                mode = int(a)
            elif o == '-i':
                in_file = a
            elif o == '-o':
                out_file = a

        # Read file
        with open(iFile, 'rt') as f:
            data = f.read()
        # Translate it
        dataNew = program_codare(data, key, mode)
        with open(oFile, 'wt') as f:
            f.write(dataNew)

    except getopt.GetoptError as err:
        print('Error parsing args:', err)
        sys.exit(1)
    except Exception as e:
        print('Error', e)
        sys.exit(2)


with open('original_text.txt', 'rt') as ff:
    data1 = ff.read()
with open('coded_text.txt', 'rt') as ff:
    data2 = ff.read()

linie = "---------------------------------------------------------------------------"


print(linie)
print("ORIGINAL TEXT:" + data1)
print(linie)
print("CODED TEXT: " + data2)
print(linie)