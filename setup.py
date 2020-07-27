from setuptools import setup
setup(    
     # mandatory
      name='hangman',
      # mandatory
      version='0.1',
      # mandatory
      author_email='bradleywboggs@gmail.com',
      package_data={},
      install_requires=['click'],
      entry_points={
        'console_scripts': ['hangman = main:main']
      }
)