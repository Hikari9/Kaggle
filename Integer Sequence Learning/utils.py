# gets python training and test data

import csv
def get_data(filename):
	return list(csv.reader(open(filename)))[1:]

def get_training_data():
	return get_data('input/train.csv')

def get_test_data():
	return get_data('input/test.csv')

def gcd(a, b):
	return (a if a >= 0 else -a) if b == 0 else gcd(b, a % b)

# can compress data values
class Compressor(object):

	def __init__(self, array):
		self._decomp = sorted(list(set(values)))
		self._comp = {value: index for index, value in enumerate(self._decomp)}

	def compress(self, item, default=None):
		return self._comp[item] if item in self._comp else default

	def decompress(self, item, default=None):
		return self._decomp[item] if item >= 0 and item < len(self._decomp) else default



