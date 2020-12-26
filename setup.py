from setuptools import setup

setup(name='mc3s_pywrapper',
      version='0.1',
      description='A set of Python programs for organizing and running MCCCS-MN simulations.',
      url='https://github.com/colinebunner/MC3S-PyWrapper',
      author='Colin Bunner',
      author_email='colinebunner@gmail.com',
      license='GNU',
      packages=['mc3s_pywrapper','mc3s_pywrapper/sections','mc3s_pywrapper/utilities','mc3s_pywrapper/writers'],
      install_requires = [
        'numpy',
      ],
      zip_safe=False)
