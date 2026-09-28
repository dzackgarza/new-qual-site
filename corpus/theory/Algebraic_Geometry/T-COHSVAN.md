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
- How is ampleness characterised cohomologically?
---

::: {.theorem}
Let $A$ be noetherian, let $X$ be projective over $A$ with $\OO_X(1)$ very ample, and let $\mcf$ be [[D-QNTZY|coherent]]. Then there is $n_0$ such that
$$
H^i(X, \mcf(n)) = 0 \quad \text{for all } i > 0 \text{ and all } n \geq n_0 .
$$
[@Har10a, Theorem III.5.2]
:::

::: {.remark title="Dependence of the bound on the sheaf"}
For a field $k$ and an integer $m\ge0$, the sheaf $\OO_{\PP_k^1}(-m)$ has vanishing positive-degree cohomology after twisting by every $n\ge m$.
At $n=m-2$, its first cohomology has dimension one [@Har10a, Theorem III.5.1]. Thus this family on $\PP_k^1$ has no common twist bound as $m$ varies; [[T-MODSERRE]] gives the explicit cohomology and global-generation bounds.
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

::: {.theorem title="Cohomological criterion for ampleness"}
Let $A$ be noetherian, let $Y$ be proper over $A$, and let $\mcl$ be an invertible sheaf on $Y$.
Then $\mcl$ is ample if and only if, for every [[D-QNTZY|coherent]] sheaf $\mcg$ on $Y$, there exists an integer $N$ such that
$$
H^i(Y,\mcg\otimes_{\OO_Y}\mcl^{\otimes n})=0
\quad\text{for every }i>0\text{ and every }n\ge N.
$$
[@Har10a, III.5.3]
:::
