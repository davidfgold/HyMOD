import numpy as np
import pandas as pd
from Hymod_functions.Hymod import Hymod01
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def main(Nq, Kq, Ks, Alp, Huz, B, Data_name):
    # read in observed rainfall-runoff data for one year
    Data = pd.read_csv(Data_name)
    Data = Data.iloc[0:365]

    # assign parameters

    # Nq: number of quickflow routing tanks
    # Kq: quickflow routing tanks parameters 				- Range [0.1, 1]
    # Ks: slowflow routing tanks rate parameter 			- Range [0, 0.1]
    # Alp: Quick-slow split parameters 						- Range [0, 1]
    # Huz: Max height of soil moisture accounting tanks 	- Range [0, 500]
    # B: Distribution function shape parameter 				- Range [0, 2]

    Pars = {'Nq': Nq,
              'Kq': Kq,
              'Ks': Ks,
              'Alp': Alp,	
              'Huz': Huz,	
              'B': B}

    # Initialize states
    InState = {'Xq': np.zeros(Pars['Nq']),
               'Xs': 0,
               'XHuz': 0}

    Model = Hymod01(Data, Pars, InState)
    
    return Model

