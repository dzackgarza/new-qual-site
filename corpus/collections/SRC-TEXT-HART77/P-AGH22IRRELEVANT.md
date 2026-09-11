---
schema: qual/card@1
id: P-AGH22IRRELEVANT
kind: problem
title: The irrelevant ideal and the empty projective vanishing locus
classification:
  areas:
  - algebraic-geometry
  topics:
  - Homogeneous Ideals
  - Projective Varieties
  - Radical Ideals
relations: []
review: draft
---

::: problem
Let $S \da k[x_0,\ldots,x_n]$ and let $\mfa \subseteq S$ be a homogeneous ideal.
Show that the following conditions are equivalent.

1. $Z(\mfa) = \emptyset$.
2. $\sqrt{\mfa}$ is either $S$ or the irrelevant ideal $S_+ = \bigoplus_{d>0} S_d$.
3. $\mfa \supseteq S_d$ for some $d > 0$.
:::

::: solution
Write $J$ for the ideal $\mfa$, write $V_p(J) \subseteq \PP^n$ for the projective vanishing locus, and write $V_a(J) = C(V_p(J)) \subseteq \AA^{n+1}$ for the corresponding affine locus in the cone.

**$(1) \iff (2)$.**
The cone over a projective set is
\[
C(V_p(J)) = \ts{\vector{0}} \union \ts{ (x_0,\ldots,x_n) \st \tv{x_0 : \cdots : x_n} \in V_p(J) } .
\]
So if $V_p(J) = \emptyset$, then $V_a(J)$ is either empty or the single point $\vector{0} \in \AA^{n+1}$.
Taking ideals gives $\sqrt{J} = I(V_a(J))$, which is $I(\emptyset) = S$ in the first case and $I(\vector{0}) = S_+$ in the second: every element of $S$ vanishes on the empty set, and an element vanishes at the origin exactly when each of its monomials is divisible by some variable, i.e. when it lies in $S_+$.
Each step reverses, which gives the converse.

**$(2) \implies (3)$.**
If $\sqrt{J} = S$ then $1 \in \sqrt{J}$, so $1 \in J$ and $J = S$, which contains every graded piece $S_d$.

If instead $\sqrt{J} = S_+$, then each variable $x_i$ lies in $\sqrt{J}$, so there are integers $N_i$ with $x_i^{N_i} \in J$.
Put $d = \lcm(N_0,\ldots,N_n)$, so that $x_0^d,\ldots,x_n^d \in J$.
Every monomial of degree $(n+1)d$ is divisible by some $x_i^d$, so $J$ contains a graded piece $S_D$ for $D = (n+1)d$.

**$(3) \implies (1)$.**
Suppose $S_d \subseteq J$ for some $d > 0$.
Then the monomials $x_0^d, \ldots, x_n^d$ all lie in $J$, and they have no common zero in $\PP^n$, since a point of $\PP^n$ has some nonzero coordinate.
Hence $V_p(J) = \emptyset$.
:::
