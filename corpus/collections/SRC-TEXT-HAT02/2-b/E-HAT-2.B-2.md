---
schema: qual/card@1
id: E-HAT-2.B-2
kind: problem
title: "Homology of complements of finite graphs in spheres"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the Alexander-duality and Mayer--Vietoris calculations and all degree shifts.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.B Exercise 2, printed page
    176, with the printed hint. Checked: a finite tree is contractible, so Alexander
    duality (Theorem 3.44, p. 253) makes the complement's reduced homology vanish; in
    general the homology of a connected graph is free with H_0 = Z and H_1 of rank r,
    so the universal coefficient theorem (Theorem 3.2, p. 195) has no Ext term and
    H̃^j(X) ≅ H̃_j(X), giving H̃_i(S^n − X) ≅ H̃_{n−i−1}(X) and H̃_{n−2} ≅ Z^r. No
    defect.
---
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Checked against DeMason, M382C Full Credit HW Problems (2021), Hatcher 2.B.2, pp.70-71: a
    tree is contractible, and induction on edges outside a maximal subtree keeps track of the
    complement and the rank of H_1. The card's Alexander-duality formulation is equivalent and
    applies to every embedded finite graph (compact and locally contractible). Its identification
    of the reduced cohomology with homology uses that H_*(graph) is free, so Ext(H_0(graph),Z)=0.

---

::: {.problem}
Show that $\tilde{H}_i(S^n - X) \approx \tilde{H}_{n-i-1}(X)$ when $X$ is homeomorphic to a finite connected graph.
[First do the case that the graph is a tree.]
:::

::: {.solution}
Let $X\subset S^n$ be homeomorphic to a finite connected graph. Since all homology groups of a finite graph are free abelian, the universal coefficient theorem identifies
$$
H^j(X;\ZZ)\cong \operatorname{Hom}(H_j(X;\ZZ),\ZZ)
$$
and hence, noncanonically but naturally in rank,
$$
\widetilde H^j(X;\ZZ)\cong \widetilde H_j(X;\ZZ).
$$

::: pf

::: pf-step

If $X$ is a tree, then
$$
\widetilde H_i(S^n-X)=0
\qquad\text{for all }i.
$$

::: pf-proof

A finite tree is contractible, so its reduced cohomology vanishes. Alexander duality gives
$$
\widetilde H_i(S^n-X)\cong \widetilde H^{\,n-i-1}(X)=0.
$$

:::

:::

::: pf-step

For an arbitrary finite connected graph,
$$
\boxed{\widetilde H_i(S^n-X)\cong \widetilde H_{\,n-i-1}(X).}
$$

::: pf-proof

Alexander duality gives
$$
\widetilde H_i(S^n-X)\cong \widetilde H^{\,n-i-1}(X).
$$
The homology of a connected graph is free: $H_0(X)=\ZZ$, $H_1(X)$ is a free abelian group, and $H_j(X)=0$ for $j>1$. Therefore the universal coefficient theorem has no $\operatorname{Ext}$ term, and $\widetilde H^{j}(X)$ is a free abelian group of the same rank as $\widetilde H_j(X)$. Choosing the basis of $H_1(X)$ obtained by collapsing a maximal tree identifies these groups, yielding the displayed isomorphism.

:::

:::

:::

In particular, if $r=\operatorname{rank}H_1(X)$, then the only possible nonzero reduced homology group of the complement is
$$
\widetilde H_{n-2}(S^n-X)\cong\ZZ^r.
$$The two inductions, first on leaves in a tree and then on edges outside a maximal tree, are in **Kenneth DeMason, *M382C Full Credit HW Problems* (2021)**, Hatcher 2.B.2, printed pp. 70--71. Collapsing a maximal subtree produces a wedge of $r$ circles, matching the groups computed here. The displayed statement also follows by Alexander duality, and the card records that it applies because every finite graph is compact and locally contractible (Theorem 3.45, p. 254); in cohomology the Ext term vanishes because homology of a graph is free, as shown above.


:::
