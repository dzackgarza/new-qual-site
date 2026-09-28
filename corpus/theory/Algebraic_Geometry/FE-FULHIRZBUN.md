---
schema: qual/card@1
id: FE-FULHIRZBUN
kind: example
title: The Hirzebruch surface as a projective bundle over the line
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Surfaces
  - Vector Bundles
relations:
- kind: uses
  target: FE-TORHIRZ
- kind: uses
  target: PR-TORMOR
review: draft
prompts:
- Identify the Hirzebruch surface as the projectivisation of a rank two bundle on P^1.
- What is the normal bundle of the negative section of F_a?
---

::: {.example title="The ruling is a toric morphism"}
With the fan of $\FF_a$ given by $u_1 = (1,0)$, $u_2 = (0,1)$, $u_3 = (-1,a)$, $u_4 = (0,-1)$, the lattice map
\[
\phi : N = \ZZ^2 \to \ZZ, \qquad (p,q) \mapsto p
\]
sends $u_1 \mapsto 1$, $u_3 \mapsto -1$, and $u_2, u_4 \mapsto 0$, so each cone of $\FF_a$ lands in a cone of the fan $\ts{\RR_{\geq 0}, \ts{0}, \RR_{\leq 0}}$ of $\PP^1$.
The induced toric morphism $\pi : \FF_a \to \PP^1$ is the ruling, with invariant fibres $D_1$ and $D_3$ and disjoint invariant sections $D_2$ and $D_4$.
:::

::: {.example title="The four charts"}
Let $\sigma_1 = \Cone(u_1, u_2)$, $\sigma_2 = \Cone(u_4, u_1)$, $\sigma_3 = \Cone(u_3, u_4)$ and $\sigma_4 = \Cone(u_2, u_3)$.
Then
\[
U_{\sigma_1} = \Spec \CC[x, y], \quad
U_{\sigma_2} = \Spec \CC[x, y^{-1}], \quad
U_{\sigma_3} = \Spec \CC[x^{-1}, x^{-a}y^{-1}], \quad
U_{\sigma_4} = \Spec \CC[x^{-1}, x^{a}y] ,
\]
which patch as follows:

\begin{tikzcd}
	{U_{\sigma_4}} & {(x^{-1}, x^a y)} & {(x, y)} & {U_{\sigma_1}} \\
	{U_{\sigma_3}} & {(x^{-1}, x^{-a} y^{-1})} & {(x, y^{-1})} & {U_{\sigma_2}}
	\arrow[leftrightarrow, from=1-2, to=1-3]
	\arrow[leftrightarrow, from=1-2, to=2-2]
	\arrow[leftrightarrow, from=1-3, to=2-3]
	\arrow[leftrightarrow, from=2-2, to=2-3]
\end{tikzcd}

Setting $y = 0$ gives the patching $x \mapsto x^{-1}$ of a copy of $\PP^1$, and patching in the fibre direction, for example $U_{\sigma_1}$ with $U_{\sigma_2}$, gives a copy of $\CC \times \PP^1$; so $\FF_a$ is a $\PP^1$-bundle over $\PP^1$.
:::

::: {.example title="The bundle"}
\[
\FF_a \cong \PP\big( \OO_{\PP^1} \oplus \OO_{\PP^1}(a) \big) .
\]
The two disjoint sections are the ones cut out by the two summands, and they have
\[
D_2^2 = -a, \qquad D_4^2 = +a ,
\]
so $D_2$ is the **negative section**. Its normal bundle is
\[
N_{D_2 / \FF_a} \cong \OO_{D_2}(D_2) \cong \OO_{\PP^1}(-a) ,
\]
because the normal bundle of a divisor in a surface is its own restriction, of degree $D_2^2 = -a$ on $D_2 \cong \PP^1$.
Likewise $N_{D_4/\FF_a} \cong \OO_{\PP^1}(a)$.
:::

::: {.remark title="Conventions, and what is invariant"}
Twisting changes the bundle and not the surface: $\PP(E) \cong \PP(E \tensor L)$ for any line bundle $L$, so
\[
\PP\big( \OO \oplus \OO(a) \big) \cong \PP\big( \OO(-a) \oplus \OO \big) ,
\]
and both notations name $\FF_a$.
What does not depend on the convention is the pair of self-intersections $\ts{-a, +a}$ and the difference $a$ between them.

For $a \geq 1$ the negative section is the unique irreducible curve on $\FF_a$ with negative self-intersection, which is why $\FF_a \cong \FF_b$ forces $a = b$: the integer $a$ is recovered from the surface.
For $a = 0$ there is no negative curve and $\FF_0 = \PP^1 \times \PP^1$ has two rulings instead of one.
Contracting the negative section of $\FF_a$ gives the cone over the rational normal curve of degree $a$, which is how the affine singular cone and the surface classification are the same picture seen twice.
:::
