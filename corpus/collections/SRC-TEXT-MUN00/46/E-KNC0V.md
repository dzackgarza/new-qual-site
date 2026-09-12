---
schema: qual/card@1
id: E-KNC0V
kind: problem
title: Separation properties of the compact-open topology
classification:
  areas:
  - topology
  topics:
  - Function Spaces
relations: []
review: draft
---

::: {.exercise}

Show that in the compact-open topology, $\mathcal{C}(X, Y)$ is Hausdorff if $Y$ is Hausdorff, and regular if $Y$ is regular.
[Hint: If $\overline{U} \subset V$, then $\overline{S(C, U)} \subset S(C, V)$.]
:::

::: {.solution}
Assume $Y$ Hausdorff. If $f\ne g$ in $C(X,Y)$, choose $x$ with $f(x)\ne g(x)$ and disjoint open neighborhoods $U,V$ of these values. Since $\{x\}$ is compact, the subbasic sets
\[
S(\{x\},U),\qquad S(\{x\},V)
\]
are disjoint neighborhoods of $f,g$. Hence $C(X,Y)$ is Hausdorff.

Now assume $Y$ regular. It suffices to shrink a basic neighborhood
\[
N=\bigcap_{i=1}^n S(C_i,V_i)
\]
of $f$. For each $i$, compactness of $f(C_i)$ and regularity of $Y$ give an open $U_i$ with
\[
f(C_i)\subset U_i,\qquad \overline{U_i}\subset V_i.
\]
Put $M=\bigcap_iS(C_i,U_i)$. Then $f\in M$. The hinted inclusion
\[
\overline{S(C,U)}\subset S(C,V)\quad(\overline U\subset V)
\]
follows because if $h(C)$ is not contained in $V$, choose $x\in C$ with $h(x)\notin V$; the evaluation neighborhood at $x$ avoiding $\overline U$ separates $h$ from $S(C,U)$. Therefore
\[
\overline M\subset\bigcap_i\overline{S(C_i,U_i)}\subset N.
\]
So the function space is regular.
:::
