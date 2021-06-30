import numpy as np
import h5py
team_name = "PIPPO"

result = [0, 7, 6, 8]
result = np.array(result)

f = h5py.File("%s.h5" %team_name, "w")
f.create_dataset('Result', data = result,  compression='gzip')
f.close()
