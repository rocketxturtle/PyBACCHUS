from astropy import *
import astropy.units as u
from astropy.io import fits
from astropy.table import Table,vstack,hstack
from astropy.io import ascii
import numpy as np
import pandas as pd
import random
import warnings

import math
import matplotlib.pyplot as plt
import glob

from BACCHUS import BACCHUS
from par import *
from plt import *
from abu import *
from eqw import *
from Results import *

class Star(object):
    def __init__(self,name):
        self.name = name
        self.path = None
        self.best_parameters = None
        self.par = None

        self.atomic_symbols = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al',
 'Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe',
 'Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y',
 'Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te',
 'I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb',
 'Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt',
 'Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa',
 'U']
        self.Abundance = dict() 
        for i in self.atomic_symbols:
            self.Abundance[i] = None
        

    def get_par(self, path):
        self.path = path
        self.par = Par(self.path + '{}.par'.format(self.name))

    def get_abundance(self, element):
        self.Abundance[element] = Results(self.path,self.name,element)

    def get_best_parameters(self):
        self.par = Par(self.path + '{}.par'.format(self.name))

    def set_initial_values(self, spectra_path, teff, logg, m_h, v_micro, conv):
        
        self.spectra_path = spectra_path
        self.teff = teff
        self.logg = logg
        self.m_h = m_h
        self.vmicro = v_micro
        self.conv = conv

    def get_spectrum(self, has_uncertainties=False):
        data = np.loadtxt(self.spectra_path)
        self.waves = data[:,0]
        self.flux = data[:,1]
        if has_uncertainties == True:
            self.flux = data[:,2]

    def view_obs_spectra(self,xlabel='Wavelength [Angstroms]',ylabel='Rectified Flux',savefig=False):
        """
        View the observed spectra to make sure it's 100% okay. Useful for smoothbrains like me who get their file indexing wrong.
        """
        plt.figure(figsize=(14,4))
        plt.plot(self.waves,self.flux)
        plt.xlabel(xlabel, fontsize=15)
        plt.ylabel(ylabel, fontsize=15)
        plt.title(self.name, fontsize=15)
        plt.tight_layout()
        if savefig==True:
            plt.savefig('{}_observed_spectrum.jpg'.format(self.name))

    ##### ABUNDANCE INFORMATION #####



    ##### STAR PARAMETERS #####

    def get_best_params(self):
        """
        For stars where bacchus.param is run (or after make_best_params is run) to get the best fit atmospheric parameters.
        """
        pass

    def make_best_params(self,teff,logg,m_H,v_micro,conv, e_teff=100,e_logg=0.1,e_m_H=0.1,e_v_micro=0.1,e_conv=0.1):
        """
        Make a pseudo best_parameters.tab file using input guesses
        """
        pass

    

    

    
        

    


