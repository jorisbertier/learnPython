import numpy as np
import pandas as pd

data = pd.read_csv('notes.csv')
moyenne_matiere = data.groupby('matiere').agg({'note' : ['mean']})
moyenne_par_eleve = data.groupby('nom').agg({'note' : ['mean']})
print(moyenne_par_eleve)