from ligotools.utils import write_wavfile, reqshift
import numpy as np
import os

def test_write_wavfile():

	test_data = np.array([2, 5, 8, 4, 7, 9])
	write_wavfile("output.wav", 4096, test_data)

	assert os.path.exists("output.wav"), "Output .wav file was not created!"

	os.remove("output.wav")

def test_reqshift():

	test_data = np.array([4, 1, 4, 8, 9, 6, 7, 9])
	output = reqshift(test_data)

	assert len(output) == len(test_data), "The lengths of the two datasets do not match!"