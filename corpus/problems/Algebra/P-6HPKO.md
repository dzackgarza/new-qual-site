---
schema: qual/card@1
id: P-6HPKO
kind: problem
title: $G/Z(G)$ cyclic implies $G$ abelian
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Abelian Groups
  - Cyclic Groups
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
Prove that if $G/Z(G)$ is cyclic, then $G$ is abelian.
:::

::: {.solution}
Write $Z=Z(G)$ and suppose
\[
G/Z=\langle gZ\rangle.
\]

<1>1. Every element of $G$ can be written as $g^m z$ for some $m\in\ZZ$ and $z\in Z$.
::: {.proof}
If $x\in G$, then its coset lies in the cyclic quotient, so
\[
xZ=(gZ)^m=g^mZ
\]
for some $m$. Hence
\[
g^{-m}x\in Z,
\]
so $x=g^m z$ for some $z\in Z$.
:::

<1>2. Any two elements of $G$ commute.
::: {.proof}
Take
\[
x=g^m z_1,
\qquad
y=g^n z_2
\]
with $z_1,z_2\in Z$ by <1>1. Since the $z_i$ are central,
\[
xy=g^m z_1g^n z_2=g^{m+n}z_1z_2
=g^{m+n}z_2z_1=g^n z_2g^m z_1=yx.
\]
:::

<1>3. Therefore $G$ is abelian.
::: {.proof}
By <1>2, every pair of elements of $G$ commutes.
:::
:::
