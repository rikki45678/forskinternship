#regular exp

import re

dir(re)

"""
sub
findall
search
match
compile
"""

s = 'aaa@gmail.com bbb@yahoo.com ccc@outlook.com'

#'ABC@gmail.com, ABC@yahoo.com ABC@outlook.com'

sub_s = re.sub('[a-z]*@','ABC@',s)


str1 = '123abc123xyz456_0'

re.findall('\d\d\d',str1)

#if we want to find only first 123 

re.findall('^\d\d\d',str1)

str2 = 'bluepink123abc123xyz456_0'
re.findall('^\d\d\d',str2)



str1 = 'foo123bar'

re.search('\d\d\d',str1)


str2 = 'Forsk forsk Coding School'

re.match('forsk',str2) #^
re.search('forsk',str2)

re.match('Forsk',str2)
re.search('Forsk',str2)

#search -> find something which is anywhere in the string and return a match object
#match ->  find something at the begining of the string and return a match object

#version 01
str1 = 'kisan andolan forsklabs@gmail.com 1234 yogendra@forsk.in sylvester Drishyam2 yogendrasingh@qualcomm.com mohanlal ysingh@mango.com covid yogendra@zdrv.com'
re.findall('\w+@\w+\.\w+',str1)

#version 02

str1 = 'kisan andolan forsklabs@gmail.com 1234 yogendra@forsk.in sylvester Drishyam2 yogendrasingh@qualcomm.com mohanlal ysingh@mango.com covid yogendra@zdrv.com'
epattern = re.compile(r'\w+@\w+\.\w+')
epattern.findall(str1)
