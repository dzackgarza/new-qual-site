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

::: {.problem}
Define a complex torus and determine its group of holomorphic automorphisms.
:::

::: {.solution}
A complex torus is a quotient
$$
T=\CC/\Lambda,
$$
where
$$
\Lambda=\ZZ\omega_1\oplus\ZZ\omega_2
$$
is a lattice with $\omega_1,\omega_2$ linearly independent over $\RR$.

Every holomorphic automorphism of $T$ is induced by an affine map
$$
z\longmapsto az+b
$$
with
$$
a\Lambda=\Lambda.
$$
Consequently
$$
\boxed{
\operatorname{Aut}_{\mathrm{hol}}(T)
\cong T\rtimes U(\Lambda),
\qquad
U(\Lambda)=\{a\in\CC^*:a\Lambda=\Lambda\}.}
$$

To prove this, let $F:T\to T$ be a holomorphic automorphism and let
$$
\pi:\CC\to T
$$
be the universal covering. Since $\CC$ is simply connected, $F\circ\pi$ lifts to an entire map
$$
\widetilde F:\CC\to\CC.
$$
For every $\lambda\in\Lambda$, the difference
$$
\widetilde F(z+\lambda)-\widetilde F(z)
$$
takes values in the discrete set $\Lambda$ and depends continuously on $z$, hence is constant. Differentiating gives
$$
\widetilde F'(z+\lambda)=\widetilde F'(z).
$$
Thus $\widetilde F'$ is $\Lambda$-periodic and descends to a holomorphic function on the compact torus $T$. By the maximum modulus principle it is constant, so
$$
\widetilde F(z)=az+b.
$$
For this affine map to descend one needs $a\Lambda\subseteq\Lambda$; since $F$ is invertible, the inverse gives the reverse inclusion, hence
$$
a\Lambda=\Lambda.
$$
Conversely, every affine map with this property descends to a holomorphic automorphism of $T$.

The subgroup $U(\Lambda)$ is finite. Indeed, multiplication by $a$ scales Euclidean covolume by $\abs{a}^2$, while $a\Lambda=\Lambda$ preserves the covolume, so $\abs{a}=1$. Fix a nonzero $\lambda\in\Lambda$. Then
$$
a\lambda\in\Lambda
\qquad\text{and}\qquad
\abs{a\lambda}=\abs{\lambda}.
$$
A lattice has only finitely many points in a bounded set, so there are only finitely many possibilities for $a\lambda$, hence only finitely many possibilities for $a$.

For example, if $\Lambda=\ZZ+i\ZZ$, then multiplication by $\pm1,\pm i$ preserves $\Lambda$, giving the fourth roots of unity in $U(\Lambda)$. If $\Lambda=\ZZ+\ZZ e^{i\pi/3}$, then multiplication by the sixth roots of unity preserves $\Lambda$.
:::
