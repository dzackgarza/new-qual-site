---
schema: qual/card@1
id: E-CCLL5
kind: problem
title: Normal subgroups and regular coverings
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
---

::: {.exercise}

Let $p: E \to B$ be a covering map; let $p(e_0) = b_0$.
Show that $H_0 = p_*(\pi_1(E, e_0))$ is a normal subgroup of $\pi_1(B, b_0)$ if and only if for every pair of points $e_1, e_2$ of $p^{-1}(b_0)$, there is an equivalence $h: E \to E$ with $h(e_1) = e_2$.
:::

::: {.solution}
Assume \(E\) is connected and locally path connected, as in the covering-space classification theorem. Fix \(e_0\in p^{-1}(b_0)\) and put
\[
H_0=p_*\pi_1(E,e_0)\le G:=\pi_1(B,b_0).
\]
For any \(e\in p^{-1}(b_0)\), choose a path \(\lambda\) in \(E\) from \(e_0\) to \(e\), and let
\[
g=[p\lambda]\in G.
\]
Changing basepoint along \(\lambda\) gives
\[
p_*\pi_1(E,e)=g^{-1}H_0g
\]
(up to the consistent convention for concatenation; only conjugacy matters below).

Suppose first that \(H_0\triangleleft G\). Then for every \(e\in p^{-1}(b_0)\),
\[
p_*\pi_1(E,e)=H_0.
\]
Given \(e_1,e_2\in p^{-1}(b_0)\), the two pointed coverings \((E,e_1)	o(B,b_0)\) and \((E,e_2)	o(B,b_0)\) therefore have the same associated subgroup. By the equivalence theorem for pointed connected coverings, there is a covering equivalence
\[
h:E\to E,\qquad p\circ h=p,\qquad h(e_1)=e_2.
\]

Conversely, suppose that for every pair \(e_1,e_2\) in the fiber there is such an equivalence. For any \(g\in G\), lift a representative loop at \(b_0\) beginning at \(e_0\), and let its endpoint be \(e_g\). The basepoint-change formula gives
\[
p_*\pi_1(E,e_g)=g^{-1}H_0g.
\]
By hypothesis there is an equivalence \(h:E	o E\) with \(h(e_0)=e_g\). Since \(p h=p\),
\[
p_*\pi_1(E,e_g)
=p_*h_*\pi_1(E,e_0)
=p_*\pi_1(E,e_0)=H_0.
\]
Thus \(g^{-1}H_0g=H_0\) for every \(g\in G\). Hence \(H_0\) is normal.
:::
