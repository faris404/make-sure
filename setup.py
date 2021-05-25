# from distutils.core import setup
from setuptools import setup

with open('README.md','r') as f:
    long_description = f.read()




setup(
  name = 'makesure',        
  packages = ['makesure'],   
  version = '0.3',      
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'simple validator for input data (only for python dic)', 
  author = 'Muhammed Faris',               
  author_email = 'faris.um2000@gmail.com',     
  long_description=long_description,
  long_description_content_type="text/markdown", 
  url = 'https://github.com/faris404/make-sure',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/faris404/make-sure/archive/v_0.1.tar.gz',    # I explain this later on
  keywords = ['makesure', 'validation', 'parser','json validator'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.6',    
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)