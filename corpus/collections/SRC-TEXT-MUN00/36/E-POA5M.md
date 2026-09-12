---
schema: qual/card@1
id: E-POA5M
kind: problem
title: Compact locally imbeddable spaces imbed in euclidean space
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
---

::: {.exercise}

Let $X$ be a compact Hausdorff space.
Suppose that for each $x \in X$, there is a neighborhood $U$ of $x$ and a positive integer $k$ such that $U$ can be imbedded in $\mathbb{R}^k$.
Show that $X$ can be imbedded in $\mathbb{R}^N$ for some positive integer $N$.
:::

::: {.solution}
For each \(x\in X\), choose a neighborhood \(U_x\) and an embedding
\[
e_x:U_x\hookrightarrow\mathbb R^{k_x}.
\]
Since compact Hausdorff spaces are normal, shrink twice: choose open sets
\[
x\in V_x\subset\overline{V_x}\subset W_x\subset\overline{W_x}\subset U_x.
\]
By compactness choose finitely many \(V_1,\dots,V_m\) covering \(X\), with corresponding \(W_i,U_i,e_i:U_i\to\mathbb R^{k_i}\).

By Urysohn's lemma choose continuous functions
\[
\phi_i:X\to[0,1]
\]
such that \(\phi_i=1\) on \(\overline{V_i}\) and \(\phi_i=0\) on \(X\setminus W_i\). Since \(\overline{W_i}\) is compact and lies in \(U_i\), the coordinate functions of \(e_i\) are bounded on \(\overline{W_i}\). Hence the map
\[
F_i:X\to\mathbb R^{k_i},
\qquad
F_i(x)=
\begin{cases}
\phi_i(x)e_i(x),&x\in U_i,\\
0,&x\notin U_i,
\end{cases}
\]
is continuous: near the boundary of \(U_i\), \(\phi_i\) is already zero.

Define
\[
F:X\to\mathbb R^N,
\qquad
F(x)=\bigl(\phi_1(x),F_1(x),\dots,\phi_m(x),F_m(x)\bigr),
\]
where
\[
N=\sum_{i=1}^m(k_i+1).
\]
We show \(F\) is injective. If \(x\ne y\), choose \(i\) with \(x\in V_i\), so \(\phi_i(x)=1\). If \(\phi_i(y)\ne1\), the scalar coordinate \(\phi_i\) separates them. If \(\phi_i(y)=1\), then \(y\in W_i\subset U_i\), and
\[
F_i(x)=e_i(x),\qquad F_i(y)=e_i(y),
\]
which are distinct because \(e_i\) is injective.

Thus \(F\) is a continuous injection from compact \(X\) into Hausdorff \(\mathbb R^N\). It is therefore a homeomorphism onto its image. Hence \(X\) embeds in some finite-dimensional Euclidean space.
:::
