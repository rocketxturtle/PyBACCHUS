from astropy import *
import astropy.units as u
from astropy.io import fits
import numpy as np
# import glob as glob
import pandas as pd
from astropy.table import Table,vstack,hstack
from astropy.io import ascii
import random
import warnings

%matplotlib inline
import math
import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table
import glob

from BACCHUS.py import BACCHUS

class Star(BACCHUS):
    def __init__(self, teff, logg, m_h, vmicro,conv):
        self.teff = teff
        self.logg = logg
        self.m_h = m_h
        self.vmicro = vmicro
        self.conv = conv

    ##### PREPROCESSING #####

    def get_spectra(self, wavelengths, fluxes, errs, show=False):
        pass

    def add2stellarparams(self,spectra_path):
        pass

    ##### ABUNDANCE INFORMATION #####

    def get_abu(self,element):
        pass

    def get_plt(self, element):
        pass

    def get_tab(self, element):
        pass

    def get_list(self, element):
        pass

    def display_fits(self, element):
        pass

    ##### STAR PARAMETERS #####

    def get_best_params(self):
        pass

    def make_best_params(self,teff,logg,m_H,v_micro,conv, e_teff=100,e_logg=0.1,e_m_H=0.1,e_v_micro=0.1,e_conv=0.1):
        pass

    def edit_star_par(self):
        pass

    

    
        

    


