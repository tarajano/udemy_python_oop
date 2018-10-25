

# Generating custom exceptions  

from assigment03 import ConfigDict
import sys

# Run this script like:
# caller.py OR
# caller.py <key> <value>

# Reading key,pair values from config file
dt = ConfigDict('dothis.config')


# if 1 == len(sys.argv):
#     dt.print_dict()
# elif 3 == len(sys.argv):
#     dt[str(sys.argv[1])] = str(sys.argv[2])
# else:
#     print("""
#             Run this script like:
#             python caller.py
#             OR
#             python caller.py <key> <value>
#         """)
#     exit()

print(dt['aseb'])
