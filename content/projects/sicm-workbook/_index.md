+++
template = "projects/workbook.html"
page_template = "projects/page_notitle.html"
title = "SICM Workbook"
sort_by = "title"
description = """
*The Latex formulas in my converted Jupyter Notebooks don't render in the most elegant manner and may sometimes require horizontal scrolling.*
"""
# Generate by running
# jupyter nbconvert --to markdown --template zola <blah.ipynb>
# Add mathjax() tags as necessary

[[extra.chapters]]
number = "1"
title = "Chapter 1 - Lagrangian Mechanics"

[[extra.chapters]]
number = "2"
title = "Chapter 2 - Rigid Bodies"

[[extra.chapters]]
number = "3"
title = "Chapter 3 - Hamiltonian Mechanics"
+++
