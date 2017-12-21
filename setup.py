from setuptools import setup

setup(
   name='demo',
   version='1.0',
   description='A useful module',
   author='Ashi',
   packages=['test'],  #same as name
   install_requires=['flask'], #external packages as dependencies
)
