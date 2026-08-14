---
schema: qual/card@1
id: P-CYNHH
kind: problem
title: "Find the Laurent expansions about $z=0$ of the following\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - laurent-series
  - essential-singularities
  - principal-parts
relations: []
review: draft
---
Find the Laurent expansions about $z=0$ of the following functions:
\[
e^{1\over z} \hspace{8em} \cos \qty{1\over z}
.\]

:::{.solution}
\hfill
:::{.concept}
\hfill

:::
Let $f(z) = {z+1\over z(z-1)}$.

About $z=0$:

\begin{align*}
f(z) 
&= (z+1) \qty{- {1 \over z} + {1\over z-1} } \\
&=  -(z+1) \qty{{1\over z} + \sum_{n=0}^\infty z^n } \\
&= -(z+1)\sum_{n=-1}^\infty z^n \\
&= {1\over z} + 2\sum_{n=0}^\infty z^n \\
&= -{1\over z} -2 - 2z - 2z^2 - \cdots
.\end{align*}

About $z=1$:

\begin{align*}
f(z) 
&= \qty{(1-z) -2 \over 1-z} \qty{1 \over 1 - (1-z)} \\
&= \qty{1 - {2\over 1-z}} \sum_{n=0}^\infty (1-z)^n \\ 
&= \sum_{n=0}^\infty (1-z)^n - 2 \sum_{n=-1}^\infty (1-z)^n \\
&= -{2\over 1-z} - \sum_{n=0}^\infty (1-z)^n \\
&= {2\over z-1} + \sum_{n=0}^\infty (-1)^{n+1} (z-1)^n \\
&= {2\over z-1} - 1 + (z-1) - (z-1)^2 + \cdots
.\end{align*}


:::


