import PyBACCHUS
from PyBACCHUS.bacchus import BACCHUS
from PyBACCHUS.star import Star

def main():
    starname = 'sdss_id_55749319'
    bpath = '/uufs/chpc.utah.edu/common/home/astro/zasowski/sinha/bacchus_files/b_0/'

    bacchus = BACCHUS(bpath)
    bacchus.init.show()
    
    