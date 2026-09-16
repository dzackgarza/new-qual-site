---
schema: qual/card@1
id: P-APASP07D
kind: problem
title: "Trace and computation of the averaged conjugate of a matrix over a finite group"
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let
$$
B = \begin{bmatrix}
2 & 3 & 1 \\
1 & 1 & 1 \\
27 & 0 & 3
\end{bmatrix},
$$
and let $V' = \mathbb{C}^3$ be an irreducible $G$-module for a finite group $G$, with $g \in G$ acting via the matrix $A_g$.
Let $$C = \frac{1}{|G|} \sum_{g} A_g B A_g^{-1}.$$

(a) Calculate $\operatorname{Tr}(C)$, where $\operatorname{Tr}$ is the usual trace.

(b) Calculate $C$.
:::

::: {.solution}
For every $h\in G$,
\[
A_h C A_h^{-1}
=
\frac1{|G|}\sum_{g\in G}A_hA_gBA_g^{-1}A_h^{-1}
=
\frac1{|G|}\sum_{g\in G}A_{hg}BA_{hg}^{-1}
=C,
\]
because left multiplication $g\mapsto hg$ permutes the elements of $G$. Hence $C$ commutes with every $A_h$. Since $\mathbb C^3$ is an irreducible complex $G$-module, Schur's lemma implies that
\[
C=\lambda I_3
\]
for some $\lambda\in\mathbb C$.

For part (a), trace is invariant under conjugation, so
\[
\operatorname{Tr}(C)
=
\frac1{|G|}\sum_{g\in G}\operatorname{Tr}(A_gBA_g^{-1})
=
\frac1{|G|}\sum_{g\in G}\operatorname{Tr}(B)
=
\operatorname{Tr}(B).
\]
Since
\[
\operatorname{Tr}(B)=2+1+3=6,
\]
we obtain
\[
\boxed{\operatorname{Tr}(C)=6}.
\]

For part (b), because $C=\lambda I_3$,
\[
3\lambda=\operatorname{Tr}(C)=6.
\]
Thus $\lambda=2$, and therefore
\[
\boxed{C=2I_3}.
\]
:::
