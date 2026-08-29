---
schema: qual/card@1
id: E-HAT-3.2-16
kind: exercise
title: "Torsion in products of CW complexes"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Show that if $X$ and $Y$ are finite CW complexes such that $H^*(X; \mathbb{Z})$ and $H^*(Y; \mathbb{Z})$ contain no elements of order a power of a given prime $p$, then the same is true for $X \times Y$.
[Apply Theorem 3.15 with coefficients in various fields.]

::: {.solution}
<1>1. For a finite CW complex $Z$, $H^*(Z;\ZZ)$ has no $p$-torsion iff $\dim_{\FF_p} H^n(Z;\FF_p) = \dim_{\QQ} H^n(Z;\QQ)$ for all $n$.
<2>1. By the universal coefficient theorem, $H^n(Z;\FF_p) \cong H^n(Z;\ZZ) \otimes \FF_p \oplus \operatorname{Tor}(H^{n+1}(Z;\ZZ), \FF_p)$.
Proof: UCT for cohomology.
<2>2. $\operatorname{Tor}(H^{n+1}(Z;\ZZ), \FF_p)$ is the $p$-torsion of $H^{n+1}(Z;\ZZ)$.
Proof: $\operatorname{Tor}(A, \FF_p) \cong \{a \in A : pa = 0\}$.
<2>3. $\dim_{\FF_p}(H^n(Z;\ZZ) \otimes \FF_p) = \operatorname{rank} H^n(Z;\ZZ) = \dim_{\QQ} H^n(Z;\QQ)$.
Proof: tensoring a finitely generated abelian group with $\FF_p$ kills the torsion and keeps the free part; the rank equals the rational Betti number.
<2>4. Hence $\dim_{\FF_p} H^n(Z;\FF_p) = \dim_{\QQ} H^n(Z;\QQ) + \dim_{\FF_p}(p\text{-torsion of } H^{n+1}(Z;\ZZ))$.
Proof: <2>1–<2>3.
<2>5. Therefore the equality $\dim_{\FF_p} H^n(Z;\FF_p) = \dim_{\QQ} H^n(Z;\QQ)$ for all $n$ holds iff $H^*(Z;\ZZ)$ has no $p$-torsion.
Proof: <2>4.

<1>2. By hypothesis, $\dim_{\FF_p} H^i(X;\FF_p) = \dim_{\QQ} H^i(X;\QQ)$ and $\dim_{\FF_p} H^j(Y;\FF_p) = \dim_{\QQ} H^j(Y;\QQ)$ for all $i, j$.
Proof: <1>1 applied to $X$ and $Y$.

<1>3. $\dim_{\FF_p} H^n(X \times Y;\FF_p) = \sum_{i+j=n} \dim_{\FF_p} H^i(X;\FF_p) \cdot \dim_{\FF_p} H^j(Y;\FF_p)$.
Proof: Künneth theorem (Theorem 3.15) with field coefficients $\FF_p$; the Tor term vanishes over a field.

<1>4. $\dim_{\QQ} H^n(X \times Y;\QQ) = \sum_{i+j=n} \dim_{\QQ} H^i(X;\QQ) \cdot \dim_{\QQ} H^j(Y;\QQ)$.
Proof: Künneth theorem with field coefficients $\QQ$.

<1>5. Hence $\dim_{\FF_p} H^n(X \times Y;\FF_p) = \dim_{\QQ} H^n(X \times Y;\QQ)$ for all $n$.
Proof: <1>3 and <1>4 have equal summands term-by-term by <1>2.

<1>6. Therefore $H^*(X \times Y;\ZZ)$ has no $p$-torsion.
Proof: <1>5 and <1>1 applied to $Z = X \times Y$.

<1>7. Q.E.D.
Proof: <1>6.
:::
