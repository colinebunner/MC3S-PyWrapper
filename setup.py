from setuptools import setup

setup(name='cssi_mcccs',
      version='0.1',
      description='A set of Python programs for organizing and running MCCCS-MN simulations.',
      url='https://github.com/colinebunner/CSSI_MCCCS',
      author='Colin Bunner',
      author_email='colinebunner@gmail.com',
      license='GNU',
      packages=['cssi_mcccs','cssi_mcccs/classes'],
      install_requires = [
        'numpy',
      ],
      zip_safe=False)
