---
schema: qual/card@1
id: P-G2KO6
kind: problem
title: Chinese remainder theorem
classification:
  areas:
  - algebra
  topics:
  - Chinese Remainder Theorem
  - Ideals
  - Number Theory
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
State the Chinese remainder theorem in any form you like.
Prove it.
:::


::: {.solution}
Let $R$ be a commutative ring and let $I_1,\dots,I_n$ be pairwise comaximal ideals. The Chinese remainder theorem states that the natural map
\[
\phi:R\to\prod_{i=1}^n R/I_i,
\qquad
r\mapsto(r+I_1,\dots,r+I_n)
\]
is surjective and has kernel
\[
\ker\phi=\bigcap_{i=1}^n I_i=I_1\cdots I_n.
\]
Hence
\[
R/(I_1\cdots I_n)\cong\prod_{i=1}^nR/I_i.
\]

<1>1. The kernel is $\bigcap_i I_i$.
::: {.proof}
By definition, $\phi(r)=0$ exactly when $r\in I_i$ for every $i$.
:::

<1>2. For pairwise comaximal ideals,
\[
\bigcap_i I_i=I_1\cdots I_n.
\]
::: {.proof}
It suffices to prove the two-ideal case and iterate. If $I+J=R$, choose $a\in I$ and $b\in J$ with $a+b=1$. For $x\in I\cap J$,
\[
x=x(a+b)=xa+xb\in IJ.
\]
The reverse inclusion $IJ\subseteq I\cap J$ is automatic.
:::

<1>3. The map $\phi$ is surjective.
::: {.proof}
For each $i$, pairwise comaximality gives
\[
I_i+\prod_{j\ne i}I_j=R.
\]
Choose $e_i\in\prod_{j\ne i}I_j$ with $e_i\equiv1\pmod{I_i}$. Then $e_i\equiv0\pmod{I_j}$ for $j\ne i$. Given residues $r_i+I_i$, the element
\[
r=\sum_i r_i e_i
\]
has $r\equiv r_i\pmod{I_i}$ for every $i$.
:::

The first isomorphism theorem now gives the claimed product decomposition.
:::
