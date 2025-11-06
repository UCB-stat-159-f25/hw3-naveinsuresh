from ligotools.readligo import dq2segs, dq_channel_to_seglist
import numpy as np

def test_dq2segs():
	
	try:
		dq2segs({}, 101)
		
	except KeyError:
		pass
		
	else:
		assert False, "Function did not catch missing default channel!"

def test_dq_channel_to_seglist(fs=4096):

    func_output = dq_channel_to_seglist(np.array([1, 0, 0, 1, 0, 1, 1, 1, 1]), fs=fs)
    correct_slice = [slice(fs*0, fs*1), slice(fs*3, fs*4), slice(fs*5, fs*9)]

    assert func_output == correct_slice, "The output slices do not match!"