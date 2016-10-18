# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup
try:
    from jupyterpip import cmdclass
except:
    import pip, importlib
    pip.main(['install', 'jupyter-pip']); cmdclass = importlib.import_module('jupyterpip').cmdclass

setup(
    name='ipywidgets_file_selector',
    version='0.1',
    description='ipywidget that allows users to ipython local files and access them in a dict',
    author='Joon-Yee Chuah',
    author_email='jchuah@tacc.utexas.edu',
    license='',
    url='https://github.com/jchuahtacc/ipywidgets_file_selector',
    keywords='python ipython javascript widget ipywidgets_file_selector ipywidgets',
    classifiers=['Development Status :: 4 - Beta',
                 'Programming Language :: Python',
                 'License :: OSI Approved :: MIT License'],
    packages=['ipywidgets_file_selector'],
    include_package_data=True,
    install_requires=["jupyter-pip"],
    cmdclass=cmdclass('ipywidgets_file_selector'),
)
