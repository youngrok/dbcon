from setuptools import setup, find_packages


setup(name='dbcon',
      description='Database configuration tool for database-backed applications',
      author='Youngrok Pak',
      author_email='pak.youngrok@gmail.com',
      keywords= 'database configuration django yaml connection',
      url='https://github.com/youngrok/dbcon',
      version='0.0.1',
      packages=find_packages(),
      scripts=['bin/dbcon'],
      classifiers = [
                     'Development Status :: 3 - Alpha',
                     'Topic :: Software Development :: Libraries',
                     'License :: OSI Approved :: BSD License']
      )
