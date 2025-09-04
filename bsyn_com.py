import numpy as np
import glob
import pandas as pd
import random
import warnings
import math
import subprocess
import os

from helper_methods import *

class Bsyn(object):
    def __init__(self,path):
        self.path = path
        with open(self.path) as file:
            self.lines = file.readlines()
            self.original = file.readlines()
        file.close()

        self.nfiles_start_idx = get_linenumber(self.lines, "'NFILES", idx=0)
        self.nfiles_end_idx = get_linenumber(self.lines, "'SPHERICAL:'", idx=0)

        self.files = np.array(self.lines[self.nfiles_start_idx+1:self.nfiles_end_idx])
        
        self.nfiles = int(len(self.files))
        self.lines[self.nfiles_start_idx] = "'NFILES   :' '{}'\n".format(self.nfiles)

    def add_linelists(self, files):
        if len(files) > 0:
            self.nfiles = self.nfiles + len(files)
            self.lines[self.nfiles_start_idx] = "'NFILES   :' '{}'\n".format(self.nfiles)
            for count, i in enumerate(self.lines):
                if count == self.nfiles_start_idx + 1:
                    self.lines = np.insert(self.lines, self.nfiles_start_idx + 2, files)
                    
        with open(self.path, "w") as file:
            file.writelines(self.lines)
        file.close()

    def remove_linelists(self, files):
        if len(files) > 0:
            truth = np.isin(self.lines,files)
            self.lines = np.array(self.lines)[truth==False]
            truth = np.isin(self.files,files)
            self.files = np.array(self.files)[truth==False]
            self.nfiles = self.nfiles - len(files)
            
            self.lines[self.nfiles_start_idx] = "'NFILES   :' '{}'\n".format(self.nfiles)
            
        with open(self.path, "w") as file:
            file.writelines(self.lines)
        file.close()
        