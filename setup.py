from setuptools import setup, find_packages

setup(
  name          = 'whixh',
  version       = '0.0.1',
  author        = "Ricardo Signes",
  author_email  = 'pypi@semiotic.systems',
  packages      = find_packages('src'),
  package_dir   = { '': 'src' },
  url           = 'https://github.com/rjbs/whixh',
  keywords      = 'finding the first of several alternatives in $PATH',
  entry_points  = {
    'console_scripts': [
      'whixh=whixh:execute',
    ],
  },
  classifiers   = [
    'License :: OSI Approved :: Apache Software License'
  ]
)
