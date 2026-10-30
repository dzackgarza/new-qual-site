---
schema: qual/card@1
id: T-CRVUNIF
kind: theorem
title: Every elliptic curve over $\CC$ is a torus $\CC/\Lambda$
slogan: 'Every complex elliptic curve is $\CC/\Lambda$; on the torus, a divisor is principal exactly when its degree and group sum are both zero.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Elliptic Functions
  - Moduli
relations:
- kind: uses
  target: D-CRVWEIER
- kind: uses
  target: T-CRVMODJ
- kind: related-to
  target: PR-CRVGRP
- kind: related-to
  target: T-U5QSY
review: draft
prompts:
- How do you get from a lattice in $\CC$ to a plane cubic?
- Why is the analytic group law the same as the chord-and-tangent law?
- Every elliptic curve over $\CC$ is a torus --- what is the proof, and where does surjectivity come from?
- Which divisors on $\CC/\Lambda$ are principal?
---

::: {.theorem title="Uniformisation"}
Let $\Lambda \subseteq \CC$ be a lattice and put
$$
E_\Lambda\coloneqq V(y^2z=4x^3-g_2xz^2-g_3z^3)\subseteq\PP^2_\CC.
$$
Then $\Delta = g_2^3 - 27g_3^2 \neq 0$, so $E_\Lambda$ is a smooth cubic, and
$$
\phi \colon \CC/\Lambda \to E_\Lambda,
\qquad
z \mapsto \thevector{\wp(z) : \wp'(z) : 1}, \quad 0 \mapsto \thevector{0:1:0} ,
$$
is an isomorphism of Riemann surfaces which is also a group isomorphism onto $(E_\Lambda, p_0)$ with $p_0 = \phi(0)$.
Conversely every elliptic curve over $\CC$ is isomorphic to some $E_\Lambda$: given $c_2, c_3$ with $c_2^3 - 27c_3^2 \neq 0$ there is a lattice with $g_2 = c_2$ and $g_3 = c_3$.
:::

::: {.theorem title="Abel's theorem on the torus"}
A divisor $\sum n_i (a_i)$ on $\CC/\Lambda$ is the divisor of an elliptic function exactly when
$$
\sum n_i = 0
\qquad\text{and}\qquad
\sum n_i a_i = 0 \text{ in } \CC/\Lambda .
$$
:::

::: {.remark}
The [[D-CRVWEIER|differential equation of the Weierstrass $\wp$-function]] shows that $\phi$ lands in $E_\Lambda$.
The function $\wp$ has degree $2$ and is even, so $\wp(z)=\wp(z')$ implies $z'=\pm z$ in $\CC/\Lambda$; the odd function $\wp'$ distinguishes the two signs away from the branch points. The point at infinity is the image of $0\in\CC/\Lambda$. Hence $\phi$ is bijective and therefore an isomorphism of compact Riemann surfaces; GAGA identifies it with an algebraic isomorphism.

For the converse, [[T-CRVMODJ|the theory of the modular function $J$]] gives surjectivity of $J=g_2^3/\Delta$ on homothety classes of lattices. Scaling $\Lambda\mapsto\alpha\Lambda$ sends
$$
(g_2,g_3)\longmapsto(\alpha^{-4}g_2,\alpha^{-6}g_3),
$$
so after fixing the value of $J$, a homothety adjusts the scale to prescribed coefficients $c_2,c_3$ with $c_2^3-27c_3^2\ne0$.

The condition $\sum n_i = 0$ is degree zero; the condition $\sum n_i a_i = 0$ is the Abel--Jacobi map, which for genus $1$ is the identity $\CC/\Lambda \to \CC/\Lambda$.
Applying this to the divisor cut out by a line on the cubic shows that three points of $E_\Lambda$ are collinear exactly when their sum is $0$ in $\CC/\Lambda$, which is the chord-and-tangent group law.
The torsion subgroup is immediate from the lattice model: $E[n] = \tfrac{1}{n}\Lambda / \Lambda \cong (\ZZ/n)^2$, and topologically $E \cong (\RR/\ZZ)^2$.
:::

::: {.remark title="Normalisations"}
The model $y^2 = 4x^3 - g_2x - g_3$ is what $\wp$ produces; the Legendre model $y^2 = x(x-1)(x-\lambda)$ is what the branch-point normalisation produces.
Passing between them is a linear change of variable together with $x \mapsto \alpha^2 x$, $y \mapsto \alpha^3 y$, which is exactly the homothety $\Lambda \mapsto \alpha \Lambda$ seen on the curve.
The invariant $j$ is unchanged by these coordinate changes, while the numerical values of $g_2$ and $g_3$ depend on the chosen Weierstrass normalization.
:::
