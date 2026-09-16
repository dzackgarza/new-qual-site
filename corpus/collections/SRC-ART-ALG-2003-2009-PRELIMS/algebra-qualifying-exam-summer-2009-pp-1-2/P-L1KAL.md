---
schema: qual/card@1
id: P-L1KAL
kind: problem
title: $L = K(\alpha)$ iff the Galois conjugates of $\alpha$ are distinct
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
  note: "Compared the Galois hypothesis and both directions with page 2 of the original scan, Fields 3."
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $L/K$ be a Galois extension of fields, with Galois group $G = \{\sigma_1, \dots, \sigma_n\}$, and let $\alpha \in L$.
Prove that $L = K(\alpha)$ iff $\sigma_1(\alpha), \dots, \sigma_n(\alpha)$ are distinct.
:::

::: {.solution}
The finite Galois group in the hypothesis gives
$[L:K]=|G|=n$ [@DF04]. Let $m_\alpha\in K[x]$ be the minimal
polynomial of $\alpha$ and put $d=\deg m_\alpha=[K(\alpha):K]$.

<1>1. If $L=K(\alpha)$, the $n$ displayed conjugates are distinct.

::: {.proof}
Suppose $\sigma_i(\alpha)=\sigma_j(\alpha)$. Every element of $K(\alpha)$
is a rational expression in $\alpha$ with coefficients in $K$.
Both automorphisms fix those coefficients, and their agreement on
$\alpha$ therefore makes them agree on every element of $L=K(\alpha)$.
Thus $\sigma_i=\sigma_j$, and the enumeration of $G$ gives $i=j$.
:::

<1>2. If the $n$ displayed conjugates are distinct, then $L=K(\alpha)$.

::: {.proof}
For each $i$, fixing the coefficients of $m_\alpha$ gives
$$
m_\alpha(\sigma_i(\alpha))
=\sigma_i(m_\alpha(\alpha))=0.
$$
Thus $m_\alpha$ has at least $n$ distinct roots, so $d\geq n$.
On the other hand, the tower law in $K\subseteq K(\alpha)\subseteq L$
gives $n=[L:K(\alpha)]d$, and hence $d\leq n$.
It follows that $d=n$ and $[L:K(\alpha)]=1$, proving the conclusion.
:::
:::
