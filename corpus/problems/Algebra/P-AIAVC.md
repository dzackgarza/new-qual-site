---
schema: qual/card@1
id: P-AIAVC
kind: problem
title: Whether representations conjugate at each $g\in G$ are isomorphic
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Character Theory
  - Conjugacy
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
If you have two finite-dimensional complex representations $\pi_1$ and $\pi_2$ of a finite group $G$ such that $\pi_1(g)$ is conjugate to $\pi_2(g)$ for every g in $G$, is it true that the two representations are isomorphic?
:::


::: {.solution}
Yes.

<1>1. The two representations have the same character.
::: {.proof}
For every $g\in G$, the matrices $\pi_1(g)$ and $\pi_2(g)$ are conjugate. Conjugate matrices have the same trace, so
\[
\chi_{\pi_1}(g)=\operatorname{tr}(\pi_1(g))=\operatorname{tr}(\pi_2(g))=\chi_{\pi_2}(g)
\]
for every $g\in G$. Thus
\[
\chi_{\pi_1}=\chi_{\pi_2}.
\]
:::

<1>2. Finite-dimensional complex representations of a finite group are determined up to isomorphism by their characters.
::: {.proof}
By Maschke's theorem both representations are completely reducible. Write
\[
\pi_i\cong\bigoplus_{V\in\operatorname{Irr}(G)} m_{i,V}V.
\]
Taking characters gives
\[
\chi_{\pi_i}=\sum_V m_{i,V}\chi_V.
\]
The irreducible complex characters are linearly independent (indeed orthonormal under the standard character inner product), so equality of the two characters forces
\[
m_{1,V}=m_{2,V}
\]
for every irreducible $V$.
:::

<1>3. Hence $\pi_1\cong\pi_2$.
::: {.proof}
By <1>2, the two semisimple decompositions have the same irreducible multiplicities.
:::
:::
