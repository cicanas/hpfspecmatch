import os
import glob
# HPF wavelength bounds for different orders in Angstrom
BOUNDS = {'4': [8540.,8640.],
          '5': [8670.,8750.],
          '6': [8790.,8885.],
          '14': [9940.,10055.],
          '15': [10105.,10220.],
          '16': [10280.,10395.],
          '17': [10460.,10570.]}

# Directory name of package
DIRNAME = os.path.dirname(os.path.dirname(__file__))
print('DIRNAME: {}'.format(DIRNAME))

# Default library path
PATH_LIBRARIES = os.path.join(DIRNAME,"library")
PATH_LIBRARY = os.path.join(PATH_LIBRARIES,"20201008_specmatch_nir_library")
PATH_LIBRARY_DB = os.path.join(PATH_LIBRARY,"20201008_specmatch_nir_library.csv")
PATH_LIBRARY_FITS = os.path.join(PATH_LIBRARY,"FITS")
PATH_LIBRARY_CROSSVAL = os.path.join(PATH_LIBRARY,"crossval")
PATH_LIBRARY_ZIPNAME = os.path.join(PATH_LIBRARY,'20201008_specmatch_nir_library.zip')
#URL_LIBRARY = 'https://www.dropbox.com/s/69j00zrpov48qwx/20201008_specmatch_nir.zip?dl=1'
URL_LIBRARY = 'https://www.dropbox.com/s/epsacaktwu3by68/20201008_specmatch_nir_library.zip?dl=1'
LIBRARY_FITSFILES = sorted(glob.glob(PATH_LIBRARY_FITS+'/*/*.fits'))
