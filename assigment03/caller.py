

from assigment03 import DoThis

# Reading key,pair values from config file
dt = DoThis()
dt.load_config()
print(dt)
dt['marc'] = 'alon'
dt.set_config()

