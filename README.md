# `ipywidgets_file_selector`

An IPython Widget that displays files and subdirectories, allowing a user to select items. 

## Usage

This package has one class - `IPFileSelector`. The constrcutor takes an optional `home` argument, specifying the highest directory level that can be browsed. If no `home` argument is supplied, then the current working directory of the IPython notebook as determined by `os.getcwd()` is used.

At any time, client code and access the `selected` [traitlet](https://github.com/ipython/traitlets) member of `IPFileSelector`. It is a dictionary containing a list of files and subdirectories that have been selected by the user. The dictionary structure represents all subdirectories and files relative to the home directory that have been selected.

Subdirectories or files that are `true` are those that have been selected. If individual files within those subdirectories have been selected or deselected, subdirectories will instead be an object containing keys corresponding to all files.

The widget takes a greedy approach to selecting files within a subdirectory. That is to say that if the user selects a directory and then browses into it, all contents of the selected directory are immediately selected. This is designed to account for a user selecting all files within a subdirectory and then de-selecting individual files. Note that this does not automatically happen when writing to the `selected` traitlet. Writing to the `selected` traitlet is designed to allow restoration of a user selection of files that was previously retrieved from the traitlet.

## Acknowledgements

Built from [https://github.com/jdfreder/ipython-widgetboilerplate](https://github.com/jdfreder/ipython-widgetboilerplate) by J. D. Freder.

### Deployment instructions (from original ipython-widgetboilerplate)

Installation is made easy by [jupyter-pip](https://github.com/jdfreder/jupyter-pip).  To install  

```
pip install .
```

For development installs  

```
pip install -e .
```

### Troubleshooting

Sometimes pip or jupyter-pip, or a combination of the two, misbehaves.  When that happens, try installing by using  
```
python setup.py install
```
