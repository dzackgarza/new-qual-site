---
schema: qual/card@1
id: P-CKJ7C
kind: problem
title: Representations of $S_3$ and restriction to $S_2$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Character Theory
  - Permutations
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
What are the finite-dimensional complex representations of $S_3$?
How do they restrict to $S_2$?
:::


::: {.solution}
Let $H=S_2=\langle(12)\rangle\le S_3$.

<1>1. Up to isomorphism, $S_3$ has exactly three irreducible complex representations: the trivial representation $\mathbf 1$, the sign representation $\mathrm{sgn}$, and the two-dimensional standard representation $V$.
::: {.proof}
The conjugacy classes of $S_3$ have cycle types
\[
1^3,\qquad 2\,1,\qquad 3,
\]
so there are three irreducible complex representations. Their dimensions $d_i$ satisfy
\[
\sum_i d_i^2=|S_3|=6.
\]
The trivial and sign representations give two one-dimensional irreducibles. The remaining dimension must therefore satisfy
\[
1^2+1^2+d^2=6,
\]
so $d=2$. The standard representation on
\[
\{(x_1,x_2,x_3)\in\CC^3:x_1+x_2+x_3=0\}
\]
is irreducible and supplies this two-dimensional representation.
:::

<1>2. Every finite-dimensional complex representation of $S_3$ is a direct sum of copies of these three irreducibles.
::: {.proof}
Maschke's theorem applies because $\operatorname{char}\CC=0$ does not divide $|S_3|$. Hence every finite-dimensional representation is completely reducible.
:::

<1>3. Their restrictions to $H\cong C_2$ are
\[
\mathbf1|_H\cong\mathbf1_H,
\qquad
\mathrm{sgn}|_H\cong\mathrm{sgn}_H,
\qquad
V|_H\cong\mathbf1_H\oplus\mathrm{sgn}_H.
\]
::: {.proof}
The first two are immediate. For the standard representation, the transposition $(12)$ acts on
\[
V=\{x_1+x_2+x_3=0\}
\]
with eigenvectors
\[
(1,1,-2)\quad\text{of eigenvalue }1,
\qquad
(1,-1,0)\quad\text{of eigenvalue }-1.
\]
Thus as a representation of $H$, $V$ splits as the direct sum of the trivial and sign characters.
:::
:::
