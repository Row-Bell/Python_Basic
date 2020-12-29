#Python Strings

s = 'hi'
print(s[1])          ## i
print(len(s))        ## 2
print(s + ' there')  ## hi there

pi = 3.14
## text = 'The value of pi is ' + pi ## No, does not work
text = 'The value of pi is '+ str(pi)
print(text)

#If you want to ignore backslashes use 'r' before print
raw = r'this\t\n and that'

# this\t\n and that 
print(raw)

multi = """It was the best of times. It was the worst of times."""

#It was the best of times
# It was the worst of times.
print(multi)

##########################################################

s = ' Robel Arega '

#s is a string - s.lower() or s.upper() returns the lowercase or uppercase version of the stsring
lowerCase = s.lower()
upperCase = s.upper()
print(lowerCase, upperCase)

#s.strip() - returns a string with whitespace removed fromt he start and end
raStrip = s.strip()
print(raStrip)

#s.isalpha()/s.isdigit()/s.isspace() - tests if the string chars are in the various character classes
print(s.isalpha(),s.isdigit(),s.isspace())

#s.startwith('other'), s.endswith('other') - tests if the string starts or ends with the given other string
print(s.startswith(' '), s.endswith('F'))

#s.find('other') - searches for the given other string(not a regular expression) within s, and returns the first index where it begins or -1 if not found
print(s.find('Beer'))

#s.replace('old','new') - returns a string where all occurences of 'old' have been replaced by 'new'
print(s.replace(' Robel Arega ', 'Bro, Not Cool'))

#s.split('delim') - returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just a text
#'aaa,bbb,ccc'.split(',') -> ['aaa','bbb','ccc']. As a convenient special case s.split()(with no arguments) splits on all whitespace chars
print(s.split('e'))

#s.join(list) - opposite of split(), joins the elements in the given list together using the string as the delimiter. 
# e.g. '--'(['aaa','bbb','ccc']) -> aaa--bbb---ccc
print('-'.join(s.split('e')))

###########################################################################

#String Slices
#The 'slice' syntax a handdy way to refer to sub-parts of sequences - typically strings and lists.
#The slice s[start:end] is the elements beginning at start and extending up to but not including end. Suppose we have s="Hello"
s2 = 'Hello'

#Positive numbers for H[0] - e[1] - l[2] - l[3] - o[4]
print(s2[1:4])
print(s2[1:])
print(s2[:])
print(s2[1:100])

#Negative numbers for H[-5] - e[-4] - l[-3] - l[-2] - o[-1]
print(s2[-1])
print(s2[-4])
print(s2[:-3])
print(s2[-3:])

#Side Note: s[:n] + s[n:] == s

#################################################################################3

#String %
#Python has a printf() - like facility to put together a string
#The % operator takes a printf-type format string on the left 
#(%d int, %s string, %f/%g floating point), and the matching values in a tuple on the right

text = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (3, 'huff', 'puff', 'house')
