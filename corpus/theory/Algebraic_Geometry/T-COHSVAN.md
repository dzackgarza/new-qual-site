---
schema: qual/card@1
id: T-COHSVAN
kind: theorem
title: Serre vanishing for large twists
slogan: 'Sufficiently positive twists kill higher coherent cohomology; conversely, that eventual vanishing for every coherent sheaf characterizes ampleness.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Vanishing Theorems
  - Twisting Sheaves
relations:
- kind: uses
  target: T-COHFIN
review: draft
prompts:
- State Serre vanishing.
- What does "$n \gg 0$" depend on?
---

::: {.theorem}
Let $A$ be noetherian, let $X$ be projective over $A$ with $\OO_X(1)$ very ample, and let $\mcf$ be [[D-QNTZY|coherent]]. Then there is $n_0$ such that
$$
H^i(X, \mcf(n)) = 0 \quad \text{for all } i > 0 \text{ and all } n \geq n_0 .
$$
[@Har10a, Theorem III.5.2]
:::

::: {.remark title="Dependence of the bound on the sheaf"}
For a field $k$ and an integer $m\ge0$,
$$
H^1\bigl(\PP_k^1,\OO(n-m)\bigr)=0
\quad\Longleftrightarrow\quad
n\ge m-1.
$$
At $n=m-2$, this first cohomology group is one-dimensional [@Har10a, Theorem III.5.1]. Thus the family $\OO_{\PP_k^1}(-m)$ has no common Serre-vanishing bound as $m$ varies; [[T-MODSERRE]] gives the explicit cohomology and global-generation bounds.
:::

::: {.remark title="Euler characteristics over a field"}
Suppose $A=k$ is a field.
The dimensions $h^i(X,\mcf(n))=\dim_k H^i(X,\mcf(n))$ are finite by [[T-COHFIN]]. For all sufficiently large $n$, Serre vanishing gives
$$
\chi(X,\mcf(n))=\sum_i(-1)^i h^i(X,\mcf(n))=h^0(X,\mcf(n)).
$$
If $S$ is a finitely generated graded $k$-algebra with $S_0=k$, generated in degree one, and $M$ is a finite graded $S$-module with $X=\Proj S$ and $\mcf=\widetilde M$, then [[P-AGH259GAMMASTAR]] identifies the last term with $\dim_k M_n$ for all sufficiently large $n$.
Consequently this Euler characteristic agrees in large degrees with the Hilbert polynomial of $M$ [@Har10a, Chapter I, §7].
:::

::: {.remark title="Converse"}
On a proper scheme over a noetherian ring, eventual vanishing of higher cohomology for every coherent sheaf characterizes ampleness; this is the cohomological part of [[T-DIVSERRE]].
:::
