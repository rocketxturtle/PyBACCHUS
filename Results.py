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
from Star.py import Star

class BacchusResults(BACCHUS):
    def __init__(self, teff):
        pass

    def make_abundance_table(self,elems=[]):
        pass