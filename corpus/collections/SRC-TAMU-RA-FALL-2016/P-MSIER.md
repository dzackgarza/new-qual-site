---
schema: qual/card@1
id: P-MSIER
kind: problem
title: Pointwise convergence versus convergence in measure on a finite measure space
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Measure Theory
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Let $(\Omega,\mathcal{A},\mu)$ be a finite measure space and $(f_n)$ be a sequence of measurable functions on $X$ that converges pointwise to zero.
Prove that $(f_n)$ converges in measure to zero.
Show that the converse is false for $[0,1]$ with Lebesgue measure.
:::

:::{.solution}
Fix $\epsilon>0,\delta>0$ and define $A_n=\{x:|f_n(x)|\ge\epsilon\}$. For the $\delta$, By Egoroff's theorem, there is a measurable set $E$ with $\mu(E)<\delta$ and $f_n\to 0$ on $E^c$ uniformly, say, there is a $N$, whenever $n>N$, $x\in E^c$, $|f_n(x)|<\epsilon$. It implies that $A_n\subset E$ and thus $\mu(A_n)<\delta$. It shows that $\mu(A_n)\to 0$, which means $f_n\to 0$ in measure.

For the second part. A counterexample is $f_n=\chi_{[j/2^k,(j+1)/2^k]}$ where $n=2^k+j$ with $0\le j<2^k$ and $k\in\mathbb{N}$.
:::
