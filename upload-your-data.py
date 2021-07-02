import numpy as np
import h5py
team_name = "PIPPO"

result = [0, 7, 6, 8] #event number
result = np.array(result)

#if you have not run an HLS implementation of the algorithm, set everything except FLOPs to zero
performance = {'FLOPs':1000000000, 'Device': 'xcu250-figd2104-2L-e' ,'Latency': 500, 'DSP': 50, 'LUT': 1, 'FF': 3, 'BRAM': 0} #latency in microseconds, resources in %

f = h5py.File("%s.h5" %team_name, "w")
f.create_dataset('Result', data = result,  compression='gzip')
for k in performance.keys(): f.attrs[k]=performance[k]
f.close()

