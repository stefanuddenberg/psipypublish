---
jupyter:
  celltoolbar: Edit Metadata
  hide_input: false
  ipub:
    bibliography: ExampleBib
    listcode: false
    listfigures: false
    listtables: false
    titlepage:
      address:
      - Stefan Uddenberg
      - Peretsman Scully Hall 322
      - Princeton University
      - Princeton, NJ 08540
      - stefanu@princeton.edu
      author: Stefan Uddenberg
      email: stefanu@princeton.edu
      institution:
      - Princeton University
      logo: princeton_logo.pdf
      running_head: PsiPyPublish
      subtitle: ''
      tagline: ''
      title: 'PsiPyPublish: An IPyPublish Template for Psychological Research'
      version: Template file -- not for submission
      word_count: XXX (Main text + abstract)
    toc: true
  jupytext:
    metadata_filter:
      cells:
        additional: all
      notebook:
        additional: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.0'
      jupytext_version: 0.8.6
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.6.2
  toc:
    nav_menu: {}
    number_sections: true
    sideBar: true
    skip_h1_title: false
    toc_cell: false
    toc_position: {}
    toc_section_display: block
    toc_window_display: true
  varInspector:
    cols:
      lenName: 16
      lenType: 16
      lenVar: 40
    kernels_config:
      python:
        delete_cmd_postfix: ''
        delete_cmd_prefix: 'del '
        library: var_list.py
        varRefreshCmd: print(var_dic_list())
      r:
        delete_cmd_postfix: ') '
        delete_cmd_prefix: rm(
        library: var_list.r
        varRefreshCmd: 'cat(var_dic_list()) '
    types_to_exclude:
    - module
    - function
    - builtin_function_or_method
    - instance
    - _Feature
    window_display: false
---

```python
# My default imports for data analysis
%reset -f
%matplotlib inline
%config InlineBackend.figure_format = 'retina' # High-res graphs (rendered irrelevant by svg option below)
%config InlineBackend.print_figure_kwargs = {'bbox_inches':'tight'} # No extra white space
%config InlineBackend.figure_format = 'svg' # 'png' is default
import warnings
warnings.filterwarnings('ignore') # Because we are adults
from IPython.core.debugger import set_trace
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from IPython.display import SVG, display

# ipypublish imports
# See the imported script for matplotlib overrides
# Has helpful commands for displaying images as figures
# from ipypublish.scripts.ipynb_latex_setup import *
```

\renewcommand{\baselinestretch}{1.5} % make PDF's line spacing a little roomier


# Introduction
This is a template for an APA-style [iPyPublish](https://github.com/chrisjsewell/ipypublish) manuscript. Feel free to check out the documentation and examples at that link; it's all very good. There you can find information on how to embed figures, code, tables, and more. References are managed using [Zotero](https://www.zotero.org/) in concert with [Better BibTex](https://github.com/retorquere/zotero-better-bibtex/). For now, you're going to want to edit the notebook's metadata in order to change what appears on the title page. In addition, the metadata includes `jupytext` configuration, so that you can automatically generate markdown and py:percent versions of this notebook automatically on saving -- assuming you have `jupytext` installed and correctly configured, that is! 

## Configuration
My working configuration files for Jupyter (with Jupytext) and iPyPublish can be found in this repository. Naturally, you will need to replace your computer's original versions of these files with the new ones included here. For example, if using Anaconda, your iPyPublish installation can be found at `your_environment_name/Lib/site-packages/ipypublish` .


# Notes


## Production
Produce a notebook in the terminal with the command `nbpublish -pdf -pbug file_name.ipynb` [^1]. Outputs to `converted` folder at the `.ipynb` file's location.

[^1]: \hphantom{} Technically `-pbug` is optional so you can see verbose output, but nbpublish seems to work more reliably with this option enabled.


## Markdown
- Headings and sub-headings (and so on) are made by prefacing text with `#`. The more `#`s, the greater the level of heading.
- Unordered lists are made by prefacing text with a "-".
    1. Numbered lists start with a number and dot.
    2. Create sublists via tabbed indentation.
- Footnote links are made with `[^X]` (where `X` is some number). Footnote content is placed below with `[^X]: Content goes here`. Here's an example.[^2] 
    - Correct formatting only appears after running `nbpublish`.
- [Links](https://google.com) can be generated with the following syntax: `[link](http://www.website.com)`
- `Code` can be placed between backticks (the character to the left of the `1` key at the top of your keyboard).
    - Place it between 3 backticks (with an optional language name) and you get (syntax-highlighted) block code.[^3]
    ```python
    print(foo)```
- *Italic*, __bold__, and ***bolded italic*** text can be created by sandwiching text between 1, 2, or 3 `*`s or `_`s respectively.
- > Blockquotes are made by prefacing text with `>` .

\todo[inline]{Get inline todos with Latex's "todo" command.}

[^2]: \hphantom{} Footnote content goes here!
[^3]:Note, however, that one should not use this for displaying large chunks of code in an nbpublish PDF. Instead, see code cell \cref{code:publish} below for an example of how to place code in the PDF


## Embed HTML, including video
HTML embedding is accomplished via the `%%HTML` cell magic. Naturally, this won't appear in a PDF export.

```python
%%HTML
<iframe width='560' height='315' src='https://www.youtube.com/embed/HW29067qVWk' frameborder='0' allowfullscreen></iframe>
```

## Citations and References
- First, specify the `bibliography` entry in the notebook metadata to the correct bibliography file (Edit --> Edit Notebook Metadata). _Leave out the `.bib` extension from this file name!_ It should look like `path/to/bibFileName` .
    - If nbpublish is having problems finding the `.bib` file, I have had success by placing a copy in the `converted/notebook_name_files/` directory, as well as placing the file in the same folder as the actual notebook. This makes set up for the notebook's bibliography metadata especially easy.
- Citations can be input with citation keys and standard latex commands (e.g., `\cite{citationKey}`).
- I've had success with citation keys generated via Zotero Better BibTex, like so \citep{uddenbergTelefaceSerialReproduction2018}. Note that you won't see the final formatted output until you run `nbpublish`.
- See a [cheat sheet of valid cite commands here](http://merkel.texture.rocks/Latex/natbib.php).


## Figures
- Figures can be displayed with commands like `display(SVG("filename.svg"))` or `Image('filename.jpg', height=400)`.
- Edit the cell's metadata to change the figure caption, placement, size, et al. (View --> Cell Toolbar --> Edit Metadata --> Click on "Edit Metadata" above cell.)
- They can be linked in markdown via `\cref{fig:figNameFromMetadata}`

```python
display(SVG('figures/example.svg'))
```

## Templating — Pass Variables into Markdown
- Pipe valid Python code into markdown directly by sandwiching it between two curly braces: E.g., 2 + 2 = {{str(2 + 2)}}
- Note that the notebook needs to be `Trusted`; look to the top right to see if it is and simply click on `Not Trusted` to change that.


## Latex
- Execute arbitrary latex by sandwiching it between dollar signs: $a = b+c$
- Alternatively, use `Latex()` command from `ipypublish` within a code cell.
- Latex's `hphantom` command is useful when you just want a little more horizontal space between items.


## Terminal commands
- Execute terminal commands in Jupyter by prefacing code with `!` .
- For example, you can export this notebook with the following code cell:

```python
!nbpublish -pdf -pbug template.ipynb
```
