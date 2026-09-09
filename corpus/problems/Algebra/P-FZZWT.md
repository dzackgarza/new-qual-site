---
schema: qual/card@1
id: P-FZZWT
kind: problem
title: Group representations and their traces
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Character Theory
  - Trace
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Do you know what a group representation is?
Do you know what the trace of a group representation is?
:::


::: {.solution}
A finite-dimensional representation of a group $G$ over a field $F$ is a homomorphism
\[
\rho:G\to\operatorname{GL}(V)
\]
for some finite-dimensional $F$-vector space $V$.

The trace attached to the representation is its character
\[
\chi_\rho:G\to F,
\qquad
\chi_\rho(g)=\operatorname{tr}(\rho(g)).
\]

<1>1. The character is constant on conjugacy classes.
::: {.proof}
For $g,h\in G$,
\[
\rho(hgh^{-1})=\rho(h)\rho(g)\rho(h)^{-1}.
\]
Trace is invariant under similarity, so
\[
\chi_\rho(hgh^{-1})=\chi_\rho(g).
\]
:::

<1>2. Isomorphic representations have the same character.
::: {.proof}
If $\rho_1$ and $\rho_2$ are isomorphic, then for some invertible $T$,
\[
\rho_2(g)=T\rho_1(g)T^{-1}
\]
for every $g$. Again trace is similarity-invariant.
:::

Thus the trace packages a representation into a class function; over $\CC$ for finite groups, the character in fact determines the representation up to isomorphism.
:::
