---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.0'
      jupytext_version: 0.8.6
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
# Imports
%reset -f
%matplotlib inline
%config InlineBackend.figure_format = 'retina' # High-res graphs (rendered irrelevant by svg option below)
%config InlineBackend.print_figure_kwargs = {'bbox_inches':'tight'} # No extra white space
%config InlineBackend.figure_format = 'svg' # 'png' is default
from ipypublish.scripts.ipynb_latex_setup import *
import warnings
warnings.filterwarnings('ignore') # Because we are adults
from IPython.core.debugger import set_trace
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# ipypublish imports
from ipypublish.scripts.ipynb_latex_setup import *
from IPython.display import SVG, display
```

# Introduction
This is a template for an APA-style [iPyPublish](https://github.com/chrisjsewell/ipypublish) manuscript. Feel free to check out the documentation and examples at that link; it's all very good. There you can find information on how to embed figures, code, tables, and more. References are managed using [Zotero](https://www.zotero.org/) in concert with [Better BibTex](https://github.com/retorquere/zotero-better-bibtex/). For now, you're going to want to edit the notebook's metadata in order to change what appears on the title page. In addition, the metadata includes `jupytext` configuration, so that you can automatically generate a markdown version of this notebook on saving -- assuming you have `jupytext` installed and correctly configured, that is!  


# Notes
- Produce a notebook in the terminal with the command `nbpublish -pdf -pbug file_name.ipynb`
    - Technically `-pbug` is optional so you can see verbose output, but nbpublish seems to work more reliably with this option enabled.
- Figures can be displayed with `display(SVG("filename.svg"))`. Edit the cell's metadata to change the figure caption, placement, size, et al.
- Citations can be generated via Zotero Better BibTex cite keys, like so \citep{uddenbergTelefaceSerialReproduction2018}. It should be formatted correctly when you run `nbpublish`. Be sure See a [cheat sheet of valid cite commands here](http://merkel.texture.rocks/Latex/natbib.php).
    - This only works if you've set the `bibliography` entry in the notebook metadata to the correct file. _Leave out the `.bib` extension from this file name!_ It should look like `path/to/bibFileName`
- Pipe valid Python code into markdown directly with two curly braces, `{{str(2*4)}}`: 
    - Note that the notebook needs to be `Trusted`; look to the top right to see if it is and simply click on `Not Trusted` to change that.
- Footnotes are made like this.[^1] Correct formatting comes at the time of nbpublish-ing.
- TODO: Include example figure.

[^1]: Footnote content goes here!

```python
# display(SVG('figures/Figure 1.svg'))
# Caption (in cell metadata): A depiction of (a) the face stimuli and (b) the masks used throughout the experiments.
```
