import numpy as np
import glob
import pandas as pd
import random
import warnings
import math
import subprocess
import os

from helper_methods import *
from abu import *
from eqw import *
from plt import *

class Results(object):
    def __init__(self,path,name,elem):
        self.path = path
        self.name = name
        self.element = elem

        if len(glob.glob(self.path + '/{}*.abu'.format(self.element))) > 0:
            
            self.ABU = Abu(self.path + '/{}-{}.abu'.format(self.element,self.name))
            abus = []
            for i in glob.glob(self.path + '/{}*.abu'.format(self.element)):
                abus.append(Abu(i))
            self.ABU_hist = abus

        if len(glob.glob(self.path + '/{}*.plt'.format(self.element))) > 0:
            
            self.PLT = Plt(self.path + '/{}-{}.plt'.format(self.element,self.name))
            plts = []
            for i in glob.glob(self.path + '/{}*.plt'.format(self.element)):
                plts.append(Plt(i))
            self.PLT_hist = plts

        if len(glob.glob(self.path + '/{}*.eqw'.format(self.element))) > 0:
            
            self.EQW = EQW(self.path + '/{}-{}.eqw'.format(self.element,self.name))
            eqws = []
            for i in glob.glob(self.path + '/{}*.eqw'.format(self.name,self.element)):
                eqws.append(EQW(i))
            self.EQW_hist = eqws

        