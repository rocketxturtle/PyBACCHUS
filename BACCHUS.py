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
import subprocess

%matplotlib inline
import math
import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table
import glob

from Star.py import Star

class BACCHUS(object):
    def __init__(self,path):
        self.path = path

    ##### OPERATIONS ON STAR #####

    def load_parameters(self, Star):
        command_path = self.path + '/load_parameters.com'
        subprocess.call([command_path,Star.name])

    def param(self, Star):
        command_path = self.path + '/bacchus.param'
        subprocess.call([command_path,Star.name])

    def eqw(self, Star, lines=[],ranges=[]):
        command_path = self.path + '/bacchus.eqw'
        subprocess.call([command_path,Star.name])

    def abund(self, Star,lines=[],ranges=[]):
        command_path = self.path + '/bacchus.abund'
        subprocess.call([command_path,Star.name])

    ##### LINELISTS & SELECTION #####

    def show_linelists(self, extension=''):
        pass

    def edit_linelist(self):
        pass

    def select_linelist(self, line_path):
        pass

    def show_lineselection(self):
        pass

    def edit_lineselection(self, elem=None,lines=[]):
        pass

    ##### STRUCTURAL #####

    def show_init_com(self):
        pass

    def edit_init_com(self):
        pass

    def show_bsyn_com(self):
        pass 

    def edit_bsyn_com(self):
        pass
        

