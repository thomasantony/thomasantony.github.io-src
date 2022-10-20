+++
title = "Projects"
+++

This page will list some of my projects and log my progress self-studying different topics of interest to me.

### Self Study -- Classical Mechanics

Go to [**Workbook**](/projects/sicm-workbook)

I am currently in the process of studying classical mechanics using *[Structure and Interpretation of Classical Mechanics](https://tgvaughan.github.io/sicm/
)* (aka SICM) by Gerald Sussman and Jack Wisdom. This is part of working towards my eventual goal of properly understanding the math behind General Relativity. Once I am done with SICM, I will move on to [*Functional Differential Geometry*](https://mitpress.mit.edu/books/functional-differential-geometry) (aka FDG) by the same authors. I have taken a couple of courses on Classical Mechanics and Variational Calculus while in gradschool. But this is the first book on the subject that I have found to be engaging while also explaining the concepts really well. I am hoping that the GR book will be similarly elucidating on the subject.

The key factor that sets aside SICM (and FDG) from other textbooks is that it uses computer programs as a way to present its ideas. Expressing the concepts in a computer language (in this case, [Scheme](https://en.wikipedia.org/wiki/Scheme_(programming_language)
)), forces the author to be precise and unambiguous. The authors have written a library called [scmutils](https://groups.csail.mit.edu/mac/users/gjs/6946/installation.html) that is required for implementing the methods presented in the book while working through it. Sam Ritchie has made a Clojure version of `scmutils` called [sicmutils](https://github.com/sicmutils/sicmutils). This is what I used to create my workbooks, along with along with [CloJupyter](https://github.com/clojupyter/clojupyter).

With all that said, I still find a few spots where a step is missing or it is not entirely clear how the authors came to a certain conclusion. In these cases, I think it is important to note it down, so that it can be a reference for me (and others) in the future. To this end, I will be publishing my notes and exercise solutions [here](/projects/sicm-workbook). These are Jupyter notebooks converted into markdown and then to HTML. The formatting may not be perfect, but it is better than nothing. 


#### References
* *[Structure and Interpretation of Classical Mechanics](https://tgvaughan.github.io/sicm/)*, Gerald J. Sussman and Jack Wisdom
* *[No-Nonsense Classical Mechanics](https://nononsensebooks.com/cm/)*, Jakob Schwichtenberg
