---
schema: qual/card@1
id: T-BIRINV
kind: theorem
title: Plurigenera and irregularity are birational invariants
slogan: 'Birational smooth projective varieties have the same global tensor powers of differential forms; plurigenera survive in every characteristic, and irregularity does in characteristic zero.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Birational Invariants
  - Plurigenera
  - Kodaira Dimension
relations:
- kind: uses
  target: D-G1AEH
- kind: uses
  target: D-COHEULER
- kind: related-to
  target: D-VARFANO
review: draft
prompts:
- What is the plurigenus of a smooth projective variety?
- What is the irregularity of a smooth projective variety?
- What is a variety of general type?
- Show that the geometric genus, plurigenera and irregularity are birational invariants.
---

::: {.theorem}
Let $X$ and $X'$ be birational smooth projective varieties of dimension $n$ over the same algebraically closed field $k$.
For every $0\le p\le n$ and $m\ge1$, birational pullback gives an isomorphism
$$
H^0(X,(\Omega^p_{X/k})^{\otimes m})
\cong H^0(X',(\Omega^p_{X'/k})^{\otimes m}),
\qquad\Omega^p_{X/k}=\bigwedge^p\Omega_{X/k}.
$$
In particular $p_g$, every $P_m$, and every $h^{p,0}$ are birational invariants in any characteristic.
The inverse pullbacks are constructed in [[P-AGH288PLURIGENUS]], following the method of [@Har77, Theorem II.8.19 and Exercise II.8.8].
:::

::: {.remark title="Plurigenera and Kodaira dimension"}
The invariants $p_g$, $q$, and $P_m$ are defined in [[D-COHEULER]]. Since every plurigenus is birationally invariant, the asymptotic growth of the sequence $P_m$ is birationally invariant. Hence Kodaira dimension and the property of being [[D-VARFANO|of general type]] are birational invariants for smooth projective varieties.
:::

::: {.proposition title="Characteristic-zero Hodge comparison"}
For smooth projective varieties in characteristic zero, Hodge symmetry gives
$$
h^i(X,\OO_X)=h^0(X,\Omega^i_{X/k})
$$
[@Har77, Appendix B]. For a general characteristic-zero ground field, descend the smooth projective variety to a subfield finitely generated over $\QQ$ and embed that subfield in $\CC$; the complex comparison gives the equality, and coherent cohomology commutes with both field extensions [@Har77, Proposition III.9.3]. Consequently the preceding theorem also gives birational invariance of $q(X)=h^1(X,\OO_X)$, of $\chi(X,\OO_X)=\sum_i(-1)^i h^i(X,\OO_X)$, and of the arithmetic genus
$$
p_a(X)=(-1)^n\bigl(\chi(X,\OO_X)-1\bigr)
$$
[@Har77, Chapter I, §7 and Exercise III.5.2].
:::

::: {.remark}
For a smooth projective surface, blowing up a point gives $K_{\widetilde X}=\pi^*K_X+E$, by [[P-AGH285BLOWUPCANON]]. Since $E^2=-1$ and $(\pi^*K_X).E=0$, one obtains $K_{\widetilde X}^2=K_X^2-1$ [@Har77, Chapter V, §3]. Thus the self-intersection of the canonical divisor is not a birational invariant.
:::
