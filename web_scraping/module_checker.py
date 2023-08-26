import sys
'''
import subprocess

if "pandas" in sys.modules:
    print("module already imported")
else:
    print("module not imported")

    import sys
'''

import pprint

pprint.pprint(sys.path)

import pandas

# decimalモジュールのパスを確認
print(pandas.__file__)
