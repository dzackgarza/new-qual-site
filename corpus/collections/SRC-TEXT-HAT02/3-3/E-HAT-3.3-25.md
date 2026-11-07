---
schema: qual/card@1
id: E-HAT-3.3-25
kind: problem
title: Torsionfree $H_{k-1}$ implies torsionfree $H_k$
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 25; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 25; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: torsion-freeness of the finitely generated $H_{k-1}$ kills the Ext term, so
    $H^k\cong\operatorname{Hom}(H_k,\ZZ)$ is free, and Poincaré duality identifies it with $H_k$.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Published argument located at Guanyu Li, Hatcher.pdf, Exercise 3.3.9 (Hatcher 3.3 #25), printed
    p.59, with its symbol defect corrected: the universal coefficient sequence goes from
    Ext(H_{k-1}) to H^k to Hom(H_k), so the object after its vanishing Ext term is Hom(H_k(M),Z),
    not Ext(H_k(M),Z). Poincare duality then gives H_k(M), and Hom of a finitely generated group
    into Z is free (in particular torsionfree).

---

::: {.problem}
Show that if a closed orientable manifold $M$ of dimension $2k$ has $H_{k-1}(M; \ZZ)$ torsionfree, then $H_k(M; \ZZ)$ is also torsionfree.
:::

::: {.solution}
Since $M$ is a closed manifold, all its homology groups are finitely generated. Thus the hypothesis that $H_{k-1}(M;\ZZ)$ is torsionfree implies that it is free abelian, and therefore
$$
\operatorname{Ext}(H_{k-1}(M;\ZZ),\ZZ)=0.
$$
The universal coefficient theorem for cohomology gives
$$
0\to \operatorname{Ext}(H_{k-1}(M),\ZZ)
\to H^k(M;\ZZ)
\to \operatorname{Hom}(H_k(M),\ZZ)\to0,
$$
so
$$
H^k(M;\ZZ)\cong\operatorname{Hom}(H_k(M),\ZZ).
$$
The group on the right is free abelian.

Poincaré duality for the closed orientable $2k$-manifold $M$ gives
$$
H^k(M;\ZZ)\cong H_{2k-k}(M;\ZZ)=H_k(M;\ZZ).
$$
Hence $H_k(M;\ZZ)$ is free abelian, in particular torsionfree.

This is the argument in Guanyu Li, [`Hatcher.pdf`](https://guanyulee.github.io/Hatcher.pdf), Exercise 3.3.9 (Hatcher §3.3 #25), printed p. 59 (local file `tmp/sources/hatcher-solutions-guanyu-li.pdf`). The source writes $H^k(M;\ZZ)\cong\operatorname{Ext}(H_k(M),\ZZ)$ immediately after the universal coefficient sequence; that symbol must be $\operatorname{Hom}(H_k(M),\ZZ)$, as displayed here. After this typo is corrected, the remaining step is Poincare duality, and freeness of Hom follows because $H_k(M)$ is finitely generated (Corollaries A.8 and A.9 in Hatcher's Appendix).
:::
