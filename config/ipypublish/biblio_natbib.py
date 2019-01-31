tplx_dict = {
    "meta_docstring": "with the main ipypublish bibliography",
    "document_packages": r"""
	% bibliography formatting
	\usepackage[natbibapa, nodoi]{apacite} % WORKING -- suppresses doi
	% \usepackage[numbers, square, super, sort&compress]{natbib} % ORIG
	% hyperlink doi's
	\usepackage{doi}
""",
    "document_bibliography": r"""
((*- if nb.metadata.ipub: -*))
((*- if nb.metadata.ipub.bibliography: -*))
((* set filename = nb.metadata.ipub.bibliography | posix_path *))

% sort citations by order of first appearance
\bibliographystyle{apacite} % formerly unsrtnat with natbib
\setlength\bibsep{\baselineskip} % increase space between refs
\bibliography{((( filename )))}

((*- endif *))
((*- endif *))
""",
}
