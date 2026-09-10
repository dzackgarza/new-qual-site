---
schema: qual/card@1
id: E-ARGEV
kind: problem
title: Pointwise bounded collections that fail equicontinuity
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

(a) Let $f_n: I \to \mathbb{R}$ be the function $f_n(x) = x^n$.
The collection $\mathcal{F} = \ts{f_n}$ is pointwise bounded but the sequence $(f_n)$ has no uniformly convergent subsequence; at what point or points does $\mathcal{F}$ fail to be equicontinuous?

(b) Repeat (a) for the functions $f_n$ of Exercise 9 of §21.
:::

::: {.solution}
For $f_n(x)=x^n$, equicontinuity holds at every $x_0<1$: choose $a$ with $x_0<a<1$; on a sufficiently small neighborhood contained in $[0,a]$, the finitely many small $n$ are uniformly continuous, while for all sufficiently large $n$ both $x^n$ and $x_0^n$ are arbitrarily small. At $x_0=1$ equicontinuity fails: for every $\delta>0$, choose $x<1$ with $1-\delta<x<1$ and then $n$ so large that $x^n<1/2$, whereas $f_n(1)=1$.

For the sequence from §21 Exercise 9,
\[
f_n(x)=\frac1{n^3(x-1/n)^2+1},
\]
the family fails equicontinuity exactly at $0$. Indeed $f_n(0)=1/(n+1)\to0$ but $f_n(1/n)=1$, and $1/n\to0$, contradicting equicontinuity at $0$. If $x_0\ne0$, choose a neighborhood $J$ of $x_0$ whose closure avoids $0$. For large $n$, $1/n$ stays a fixed positive distance from $J$, so both $f_n$ and its derivative tend uniformly to $0$ on $J$; the finitely many remaining functions are uniformly continuous there. Thus the family is equicontinuous at every $x_0\ne0$.
:::
