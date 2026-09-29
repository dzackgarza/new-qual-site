---
schema: qual/card@1
id: P-Y3PUL
kind: problem
title: $\RP^2\vee S^1$ is not homotopy equivalent to a compact surface
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Surfaces
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Replaced the unsupported general torsion argument with a direct classification and Klein-bottle group proof.
---

::: {.problem}
Show that $\RP^2 \lor S^1$ is *not* homotopy equivalent to a compact surface (possibly with boundary).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For
\[
X=\RP^2\vee S^1,
\]
one has
\[
\chi(X)=0,
\qquad
H_1(X;\ZZ)\cong\ZZ/2\ZZ\oplus\ZZ,
\qquad
H_2(X;\ZZ)=0.
\]

::: pf-proof

The wedge has the CW structure obtained by adjoining to the standard CW structure on $\RP^2$ one additional $1$-cell at the common basepoint.
Thus it has one $0$-cell, two $1$-cells, and one $2$-cell, so
\[
\chi(X)=1-2+1=0.
\]

Reduced homology takes wedges of connected CW complexes to direct sums, hence
\[
\widetilde H_i(X;\ZZ)
\cong
\widetilde H_i(\RP^2;\ZZ)
\oplus
\widetilde H_i(S^1;\ZZ).
\]
Using
\[
H_1(\RP^2;\ZZ)\cong\ZZ/2\ZZ,
\qquad
H_1(S^1;\ZZ)\cong\ZZ,
\]
and $H_2(\RP^2;\ZZ)=H_2(S^1;\ZZ)=0$ gives the stated groups.

:::

:::

::: {.pf-step #s2}

If a compact connected surface $S$ were homotopy equivalent to $X$, then $S$ would be one of
\[
T^2,
\qquad
S^1\times[0,1],
\qquad
K,
\qquad
M,
\]
where $K$ is the Klein bottle and $M$ is the Möbius band.

::: pf-proof

Euler characteristic is a homotopy invariant for finite CW complexes, so step [](#s1){.pf-ref} would give
\[
\chi(S)=0.
\]
By the classification of compact connected surfaces,
\[
\chi(\Sigma_{g,b})=2-2g-b
\]
for an orientable surface and
\[
\chi(N_{k,b})=2-k-b
\]
for a nonorientable surface.
The nonnegative integer solutions of these equations with Euler characteristic zero are
\[
(g,b)=(1,0),(0,2)
\]
and
\[
(k,b)=(2,0),(1,1),
\]
respectively.
These are exactly the torus, annulus, Klein bottle, and Möbius band.

:::

:::

::: {.pf-step #s3}

The torus, annulus, and Möbius band are not homotopy equivalent to $X$.

::: pf-proof

The torus has
\[
H_2(T^2;\ZZ)\cong\ZZ,
\]
whereas step [](#s1){.pf-ref} gives $H_2(X;\ZZ)=0$.
Thus $T^2\not\simeq X$.

Both the annulus and the Möbius band deformation retract onto a circle, so each has
\[
H_1(-;\ZZ)\cong\ZZ.
\]
This differs from
\[
H_1(X;\ZZ)\cong\ZZ/2\ZZ\oplus\ZZ.
\]
Hence neither is homotopy equivalent to $X$.

:::

:::

::: {.pf-step #s4}

The fundamental group
\[
\pi_1(X)
\cong
\ZZ/2\ZZ * \ZZ
\]
contains a nontrivial element of order $2$.

::: pf-proof

By Seifert--van Kampen for a wedge,
\[
\pi_1(X)
\cong
\pi_1(\RP^2)*\pi_1(S^1)
\cong
\ZZ/2\ZZ * \ZZ.
\]
The canonical map from either free factor into a free product is injective.
Therefore the nonidentity element of the factor $\ZZ/2\ZZ$ remains an element of order $2$ in $\pi_1(X)$.

:::

:::

::: {.pf-step #s5}

The Klein-bottle group is torsion-free.

::: pf-proof

Use the standard presentation
\[
\pi_1(K)
\cong
G=\left\langle a,b\ \middle|\ aba^{-1}=b^{-1}\right\rangle.
\]
The relation gives
\[
ab=b^{-1}a,
\]
so every element of $G$ can be written in the form
\[
b^m a^n
\qquad(m,n\in\ZZ).
\]
Moreover $G$ is the semidirect product
\[
\ZZ\rtimes_{-1}\ZZ,
\]
with multiplication
\[
(m,n)(m',n')
=
\bigl(m+(-1)^n m',\,n+n'\bigr),
\]
under the correspondence $(m,n)\leftrightarrow b^m a^n$.
Thus this normal form is unique.

Suppose $g=b^m a^n$ has finite order $r>0$.
Projection onto the second coordinate defines a homomorphism
\[
G\to\ZZ,
\qquad
b^m a^n\longmapsto n.
\]
From $g^r=1$ we obtain
\[
r n=0,
\]
so $n=0$.
Hence $g=b^m$.
But $\langle b\rangle\cong\ZZ$, so $b^m$ has finite order only when $m=0$.
Therefore $g=1$, proving that $G$ is torsion-free.

:::

:::

::: {.pf-step #s6}

The Klein bottle is not homotopy equivalent to $X$.

::: pf-proof

A homotopy equivalence induces an isomorphism on fundamental groups.
By step [](#s4){.pf-ref}, $\pi_1(X)$ contains a nontrivial element of order $2$, while by step [](#s5){.pf-ref}, $\pi_1(K)$ is torsion-free.
Thus
\[
\pi_1(X)\not\cong\pi_1(K),
\]
so $X\not\simeq K$.

:::

:::

::: pf-step

Therefore $\RP^2\vee S^1$ is not homotopy equivalent to any compact surface, with or without boundary.

::: pf-proof

By step [](#s2){.pf-ref}, a compact connected surface homotopy equivalent to $X$ would have to be one of four surfaces.
Steps [](#s3){.pf-ref} and [](#s6){.pf-ref} exclude all four.

:::

:::

:::

:::
