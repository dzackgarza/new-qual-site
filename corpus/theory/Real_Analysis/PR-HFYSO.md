---
schema: qual/card@1
id: PR-HFYSO
kind: proposition
title: A nonnegative function has integral zero if and only if it vanishes almost everywhere
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure space]] and $f\in$ [[D-BF5L2|$L^+$]].
Then
$$
\int_X f\dmu = 0 \quad\iff\quad f = 0 \ \mu\text{-almost everywhere}.
$$
:::

::: {.proof}
If $f=0$ almost everywhere, every simple function $0\leq\phi\leq f$ vanishes outside a null set, so $\int\phi\dmu=0$, and hence $\int f\dmu=0$.
Conversely, $\theset{f>0}=\bigcup_{n\geq1}E_n$ with $E_n\coloneqq\theset{f>1/n}$, and $\frac1n\mu(E_n)\leq\int_X f\dmu=0$.
So each $\mu(E_n)=0$ and $\mu(\theset{f>0})=0$ by countable subadditivity.
:::
