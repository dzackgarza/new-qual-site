---
schema: qual/card@1
id: PR-CRVAUT
kind: proposition
title: Automorphisms of a curve of genus $g \geq 2$
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
- State the sharp bound on $\size \Aut C$ and the curve that attains it.
- Where do the automorphisms of a genus-$3$ curve come from?
- Does the general curve of genus $g \geq 3$ have a nontrivial automorphism?
---

::: {.proposition}
Let $C$ be a smooth projective curve of genus $g \geq 2$ over $k = \kbar$.
Then $\Aut C$ is finite, and in characteristic zero
\[
\size \Aut C \leq 84(g-1) .
\]
If $C$ is non-hyperelliptic, every automorphism of $C$ is induced by a linear automorphism of the ambient $\PP^{g-1}$ of the canonical embedding; for $g = 3$ this says $\Aut C$ is the subgroup of $\PGL_3$ preserving the plane quartic.
The general curve of genus $g \geq 3$ has $\Aut C = 1$.
:::

::: {.remark}
Finiteness has a one-line reason and an argument, and both are worth carrying.
The reason: $T_C \cong \omega_C\dual$ has degree $2-2g < 0$, so $h^0(T_C) = 0$ and there are no infinitesimal automorphisms; $\Aut C$ is an algebraic group of dimension $0$.
The argument that makes it a *finite* group rather than merely $0$-dimensional runs through the canonical embedding: $\omega_C$ is intrinsic, so any automorphism carries $\abs{K}$ to itself and acts on $\PP^{g-1} = \PP(H^0(\omega_C)\dual)$.
For non-hyperelliptic $C$ the canonical map is an embedding, so $\Aut C$ is exactly the closed subgroup of $\PGL_g$ stabilizing the canonical curve, hence an algebraic group of dimension $0$ in a variety, hence finite.
For hyperelliptic $C$ run the same argument with $\abs{3K}$, which is very ample.
The genus-$3$ statement is this with $g-1 = 2$: automorphisms are restrictions of automorphisms of $\PP^2$, so a plane quartic has no automorphisms beyond the linear ones visible in its equation.

The bound comes from Riemann--Hurwitz applied to the quotient $C \to C/G$ with $G = \Aut C$ of order $n$.
Writing $g'$ for the genus of the quotient and $e_1,\ldots,e_r$ for the ramification indices of the branch points,
\[
2g-2 = n\left( 2g'-2 + \sum_{i=1}^r \left(1 - \frac{1}{e_i}\right) \right) ,
\]
so $n$ is largest when the bracket is smallest, and the smallest positive value the bracket can take is $\frac{1}{42}$, attained at $g' = 0$ with three branch points of orders $(2,3,7)$.
That gives $n \leq 42(2g-2) = 84(g-1)$.
The bound is sharp: the Klein quartic $x^3 y + y^3 z + z^3 x = 0$ has $g = 3$ and $\Aut = \PSL_2(\FF_7)$ of order $168 = 84 \cdot 2$, and it is a plane quartic, so its automorphisms are linear as the previous paragraph requires.
The characteristic hypothesis is not decorative: the count of $1 - 1/e_i$ is the tame formula, and in characteristic $p$ wild ramification breaks the bound.

The two ends of this card are what the moduli statements need.
Finiteness of $\Aut C$ is why the $\PGL_3$ orbits in the plane-quartic count are $8$-dimensional, which is what makes $\dim \mathcal{M}_3 = 14-8$ come out right.
Nontriviality of $\Aut C$ for *some* curve is the obstruction to a fine moduli space, and no genus escapes it: the general curve of genus $g \geq 3$ has no automorphisms, but every hyperelliptic curve carries its involution and the hyperelliptic locus is nonempty in every genus.
At $g = 2$ there is no general case to appeal to at all, since every genus-$2$ curve is hyperelliptic.
:::
