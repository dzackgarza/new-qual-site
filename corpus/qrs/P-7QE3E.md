---
schema: qual/card@1
id: P-7QE3E
kind: problem
title: "Let $F \\subset \\mathbb{R}$ be closed, and define"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
a.
Let $F \subset \mathbb{R}$ be closed, and define
\[
\delta_{F}(y):=\inf _{x \in F}|x-y| .
\]
For $y \notin F$, show that
\[
\int_{F}|x-y|^{-2} d x \leq \frac{2}{\delta_F(y)},
\]
b.
Let $F \subset \mathbb{R}$ be a closed set whose complement has finite measure, i.e. $m(R \sm F)< \infty$. 
Define the function
\[
I(x):=\int_{\mathbb{R}} \frac{\delta_{F}(y)}{|x-y|^{2}} d y
\]
Prove that $I(x)=\infty$ if $x \not\in F$, however $I(x)<\infty$ for almost every $x \in F$. 

  > Hint: investigate $\int_{F} I(x) d x$.


