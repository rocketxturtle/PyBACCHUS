import numpy as np
import pandas as pd

from PyBACCHUS.helper_methods import *

class StellarParameters(object):
    def __init__(self,path):
        self.path = path
        self.read()

        name,spectra_location,teff,logg,met,vmicro,conv= [],[],[],[],[],[],[]

        for i in self.lines[1:]:
            array = i.split('\t')
            array = list(filter(('').__ne__, array))

            name.append(array[0])
            spectra_location.append(array[1])
            teff.append(array[2])
            logg.append(array[3])
            met.append(array[4])
            vmicro.append(array[5])
            conv.append(array[6].replace('\n',''))
        data = [name,spectra_location,teff,logg,met,vmicro,conv]
        stellar_params = {'star_name':name,'spectrum_location': spectra_location, 'teff': teff, 'logg': logg, 'm_h': met, 'v_micro': vmicro, 'convolution': conv}
        df = pd.DataFrame(stellar_params)

        self.entries = df

    def add_star(self, Star):
        truth = np.isin(True,np.isin(self.entries['star_name'],Star.name))
        if truth:
            print('entry already added!')
        else:
            self.entries.loc[len(self.entries)] = [Star.name,Star.spectra_path,Star.teff,Star.logg,Star.m_h,Star.vmicro,Star.conv]

        # with open(self.path, 'w') as file:
        #     file.write('# starname                  obsfile               Teff   logg    [Fe/H] microt   convol  rv\n')
        # file.close()

        # with open(self.path , 'a') as file:
        #     for i in range(len(self.entries['star_name'])):
        #         output = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(self.entries.loc[i,'star_name'],self.entries.loc[i,'spectrum_location'],self.entries.loc[i,'teff'],
        #                                               self.entries.loc[i,'logg'],self.entries.loc[i,'m_h'],self.entries.loc[i,'v_micro'],self.entries.loc[i,'convolution'],0)
        #         file.write(output)
        # file.close()
        
    def remove_star(self, Star):
        truth = np.where(np.isin(self.entries['star_name'],Star.name)==False)[0]
        self.entries = self.entries.loc[truth]

        # with open(self.path, 'w') as file:
        #     file.write('# starname                  obsfile               Teff   logg    [Fe/H] microt   convol  rv\n')
        # file.close()

        # with open(self.path , 'a') as file:
        #     for i in range(len(self.entries['star_name'])):
        #         output = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(self.entries.loc[i,'star_name'],self.entries.loc[i,'spectrum_location'],self.entries.loc[i,'teff'],
        #                                               self.entries.loc[i,'logg'],self.entries.loc[i,'m_h'],self.entries.loc[i,'v_micro'],self.entries.loc[i,'convolution'],0)
        #         file.write(output)
        # file.close()


    def show(self):
        for n, i in enumerate(self.lines):
            print('{}, {}'.format(n, i))
            
    def read(self):
        with open(self.path) as file:
            self.lines = file.readlines()
        file.close()
        
    def write(self,newfile=False, newfilename=''):
        if newfile==True:
            with open(newfilename, 'w') as file:
                file.write('# starname                  obsfile               Teff   logg    [Fe/H] microt   convol  rv\n')
            file.close()

            with open(newfilename , 'a') as file:
                for i in range(len(self.entries['star_name'])):
                    output = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(self.entries.loc[i,'star_name'],self.entries.loc[i,'spectrum_location'],self.entries.loc[i,'teff'],
                                                      self.entries.loc[i,'logg'],self.entries.loc[i,'m_h'],self.entries.loc[i,'v_micro'],self.entries.loc[i,'convolution'],0)
                    file.write(output)
            file.close()
        else:
            with open(self.path, 'w') as file:
                file.write('# starname                  obsfile               Teff   logg    [Fe/H] microt   convol  rv\n')
            file.close()

            with open(self.path , 'a') as file:
                for i in range(len(self.entries['star_name'])):
                    output = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(self.entries.loc[i,'star_name'],self.entries.loc[i,'spectrum_location'],self.entries.loc[i,'teff'],
                                                      self.entries.loc[i,'logg'],self.entries.loc[i,'m_h'],self.entries.loc[i,'v_micro'],self.entries.loc[i,'convolution'],0)
                    file.write(output)
            file.close()

    def edit(self, line_number, text):
        new_lines = []
        for count,i in enumerate(self.lines):
            if count != line_number:
                self.lines[count] = i
            else:
                self.lines[count] = text

    def add_line(self, line2add, line_num = -1):
        if line_num == -1:
            self.lines = np.insert(self.lines,len(self.lines), line2add)
        else:
            self.lines = np.insert(self.lines,line_num, line2add)
                    
    def add_lines(self, lines2add, linenumbers = []):
        if linenumbers != []:
            for count, i in enumerate(lines2add):
                self.add_line(i, linenumbers[count])
        else:
            for count, i in enumerate(lines2add):
                self.add_line(i)

    def remove_lines(self, lines2remove):
        truth = np.isin(self.lines,lines2remove)
        self.lines = np.array(self.lines)[truth==False]