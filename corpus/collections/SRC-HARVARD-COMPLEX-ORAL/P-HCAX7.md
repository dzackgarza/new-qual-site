---
schema: qual/card@1
id: P-HCAX7
kind: problem
title: Complex tori and their automorphisms
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Tori
relations: []
review: draft
---

::: problem
Define a complex torus and determine its group of holomorphic automorphisms.
:::

::: solution
A complex torus is a quotient
\[
T=\mathbb C/\Lambda,
\]
where
\[
\Lambda=\mathbb Z\omega_1\oplus\mathbb Z\omega_2
\]
is a lattice with $\omega_1,\omega_2$ linearly independent over $\mathbb R$.

Every holomorphic automorphism of $T$ is induced by an affine map
\[
z\longmapsto az+b
\]
with
\[
a\Lambda=\Lambda.
\]
Consequently
\[
\boxed{
\operatorname{Aut}_{\mathrm{hol}}(T)
\cong T\rtimes U(\Lambda),
\qquad
U(\Lambda)=\{a\in\mathbb C^*:a\Lambda=\Lambda\}.}
\]

To prove this, let $F:T\to T$ be a holomorphic automorphism and let
\[
\pi:\mathbb C\to T
\]
be the universal covering. Since $\mathbb C$ is simply connected, $F\circ\pi$ lifts to an entire map
\[
\widetilde F:\mathbb C\to\mathbb C.
\]
For every $\lambda\in\Lambda$, the difference
\[
\widetilde F(z+\lambda)-\widetilde F(z)
\]
takes values in the discrete set $\Lambda$ and depends continuously on $z$, hence is constant. Differentiating gives
\[
\widetilde F'(z+\lambda)=\widetilde F'(z).
\]
Thus $\widetilde F'$ is $\Lambda$-periodic and descends to a holomorphic function on the compact torus $T$. By the maximum modulus principle it is constant, so
\[
\widetilde F(z)=az+b.
\]
For this affine map to descend one needs $a\Lambda\subseteq\Lambda$; since $F$ is invertible, the inverse gives the reverse inclusion, hence
\[
a\Lambda=\Lambda.
\]
Conversely, every affine map with this property descends to a holomorphic automorphism of $T$.

The subgroup $U(\Lambda)$ is finite. Indeed, multiplication by $a$ scales Euclidean covolume by $|a|^2$, while $a\Lambda=\Lambda$ preserves the covolume, so $|a|=1$. Fix a nonzero $\lambda\in\Lambda$. Then
\[
a\lambda\in\Lambda
\qquad\text{and}\qquad
|a\lambda|=|\lambda|.
\]
A lattice has only finitely many points in a bounded set, so there are only finitely many possibilities for $a\lambda$, hence only finitely many possibilities for $a$.

For example, if $\Lambda=\mathbb Z+i\mathbb Z$, then multiplication by $\pm1,\pm i$ preserves $\Lambda$, giving the fourth roots of unity in $U(\Lambda)$. If $\Lambda=\mathbb Z+\mathbb Z e^{i\pi/3}$, then multiplication by the sixth roots of unity preserves $\Lambda$.
:::
