try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='pkm2png',
      version='0.1',
      description='Convert PKM files to PNG images.',
      author='Patrick Jacobs',
      author_email='ceolwulf@gmail.com',
      keywords=['pkm', 'pokemon', 'image', 'png'],
      url='https://github.org/ceol/pkm2png',
      packages=['pkm2png'],
     )