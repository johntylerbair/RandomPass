import argparse
import random
import string

parser = argparse.ArgumentParser(description="Get number of characters")
parser.add_argument('size', type=int)
args = parser.parse_args()
password = ''.join("%s" % random.choice(string.ascii_letters + string.digits) for i in range(args.size))
print(password)
