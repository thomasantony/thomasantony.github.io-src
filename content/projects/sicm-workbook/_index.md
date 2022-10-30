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
prefix = "1"
title = "Chapter 1 - Lagrangian Mechanics"

[[extra.chapters]]
prefix = "2"
title = "Chapter 2 - Rigid Bodies"
+++
