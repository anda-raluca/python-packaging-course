from setuptools import setup

setup(name='tstools_AndaVersion',
      version='0.1',
      description='A package to analyse cool timeseries',
      url='myfancywebsite.com',
      author='Anda',
      email= 'anda@email.com',
      packages=['tstools'],
      install_requires=["numpy", "matplotlib", "scipy"],
      license='GPLv3')