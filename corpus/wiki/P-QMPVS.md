---
schema: qual/card@1
id: P-QMPVS
kind: problem
title: "a. Prove Holder's inequality:"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
a. Prove Holder's inequality:
  let $f\in L^p, g\in L^q$ with $p, q$ conjugate, and show that
\[
\pnorm{fg}p \leq \pnorm{f}p \cdot \pnorm{g}q
.\]

b. Prove Minkowski's Inequality:
\[
1\leq p < \infty \implies \pnorm{f+g}{p} \leq \pnorm{f}{p}+ \pnorm{g}{p}
.\]
Conclude that if $f, g\in L^p(\RR^n)$ then so is $f+g$.

c. Let $X = [0, 1] \subset \RR$.

    1. Give a definition of the Banach space $L^\infty(X)$ of essentially bounded functions of $X$.

    2. Let $f$ be non-negative and measurable on $X$, prove that
    \[
    \int_X f(x)^p \,dx \converges{p\to\infty}\to
    \begin{dcases}
    \infty \quad\text{or} \\
    m\qty{\theset{f\inv(1)}}
    \end{dcases}
    ,\]
    and characterize the functions of each type


:::{.solution}
\[
\int f^p 
&= \int_{x < 1} f^p + \int_{x=1}f^p + \int_{x > 1} f^p\\
&= \int_{x < 1} f^p + \int_{x=1}1 + \int_{x > 1} f^p \\
&= \int_{x < 1} f^p + m(\theset{f = 1}) + \int_{x > 1} f^p \\
&\converges{p\to\infty}\to 0  + m(\theset{f = 1}) + 
\begin{cases} 
0 & m(\theset{x\geq 1}) = 0 \\ 
\infty & m(\theset{x\geq 1}) > 0.
\end{cases}
\] 

:::
