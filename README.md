# exploHelp
 Auxiliary scripts for penetration testing.

## Current scripts available:
xmldecoder_generator.py - XMLDecoder payload generator
```
usage: xmldecoder_generator.py [-h] -c C

XMLDecoder payload generator

optional arguments:
  -h, --help  show this help message and exit
  -c C        command line input
```
pickle_generator.py - Pickle payload generator
```
usage: pickle_generator.py [-h] -c C -b

Pickle Code Execution payload generator

optional arguments:
  -h, --help  show this help message and exit
  -c C        command line input
  -b          encode with Base64
```
cors_scanner.py - Cross-Origin Resource Sharing scanner
```
usage: cors_scanner.py [-h] -t T

Cross-Origin Resource Sharing scanner

optional arguments:
  -h, --help  show this help message and exit
  -t T        target range
```


Python 2.7 *required* for these scripts to work!

Coded by Vilius Povilaika. Copyright © 2017
