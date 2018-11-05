
def doubleit(var):
    return var * 2

# This bridge guarantees that the code inside is only 
# executed when the script is called/run directly. 
# If the script is imported by some other script, then 
# the code within the bridge won't not executed. 
if __name__ == '__main__':
    v = 1
    print("{0} doubled = {1}".format(v, doubleit(v)))
