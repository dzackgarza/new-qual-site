---
schema: qual/card@1
id: T-BIRINV
kind: theorem
title: Plurigenera and irregularity are birational invariants
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
review: draft
prompts:
- What is the plurigenus of a smooth projective variety?
- What is the irregularity of a smooth projective variety?
- What is a variety of general type?
- Show that the geometric genus, plurigenera and irregularity are birational invariants.
---

::: {.definition}
Let $X$ be a smooth projective variety of dimension $n$ over an algebraically closed field.

- The \dfn{geometric genus} is $p_g(X) = h^0(X, \omega_X)$, and the \dfn{$m$-th plurigenus} is $P_m(X) = h^0(X, \omega_X^{\otimes m})$ for $m \geq 1$.

- The \dfn{irregularity} is $q(X)=h^1(X,\OO_X)$; for surfaces this is also $p_g(X)-p_a(X)$ [@Har10a, Remark III.7.12.3].
  The number of regular one-forms is $h^{1,0}(X)=h^0(X,\Omega^1_{X/k})$.
  In characteristic zero, Hodge symmetry gives $q(X)=h^{1,0}(X)$ [@Har10a, Appendix B].

- $X$ is of \dfn{general type} if $P_m(X)$ grows like a positive multiple of $m^n$, that is, $X$ has Kodaira dimension $n$.
:::

::: {.theorem}
Let $X$ and $X'$ be birational smooth projective varieties of dimension $n$ over the same algebraically closed field $k$.
For every $0\le p\le n$ and $m\ge1$, birational pullback gives an isomorphism
$$
H^0(X,(\Omega^p_{X/k})^{\otimes m})
\cong H^0(X',(\Omega^p_{X'/k})^{\otimes m}),
\qquad\Omega^p_{X/k}=\bigwedge^p\Omega_{X/k}.
$$
In particular $p_g$, every $P_m$, and every $h^{p,0}$ are birational invariants in any characteristic.
The inverse pullbacks are constructed in [[P-AGH288PLURIGENUS]], following the method of [@Har10a, Theorem II.8.19 and Exercise II.8.8].
:::

::: {.proposition title="Characteristic-zero Hodge comparison"}
For smooth projective varieties in characteristic zero, Hodge symmetry gives
$$
h^i(X,\OO_X)=h^0(X,\Omega^i_{X/k})
$$
[@Har10a, Appendix B].
For a general characteristic-zero ground field, descend the smooth projective variety to a subfield finitely generated over $\QQ$ and embed that subfield in $\CC$; the complex comparison gives the equality, and coherent cohomology commutes with both field extensions [@Har10a, Proposition III.9.3].
Consequently the preceding theorem also gives birational invariance of $q(X)=h^1(X,\OO_X)$, of $\chi(X,\OO_X)=\sum_i(-1)^i h^i(X,\OO_X)$, and of the arithmetic genus
$$
p_a(X)=(-1)^n\bigl(\chi(X,\OO_X)-1\bigr)
$$
[@Har10a, Chapter I, §7 and Exercise III.5.2].
The Euler characteristic and arithmetic genus are distinct quantities.
:::

::: {.remark}
For a smooth projective surface, blowing up a point gives $K_{\widetilde X}=\pi^*K_X+E$, by [[P-AGH285BLOWUPCANON]].
Since $E^2=-1$ and $(\pi^*K_X).E=0$, one obtains $K_{\widetilde X}^2=K_X^2-1$ [@Har10a, Chapter V, §3].
Thus the self-intersection of the canonical divisor is not a birational invariant.
:::
