---
schema: qual/card@1
id: E-S57IX
kind: problem
title: Products of quotient maps with locally compact Hausdorff factors
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
  - Compactness
relations: []
review: draft
---

::: {.exercise}

(a) Lemma.
If $p: X \to Y$ is a quotient map and if $Z$ is a locally compact Hausdorff space, then the map

$$
\pi = p \times i_Z: X \times Z \to Y \times Z
$$

is a quotient map.

[Hint: If $\pi^{-1}(A)$ is open and contains $x \times y$, choose open sets $U_1$ and $V$ with $\overline{V}$ compact, such that $x \times y \in U_1 \times V$ and $U_1 \times \overline{V} \subset \pi^{-1}(A)$. Given $U_i \times \overline{V} \subset \pi^{-1}(A)$, use the tube lemma to choose an open set $U_{i+1}$ containing $p^{-1}(p(U_i))$ such that $U_{i+1} \times \overline{V} \subset \pi^{-1}(A)$. Let $U = \bigcup U_i$; show that $U \times V$ is a saturated neighborhood of $x \times y$ that is contained in $\pi^{-1}(A)$.]

An entirely different proof of this result will be outlined in the exercises of §46.

(b) Theorem.
Let $p: A \to B$ and $q: C \to D$ be quotient maps.
If $B$ and $C$ are locally compact Hausdorff spaces, then $p \times q: A \times C \to B \times D$ is a quotient map.
:::

::: {.solution}
(a) Let \(\pi=p\times i_Z\), and suppose \(A\subset Y\times Z\) is such that \(\pi^{-1}(A)\) is open. Fix \((y,z)\in A\) and choose \(x\in p^{-1}(y)\). By local compactness and the preceding exercise, choose an open neighborhood \(V\) of \(z\) with compact closure \(\overline V\). Since \(\pi^{-1}(A)\) is open and contains \((x,z)\), shrink to an open \(U_1\ni x\) such that
\[
U_1\times\overline V\subset\pi^{-1}(A).
\]

Inductively, assume \(U_i\times\overline V\subset\pi^{-1}(A)\). For each \(x'\in p^{-1}(p(U_i))\), the compact slice \(\{x'\}\times\overline V\) lies in the open set \(\pi^{-1}(A)\). By the tube lemma there is an open neighborhood \(W_{x'}\) of \(x'\) with
\[
W_{x'}\times\overline V\subset\pi^{-1}(A).
\]
Let \(U_{i+1}=\bigcup_{x'}W_{x'}\). Then \(U_{i+1}\) is open, contains \(p^{-1}(p(U_i))\), and still satisfies the product inclusion.

Set \(U=\bigcup_iU_i\). Then \(U\) is open and saturated: if \(u\in U_i\), the whole fiber \(p^{-1}(p(u))\subset U_{i+1}\subset U\). Hence \(p(U)\) is open in \(Y\), because \(p\) is quotient and \(U=p^{-1}(p(U))\). Also
\[
p(U)\times V\subset A.
\]
Thus every point of \(A\) has an open neighborhood contained in \(A\), so \(A\) is open. Therefore \(\pi\) is quotient.

(b) Factor
\[
p\times q=(i_B\times q)\circ(p\times i_C).
\]
Since \(C\) is locally compact Hausdorff, part (a) shows \(p\times i_C:A\times C\to B\times C\) is quotient. Since \(B\) is locally compact Hausdorff, applying part (a) to \(q:C\to D\) gives \(i_B\times q:B\times C\to B\times D\) quotient. A composition of quotient maps is quotient, so \(p\times q\) is quotient.
:::
