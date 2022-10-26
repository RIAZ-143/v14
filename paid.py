import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from v14 import abcdefg

    abcdefg()

elif bit == '32bit':

    from v14s import abcdefg

    abcdefg()
