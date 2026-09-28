---
schema: qual/card@1
id: P-AGXGATHIRRCOMPS
kind: problem
title: Irreducible components of $V(x-yz,\, xz-y^2) \subset \AA^3/\CC$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducible Components
  - Coordinate Rings
  - Integral Domains
relations: []
review: draft
---

::: {.problem}
Find the irreducible components of
\[
X = V(x - yz, xz - y^2) \subset \AA^3/\CC
.\]
:::

::: {.solution}
Since $x=yz$ for all points of $X$,
\[
X &= V(x-yz, yz^2 - y^2) \\
&= V\qty{x-yz, y(z^2 - y) } \\
&= V(x-yz, y) \union V(x-yz, z^2-y) \\
&\da X_1 \union X_2
.\]

**Claim**: these two subvarieties are irreducible.

It suffices to show that the $A(X_i)$ are integral domains.
We have
\[
A(X_1) \da \CC[x,y,z] / \gens{x-yz, y} \cong \CC[y,z]/\gens{y} \cong \CC[z]
,\]
which is an integral domain since $\CC$ is a field and thus an integral domain, and
\[
A(X_2) \da \CC[x,y,z]/\gens{x-yz, z^2 - y} \cong \CC[y,z]/\gens{z^2-y} \cong \CC[y]
,\]
which is an integral domain for the same reason.
:::

::: {.remark}
Erratum: in the second isomorphism the relation $y=z^2$ eliminates $y$, so $A(X_2)\cong \CC[y,z]/\gens{z^2-y}\cong \CC[z]$, not $\CC[y]$; the conclusion that $A(X_2)$ is an integral domain is unaffected.
:::
