---
schema: qual/card@1
id: E-PKDH7
kind: problem
title: Pointwise boundedness and equicontinuity of four collections
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Which of the following subsets of $\mathcal{C}(\RR, \RR)$ are pointwise bounded?
Which are equicontinuous?

(a) The collection $\theset{f_n}$, where $f_n(x) = x + \sin nx$.

(b) The collection $\theset{g_n}$, where $g_n(x) = n + \sin x$.

(c) The collection $\theset{h_n}$, where $h_n(x) = \abs{x}^{1/n}$.

(d) The collection $\theset{k_n}$, where $k_n(x) = n \sin(x/n)$.
:::

::: {.solution}
(a) For fixed $x$, $\abs{x+\sin nx}\le \abs{x}+1$, so the family is pointwise bounded. It is not equicontinuous: at $0$, for any $\delta>0$ choose $n$ large and $x=\pi/(2n)<\delta$; then $\abs{f_n(x)-f_n(0)}=x+1>1$.

(b) $g_n(x)=n+\sin x$ is not pointwise bounded at any $x$. It is equicontinuous since
$$
\abs{g_n(x)-g_n(y)}=\abs{\sin x-\sin y}\le\abs{x-y}
$$
for all $n$.

(c) The family $h_n(x)=\abs{x}^{1/n}$ is pointwise bounded: for fixed $x$, it lies between $0$ and $\max\{1,\abs{x}\}$. It is not equicontinuous at $0$: given $\delta>0$, choose $0<x<\min\{\delta,1\}$ and then $n$ so large that $x^{1/n}>1/2$, whereas $h_n(0)=0$.

(d) Since $\abs{n\sin(x/n)}\le \abs{x}$, the family is pointwise bounded. Also
$$
\abs{k_n(x)-k_n(y)}\le n\abs{x/n-y/n}=\abs{x-y},
$$
so it is equicontinuous.

Thus (a): bounded, not equicontinuous; (b): equicontinuous, not bounded; (c): bounded, not equicontinuous; (d): both.
:::
