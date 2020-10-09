import numpy as np

def Nash(K, N, Xbeg, Inp):
	OO = np.zeros(N)
	Xend = np.zeros(N)
	for Res in range(0,N):
		OO[Res] = K*Xbeg[Res]
		Xend[Res] = Xbeg[Res]-OO[Res]

		if Res == 0:
			Xend[Res] = Xend[Res] + Inp
		else:
			Xend[Res] = Xend[Res] + OO[Res-1]

	out = OO[N-1]
	return out, Xend
