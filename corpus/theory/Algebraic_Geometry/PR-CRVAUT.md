---
schema: qual/card@1
id: PR-CRVAUT
kind: proposition
title: Automorphisms of a curve of genus $g \geq 2$
slogan: 'Curves of genus at least $2$ have finite automorphism groups; in characteristic zero, Hurwitz bounds their order by $84(g-1)$.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Automorphisms
  - Curves
  - Moduli
relations:
- kind: uses
  target: D-CRVHYP
- kind: related-to
  target: D-CRVMOD
- kind: related-to
  target: T-CRVMG
review: draft
prompts:
- Is the automorphism group of a curve of genus $g \geq 2$ finite, and why?
- State the sharp bound on $\size{\Aut_k(C)}$ and the curve that attains it.
- For a non-hyperelliptic genus-$3$ curve, how is its automorphism group realized projectively?
- Does the general curve of genus $g \geq 3$ have a nontrivial automorphism?
- What is Hurwitz's theorem?
---

::: {.proposition}
Let $C$ be a smooth projective curve of genus $g \geq 2$ over an algebraically closed field $k$.
Then $\Aut_k(C)$ is finite. If $\operatorname{char}k=0$, then
$$
\size{\Aut_k(C)} \leq 84(g-1).
$$
If $C$ is non-hyperelliptic, every automorphism of $C$ is induced by a linear automorphism of the ambient $\PP^{g-1}$ of the canonical embedding; for $g = 3$ this says $\Aut_k(C)$ is the subgroup of $\PGL_3(k)$ preserving the plane quartic.
In characteristic zero, a general curve of genus $g \geq 3$ has trivial automorphism group.
:::

::: {.remark}
The line bundle $3K_C$ is very ample for $g\geq2$, so the automorphism group scheme of $C$ is a closed subgroup scheme of the projective linear group preserving the $3K_C$-embedding. Its tangent space at the identity is $H^0(C,T_C)$. Since $T_C\cong\omega_C\dual$ has degree $2-2g<0$, one has $H^0(C,T_C)=0$. Thus the automorphism group scheme is zero-dimensional, affine, and of finite type over $k$, hence finite over $k$.

If $C$ is non-hyperelliptic, the canonical system already gives an embedding $C\hookrightarrow\PP(H^0(C,\omega_C)\dual)$. For $g=3$, the image is a smooth plane quartic, and $\Aut_k(C)$ is the subgroup of $\PGL_3(k)$ stabilizing that quartic.

Assume now that $\operatorname{char}k=0$. The bound follows from Riemann--Hurwitz applied to the quotient $C \to C/G$ with $G = \Aut_k(C)$ of order $n$.
Writing $g'$ for the genus of the quotient and $e_1,\ldots,e_r$ for the ramification indices of the branch points,
$$
2g-2 = n\left( 2g'-2 + \sum_{i=1}^r \left(1 - \frac{1}{e_i}\right) \right) ,
$$
so $n$ is largest when the bracket is smallest, and the smallest positive value the bracket can take is $\frac{1}{42}$, attained at $g' = 0$ with three branch points of orders $(2,3,7)$.
That gives $n \leq 42(2g-2) = 84(g-1)$.
The bound is sharp: the Klein quartic $x^3 y + y^3 z + z^3 x = 0$ has $g = 3$ and $\Aut_k(C)\cong\PSL_2(\FF_7)$ of order $168 = 84 \cdot 2$.
In positive characteristic, wild ramification changes the Riemann--Hurwitz contribution and the bound $84(g-1)$ does not hold uniformly.

Every hyperelliptic curve carries its hyperelliptic involution. In particular, curves with nontrivial automorphisms exist in every genus $g\geq2$, while the general curve has trivial automorphism group for $g\geq3$ in characteristic zero.
:::
