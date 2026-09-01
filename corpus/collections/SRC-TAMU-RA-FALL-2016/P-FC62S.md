---
schema: qual/card@1
id: P-FC62S
kind: problem
title: Every functional on a reflexive Banach space attains its norm; a counterexample
  in $\ell^1$
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Norms
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Assume that $X$ is a reflexive Banach space and $\phi$ is a continuous linear functional on $X$.
Prove that there is a norm one vector $x$ such that $\phi(x)=\|\phi\|$.
Give an counterexample in the case $X=l_1$.
:::

:::{.solution}
By problem 11 in Jan 2017, we see the Ball $B$ of $X$ is weak compact. It is also easy to verify that $\phi$ is weak continuous since it is norm continuous and so is $|\phi|$. Then $|\phi|$ achieve the max value on $B$, say there is an element $x$ such that $|\phi(x)|=\max_{y\in B}|\phi(y)|\ge\sup\{|\phi(y)|:\|y\|\le 1\}=\|\phi\|$. Thus $|\phi(x)|=\|\phi\|$ and $\|x\|=1$ holds necessarily by $|\phi(x)|\le\|\phi\|\|x\|$. Then we can choose a number $e^{i\theta}$ such that $\phi(e^{i\theta}x)=|\phi(x)|=\|\phi\|$ and $\|e^{i\theta}x\|=1$.

A counterexample: $l_1^*=l_\infty$. Then let $f=(1-1/n)_n\in l_\infty$. Then for every $x=(\alpha_n)\in l_1$ of norm 1, $|f(x)|=|\sum_n(1-1/n)\alpha_n|\le\sum_n(1-1/n)|\alpha_n|<\sum_n|\alpha_n|=1=\|f\|$.
:::
