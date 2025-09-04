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

import math
import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table
import glob
# import imports.py
from BACCHUS import BACCHUS

class Star(BACCHUS):
    def __init__(self, name, wavelengths, flux, cntm=None,flux_err=None):
        """
        Instantiate a Star object. This requires at a minimum the name of the star and the filepath to its spectrum
        """
        self.name = name
        self.waves = wavelengths
        self.flux = flux
        self.cntm = cntm
        self.flux_err = flux_err

    def get_spectrum_path(self , spectra_path):
        self.spectra_path = spectra_path

    ##### PREPROCESSING #####

    def set_initial_guesses(self, teff, logg, m_h, vmicro,conv):
        """These are the initial guesses required for stellar_parameters.tab. Here we also set the guesses for the line selection and any potential guesses for the x_H abundances. The abundance guesses will be transformed to A(x) values and passed to star.par before running that element.
        """
        self.teff = teff
        self.logg = logg
        self.m_h = m_h
        self.vmicro = vmicro
        self.conv = conv

        self.line_selection = dict()
        self.abundances = dict()



    def view_obs_spectra(self):
        """
        View the observed spectra to make sure it's 100% okay. Useful for smoothbrains like me who get their file indexing wrong.
        """
        plt.figure(figsize=(14,4))
        plt.plot(self.waves,self.flux)


    def view_obs_line_windows(self, elem):
        """
        View the observed spectra to make sure it's 100% okay. Useful for smoothbrains like me who get their file indexing wrong.
        """
        plt.figure(figsize=(14,4))
        plt.plot(self.waves,self.flux)
            

    def add2stellarparams(self,spectra_path, name):
        """
        Add the star to stellar_parameters.tab here. Will probably need to check if an entry with that name already exists and if so overwrite it.
        """
        self.spectra_path = spectra_path
        self.name = name
        pass

    ##### ABUNDANCE INFORMATION #####

    def get_star_par(self):
        """
        returns star.par file and allows for editing.
        """
        pass

    def get_abu(self,element):
        """
        I think this should just be getting the x_.abu file, and transforming it into a pandas dataframe. will need to figure out how to transform df back to file tho for updating purposes.
        """
        pass

    def get_plt(self, element):
        """
        I think this should just be getting the x_.plt file, and transforming it into a pandas dataframe. will need to figure out how to transform df back to file tho for updating purposes.
        """
        pass

    def get_tab(self, element):
        """
        I think this should just be getting the x_.tab file, and transforming it into a pandas dataframe. will need to figure out how to transform df back to file tho for updating purposes.
        """
        pass

    def get_list(self, element):
        """
        I think this should just be getting the x_.list file, and transforming it into a pandas dataframe. will need to figure out how to transform df back to file tho for updating purposes.
        """
        pass

    def display_fits(self, element):
        """
        For a given element, display the SuperMongo .pdf abundance fits. Have the option to return them as a plt object for export purposes?
        """
        pass

    def set_good_lines(self,elems = [],lines=[]):
        """
        For updating the line selection for a single star. WILL NOT UPDATE ELEMENTS.WLN. Thinking if this is not empty, BACCHUS.abund() should be fed only these lines.
        Could have an automated mode, but i think shutoff on default for doublechecking.
        """
        for i, count in enumerate(elems):
            self.line_selection[i] = lines[count]

    def set_abundance(self, element, x_H, e_x_H):
        """
        Pass an A(x) abundance to star.par to inform the model.
        """
        pass

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

    

    

    
        

    


