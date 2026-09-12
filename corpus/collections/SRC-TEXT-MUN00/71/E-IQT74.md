---
schema: qual/card@1
id: E-IQT74
kind: problem
title: Hausdorffness of wedges of circles
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

::: {.exercise}

Let $X$ be a space that is the union of subspaces $S_1, \ldots, S_n$, each of which is homeomorphic to the unit circle.
Assume there is a point $p$ of $X$ such that $S_i \cap S_j = \ts{p}$ for $i \neq j$.

(a) Show that $X$ is Hausdorff if and only if each space $S_i$ is closed in $X$.

(b) Show that $X$ is Hausdorff if and only if the topology of $X$ is coherent with the subspaces $S_i$.

(c) Give an example to show that $X$ need not be Hausdorff.
[Hint: See [[E-29WP0]].]
:::

::: {.solution}
(a) Suppose first that \(X\) is Hausdorff. Each \(S_i\) is compact, being homeomorphic to \(S^1\), so each \(S_i\) is closed in \(X\).

Conversely, suppose each \(S_i\) is closed in \(X\). Then \(S_i\times S_i\) is closed in \(X\times X\), and since \(S_i\) is Hausdorff its diagonal \(\Delta_{S_i}\) is closed in \(S_i\times S_i\), hence in \(X\times X\). Because the cover is finite,
\[
\Delta_X=\bigcup_{i=1}^n\Delta_{S_i}
\]
is closed. Therefore \(X\) is Hausdorff.

(b) For a finite cover by closed subspaces, the topology is coherent with the cover: a set \(A\subset X\) is closed iff every \(A\cap S_i\) is closed in \(S_i\). Indeed, the forward implication is immediate, while in the reverse direction each \(A\cap S_i\) is closed in \(X\) and
\[
A=\bigcup_{i=1}^n(A\cap S_i)
\]
is a finite union of closed sets. Hence, if \(X\) is Hausdorff, part (a) shows all \(S_i\) are closed and the topology is coherent.

Conversely, assume the topology is coherent with the \(S_i\). Fix \(i\). For every \(j\),
\[
S_i\cap S_j=
\begin{cases}
S_i,&j=i,\\
\{p\},&j\ne i,
\end{cases}
\]
and these are closed in \(S_j\). Coherence therefore implies that \(S_i\) is closed in \(X\). Part (a) now gives that \(X\) is Hausdorff.

(c) Here is an explicit non-Hausdorff example. Start with two circles \(S_1,S_2\) meeting only at \(p\). Choose points \(q_i\in S_i-\{p\}\) and small open arcs \(A_i\subset S_i-\{p\}\) about \(q_i\), together with homeomorphisms
\[
\theta_i:A_i\longrightarrow(-1,1),\qquad \theta_i(q_i)=0.
\]
Away from \(q_1,q_2\), use the ordinary wedge topology. A basic neighborhood of \(q_1\) is, for \(0<\varepsilon<1\),
\[
\theta_1^{-1}((-\varepsilon,\varepsilon))
\;\cup\;
\theta_2^{-1}((-\varepsilon,0)\cup(0,\varepsilon)),
\]
and define basic neighborhoods of \(q_2\) symmetrically. This is exactly the line-with-two-origins construction localized in the two arcs. Its restriction to each \(S_i\) is the usual circle topology, and \(S_1\cap S_2=\{p\}\). But every neighborhood of \(q_1\) meets every neighborhood of \(q_2\), so the resulting \(X\) is not Hausdorff.
:::
