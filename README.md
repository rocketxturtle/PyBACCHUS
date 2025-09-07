# PyBACCHUS
[![DOI](https://zenodo.org/badge/1034636798.svg)](https://doi.org/10.5281/zenodo.17070805)
[![A rectangular badge, half black half purple containing the text made at Code Astro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A Python Wrapper for running the Brussels Automatic Code for Characterizing High accUracy Spectra (BACCHUS). 

[BACCHUS (https://ui.adsabs.harvard.edu/abs/2016ascl.soft05004M/abstract)]

## 📖 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Parameters](#-parameters)
- [Examples](#-examples)
- [Contributing](#-contributing)
- [Citation](#-citation)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

## ✨ Features

The purpose of this code is to allow interfacing with the native BACCHUS enivroment using Python. This is NOT a version of BACCHUS written in Python, it requires an existing BACCHUS installation to function. 

There are three primary modules for this package: BACCHUS, Star, and Result.

### BACCHUS
The BACCHUS class is instantiated by giving it the location of an existing BACCHUS installation. Once a BACCHUS object is created, it will be populated with the existing state of all the primary bacchus modules:
- bsyn.com 
- babsma.com
- stellar_parameters.tab
- init.com
- elements.wln

as well as a linelists object that contains the paths to all available linelists. Each of these modules is accessible in a BACCHUS object as an attribute (e.g. init.com can be accessed by bacchus.init). This allows for editing each module in python, both through direct line-by-line editing, and a suite of preloaded methods (e.g. set_ncpu, set_linelist). MORE DOCUMENTATION COMING.

Once the configuration of BACCHUS is set up to your liking, you can write it out to the native BACCHUS. 

### Star

A Star object is the container for the stars being run in BACCHUS. At a minimum it requires a name to be instantiated, but to load into stellar_parameters.tab it will require the six necessary parameters (spectra path, teff, logg, etc...). This object will also have access to all the parameter and model information from a BACCHUS analysis, as well as the elemental abundance results (stored in a Results object).

### Results

A Results object holds all the data for a single element within a Star. It automatically scrapes the star's directory after a .abund, .eqw, or .param analysis load in the .abu, .plt, and .eqw results as Astropy Tables. 

### Running a Star

After you've configured your BACCHUS setup to your liking and written the setup to native BACCHUS, you can follow the same procedure normally used in native BACCHUS

for a BACCHUS object bacchus, and a Star object
1) bacchus.load_parameters(Star)
2) bacchus.abund(Star)
3) bacchus.eqw(Star)
4) bacchus.param(Star)


## 🚀 Installation

### From PyPI (Stable Release)
```
pip install PyBACCHUS
```

### From GitHub (Development Version)
```
# Latest development version
pip install git+https://github.com/rocketxturtle/PyBACCHUS

# Or clone and install locally
git clone https://github.com/rocketxturtle/PyBACCHUS.git
cd PyBACCHUS
pip install -e .
```

### Dependencies
The package requires the following Python libraries:
- `numpy` - Numerical computations
- `pandas` - Data manipulation
- `astropy` - Astronomical utilities
- `matplotlib` - Plotting functionality

These will be automatically installed with the package.

## 🎯 Quick Start 

## 📁 Project Structure

```
PyBACCHUS/
├── __init__.py             # Package initialization and version info
├── bacchus.py              # The core BACCHUS object that mimics the file structure of BACCHUS
├── star.py                 # Contains the Star class, which is used to run objects in BACCHUS
├── results.py              # A class that contains all the result data for a star
|_ other                    # Individual classes that mimic the functionality of each BACCHUS module
                              (e.g. bsyn.com, babsma.com, stellar_parameters.tab, ....)
```

## 🤝 Contributing

We welcome contributions! Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- Adding better plotting functionality
- Interfacing with Korg
- Documentation & debugging

## 📚 Citation

If you use `PyBACCHUS` in your research, please cite (bibtex):

```
@misc{obafgkm,
  author = {},
  title = {PyBACCHUS: Interactive Stellar Spectra Plotting Tool},
  year = {2025},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.17070806},
  url = {https://github.com/rocketxturtle/PyBACCHUS}
}
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/rocketxturtle/obafgkm/blob/main/LICENSE) file for details.


## 🙏 Acknowledgments

- Developed partially at [Code/Astro](https://semaphorep.github.io/codeastro/) workshop
- Special thanks to the astronomy community for feedback and testing

## 🐛 Bug Reports & Questions

Found a bug or have a question? Please open an issue on our [GitHub Issues](https://github.com/rocketxturtle/PyBACCHUS/issues) page.

## 🔮 Future Enhancements

- [ ] Add in the code for creating multiple parallelized BACCHI
- [ ] Add in better plotting (e.g. with lines) & reading in the SuperMongo plots
- [ ] Add in functionality for editing linelists

---

**Happy stellar spectroscopy! 🔭✨**

*Remember: The universe is under no obligation to make sense to you, but these spectra might help!*
