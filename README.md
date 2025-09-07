# PyBACCHUS
[![DOI](https://zenodo.org/badge/1034636798.svg)](https://doi.org/10.5281/zenodo.17070805)

A Python Wrapper for running the Brussels Automatic Code for Characterizing High accUracy Spectra (BACCHUS)

[![A rectangular badge, half black half purple containing the text made at Code Astro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A Python Wrapper for running the Brussels Automatic Code for Characterizing High accUracy Spectra (BACCHUS). 

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

- **Interactive Stellar Spectra Plotting**: Generate and visualize synthetic stellar spectra with customizable parameters
- **Wide Parameter Range**: 
  - Effective temperatures: 3000K - 8000K
  - Surface gravities: log(g) = 0.0 - 5.0 dex
  - Metallicities: subsolar ([M/H]=-2.0), solar ([M/H]=0.0), and supersolar ([M/H]=0.5)
- **Dual Spectra Display**: View both normalized and unnormalized flux spectra
- **Spectral Line Markers**: Automatic labeling of important spectral features (Ca H/K, H-alpha, H-beta, Na D lines)
- **Export Capabilities**: Save high-resolution plots for publications and presentations
- **Pre-computed Spectra**: Fast loading from pre-synthesized MARCS/Korg models

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
obafgkm/
├── __init__.py              # Package initialization and version info
├── main.py                  # Core Star class and spectra selection
├── plot.py                  # Plotting utilities and visualization
├── prompt.py                # Interactive user interface
├── rcparams.txt            # Matplotlib configuration settings
├── star_types.csv          # Database of available stellar spectra
├── normalized_spectra/     # Pre-computed normalized flux spectra
├── unnormalized_spectra/   # Pre-computed unnormalized flux spectra
└── plots/                  # Saved plot outputs (created on first save)
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
  author = {{Gozman, Katya}, {Sinha, Amaya}, {Schochet, Meir}, {Ramon, Lisha}},
  title = {obafgkm: Interactive Stellar Spectra Plotting Tool},
  year = {2025},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.16762220},
  url = {https://github.com/rocketxturtle/obafgkm}
}
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/rocketxturtle/obafgkm/blob/main/LICENSE) file for details.


## 🙏 Acknowledgments

- Developed partially at [Code/Astro](https://semaphorep.github.io/codeastro/) workshop
- Special thanks to the astronomy community for feedback and testing

## 🐛 Bug Reports & Questions

Found a bug or have a question? Please open an issue on our [GitHub Issues](https://github.com/rocketxturtle/obafgkm/issues) page.

## 🔮 Future Enhancements

- [ ] Extend temperature range to include O/B stars (>8000 K)
- [ ] Add ultra-cool dwarfs (<3000 K)
- [ ] Implement spectral classification algorithms
- [ ] Add interactive Jupyter widget interface
- [ ] Include additional spectral line identification tools
- [ ] Support for custom wavelength ranges
- [ ] Integration with observational data formats

---

**Happy stellar spectroscopy! 🔭✨**

*Remember: The universe is under no obligation to make sense to you, but these spectra might help!*
