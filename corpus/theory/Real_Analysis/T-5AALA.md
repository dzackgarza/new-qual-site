---
schema: qual/card@1
id: T-5AALA
kind: theorem
title: Parseval's theorem for orthonormal families
slogan: 'For an orthonormal family, completeness, Parseval equality, and norm-convergent Fourier expansion are equivalent.'
prompts:
- State Parseval's identity, and say when Bessel's inequality becomes it.
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - L²
  - Bases
relations: []
review: draft
---

::: {.theorem}
Let $\mch$ be a [[D-7QQUO|Hilbert space]] and let $(u_n)_{n\in A}$ be a family in $\mch$, indexed by a set $A$, with $\inner{u_n}{u_m}=0$ for $n\neq m$ and $\norm{u_n}=1$ for all $n$.
For each $x\in\mch$ only countably many $\inner{x}{u_n}$ are nonzero ([[T-4BDE3]]), and sums over $A$ below are taken over those indices.
The following are equivalent:

1. (Completeness) If $x\in\mch$ and $\inner{x}{u_n}=0$ for all $n\in A$, then $x=0$.

2. (Parseval's identity) For every $x\in\mch$,
$$
\sum_{n\in A} \abs{ \inner{x}{u_n} }^2 = \norm{x}^2 .
$$

3. (Expansion) For every $x\in\mch$,
$$
x = \sum_{n\in A} \inner{x}{u_n}u_n ,
$$
with the series converging in norm in any enumeration of its nonzero terms; and if $x=\sum_{n\in A}c_nu_n$ for scalars $c_n$, only countably many nonzero, then $c_n=\inner{x}{u_n}$ for all $n$.
:::

::: {.remark title="Variations"}
For an [[D-AQX7W|orthonormal basis]] $(e_k)_{k\geq1}$ of $\mch$, Parseval's identity reads $\sum_{k\geq1}\abs{\inner{x}{e_k}}^2=\norm{x}^2$ for every $x\in\mch$.
It is the case of equality in [[T-4BDE3|Bessel's inequality]], which gives $\sum_{n\in A}\abs{\inner{x}{u_n}}^2\le\norm{x}^2$ for every [[D-4IXAO|orthonormal]] family; by the theorem, equality holds for every $x$ exactly when the family is [[D-SLYE5|complete]].
:::
