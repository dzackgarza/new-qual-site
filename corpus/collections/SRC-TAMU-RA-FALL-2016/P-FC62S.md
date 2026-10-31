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
Prove that $\phi$ achieves its norm; that is, prove that there is a norm one vector $x$ in $X$ such that $\phi(x)=\norm{\phi}$.
Show by example that there is a continuous linear functional on the Banach space $\ell_1$ that does not achieve its norm.
Give an counterexample in the case $X=l_1$.
:::

::: {.solution}
By problem 11 in Jan 2017, we see the Ball $B$ of $X$ is weak compact.
It is also easy to verify that $\phi$ is weak continuous since it is norm continuous and so is $\abs{\phi}$.
Then $\abs{\phi}$ achieve the max value on $B$, say there is an element $x$ such that $\abs{\phi(x)}=\max_{y\in B}\abs{\phi(y)}\ge\sup\{\abs{\phi(y)}:\norm{y}\le 1\}=\norm{\phi}$.
Thus $\abs{\phi(x)}=\norm{\phi}$ and $\norm{x}=1$ holds necessarily by $\abs{\phi(x)}\le\norm{\phi}\norm{x}$.
Then we can choose a number $e^{i\theta}$ such that $\phi(e^{i\theta}x)=\abs{\phi(x)}=\norm{\phi}$ and $\norm{e^{i\theta}x}=1$.

A counterexample: $l_1^*=l_\infty$.
Then let $f=(1-1/n)_n\in l_\infty$.
Then for every $x=(\alpha_n)\in l_1$ of norm 1, $\abs{f(x)}=\abs{\sum_n(1-1/n)\alpha_n}\le\sum_n(1-1/n)\abs{\alpha_n}<\sum_n\abs{\alpha_n}=1=\norm{f}$.
:::
