

from assigment02 import *

# Log file
lf = LogFile('file.log')
lf.write('Oye! Manu')
lf.write('Llegaron bebe y bebita')

# CSV file
csv = DelimFile('file.csv', ',')
csv.write('Oye! Manu')
csv.write('Llegaron bebe y bebita')

