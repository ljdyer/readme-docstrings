# README Docstrings

A Python library for pulling docstrings from Python code files into markdown files.

I developed this library to enable me to build README files from templates so that I could include docstrings from .py files in my GitHub README pages without having to manually update them every time I update my code.

## Template syntax

### Config variables

Config variables are marked with the tag `[-^`.

- `TARGET` config variable specifies the file to write to.
- Other named variables specify paths to files containing Python code.

E.g.
```
[-^TARGET=README.md
[-^FRMG=frmg/feature_restorer_metric_getter.py
```

### Docstring references

Docstring references begin with `[-*`.

E.g.
```
[-*method FRMG>show_confusion_matrices
```
