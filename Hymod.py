import pandas as pd
import numpy as np
from Hymod_functions.Nash import Nash
from Hymod_functions.Pdm01 import Pdm01


# need to grow XHuz and others

def Hymod01(Data, Pars, InState):
	
	# initialize arrays
	XHuz = np.zeros(len(Data))
	XHuz[0] = InState['XHuz']

	Xs = np.zeros(len(Data))
	Xs[0] = InState['Xs']

	Xq = np.zeros([len(Data), Pars['Nq']])
	Xq[0,:] = InState['Xq']

	OV = np.zeros(len(Data))
	ET = np.zeros(len(Data))
	XCuz = np.zeros(len(Data))
	Qq = np.zeros(len(Data))
	Qs = np.zeros(len(Data))
	Q = np.zeros(len(Data))
    
	for i in range(0, len(Data)):
		
		# run soil moisture accounting including evapotranspiration
		OV[i], ET[i], XHuz[i], XCuz[i] = Pdm01(Pars['Huz'], Pars['B'], XHuz[i], Data['Precip'].iloc[i], Data['Pot_ET'].iloc[i])

		# run Nash Cascade routing of quickflow component
		Qq[i], Xq[i, :] = Nash(Pars['Kq'], Pars['Nq'], Xq[i, :], Pars['Alp']*OV[i])


		# run slow flow component, one infinite linear tank
		Qs[i], Xs[i] = Nash(Pars['Ks'], 1, [Xs[i]], (1-Pars['Alp'])*OV[i])

		if i < len(Data)-1:
			XHuz[i+1] = XHuz[i]
			Xq[i+1] = Xq[i]
			Xs[i+1] = Xs[i]

		Q[i] = Qs[i] + Qq[i]
	# write to a dict
	Model = {'XHuz': XHuz,
			 'XCuz': XCuz,
			 'Xq': Xq,
             'Xs': Xs,
			 'ET': ET,
			 'OV': OV,
			 'Qq': Qq,
			 'Qs': Qs,
			 'Q' : Q}

	return Model


