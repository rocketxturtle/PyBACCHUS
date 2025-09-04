import numpy as np
import glob
import pandas as pd
import random
import warnings
import math
import subprocess
import os

from helper_methods import *

class ElementsWLN(object):
    def __init__(self,path):
        self.path = path
        with open(self.path) as file:
            self.lines = file.readlines()
            self.original = file.readlines()
        file.close()
        
        self.atomic_numbers = np.arange(1,93,1)
        self.atomic_symbols = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al',
 'Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe',
 'Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y',
 'Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te',
 'I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb',
 'Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt',
 'Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa',
 'U']

        wln = dict()
        wln['Atomic_number'] = self.atomic_numbers
        wln['Atomic_symbol'] = self.atomic_symbols
        df = pd.DataFrame(wln)

        alllines = []
        nlines_used = []
        for i in df['Atomic_symbol']:
            lines = get_windows(self.path, i)
            try:
                nlines_used.append(len(lines))
                alllines.append(lines)
            except:
                nlines_used.append(0)
                alllines.append(None)
        
        df['N_Lines'] = nlines_used
        df['Lines'] = alllines

        self.wln = df

    def update_line_selection(self,newfile=False, newfilename=''):
        output = []
        for count, i in enumerate(self.wln['Atomic_symbol']):
            if (self.wln.loc[count,'Lines'] == None) == False:
                string = '{} {} '.format(self.wln.loc[count,'Atomic_number'], self.wln.loc[count,'Atomic_symbol'])
                for j in self.wln.loc[count,'Lines']:
                    string = string + '{} '.format(j)
                string = string + '\n'
                output.append(string)
                
        if newfile==True:
            with open(newfilename, "w") as file:
                file.writelines(output)
            file.close()
        else:
            with open(self.path, "w") as file:
                file.writelines(output)
            file.close()          
            

        