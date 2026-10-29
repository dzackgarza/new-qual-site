---
schema: qual/card@1
id: T-CRVMG
kind: theorem
title: $\mathcal{M}_g$ is irreducible of dimension $3g-3$
slogan: 'For $g\ge2$, curve deformations are quadratic differentials: $\dim H^1(T_C)=h^0(\omega_C^{\tensor2})=3g-3$, the dimension of irreducible $\mathcal M_g$.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Moduli
  - Curves
  - Genus
relations:
- kind: uses
  target: D-CRVMOD
- kind: related-to
  target: D-CRVHYP
- kind: related-to
  target: FE-CRVLOWG
- kind: related-to
  target: T-CRVJINV
review: draft
prompts:
- What is the dimension of the moduli space of curves of genus $g$?
- Why is $\dim \mathcal{M}_2 = 3$?
- Why is $\dim \mathcal{M}_3 = 6$?
- What is $\mathcal{M}_1$, and why does the formula $3g-3$ not give it?
---

::: {.theorem title="Deligne--Mumford"}
Fix $g \geq 2$ and let $k$ be an algebraically closed field.
The coarse moduli space $\mathcal{M}_g$ of smooth projective curves of genus $g$ over $k$ is irreducible and quasiprojective of dimension $3g-3$.
:::

::: {.proposition title="Small genus"}
$\mathcal{M}_0$ is a point, $\mathcal{M}_1 \cong \AA^1$ by the $j$-invariant, $\dim \mathcal{M}_2 = 3$, and $\dim \mathcal{M}_3 = 6$.
:::

::: {.remark}
The dimension $3g-3$ is reflected infinitesimally: first-order deformations of $C$ are $H^1(C,T_C)$, and by Serre duality this is $\dualof{H^0(C,\omega_C^{\otimes 2})}$.
Since $\deg 2K = 4g-4 > 2g-2$ for $g \geq 2$, the divisor $2K$ is nonspecial and Riemann--Roch gives $h^0(\omega^{\otimes 2}) = (4g-4) + 1 - g = 3g-3$ outright.
This count uses $g \geq 2$, so $\mathcal{M}_1$ is stated separately: for $g = 1$ the formula $3g-3$ gives $0$, but $T_C \cong \OO_C$, so $h^1(T_C) = 1 = \dim \mathcal{M}_1$.

Two concrete dimension counts recover the formula.

**Genus $2$, via the hyperelliptic locus in characteristic different from $2$.** A hyperelliptic curve of genus $g$ is then a tame double cover of $\PP^1$ branched at $2g+2$ distinct points. The curve determines the branch divisor, so the moduli are the configurations of $2g+2$ unordered points of $\PP^1$ modulo $\PGL_2$.
Normalizing three of them to $0, 1, \infty$ uses the $3$-dimensional group and leaves $2g-1$ parameters. Hence the hyperelliptic locus is irreducible of dimension $2g-1$.
Every curve of genus $2$ is hyperelliptic, so $\dim \mathcal{M}_2=3$.
For $g\geq3$, the hyperelliptic locus has dimension $2g-1<3g-3$ and is a proper closed subvariety. The same dimension statement for the hyperelliptic locus remains true in characteristic $2$, but the simple branch-point description above does not apply there.

**Genus $3$, via plane quartics.** A non-hyperelliptic curve of genus $3$ is canonically embedded as a smooth plane quartic, and every smooth plane quartic arises this way.
Quartic forms in three variables have $\binom{4+2}{2} = 15$ coefficients, so they are parameterized by $\PP^{14}$, with the smooth ones an open $U$.
Two quartics give isomorphic curves exactly when they differ by $\PGL_3$, which has dimension $8$, and the stabilizers are finite because $\Aut C$ is finite for $g \geq 2$; so the orbits are $8$-dimensional and the image of $U$ in $\mathcal{M}_3$ has dimension $14 - 8 = 6 = 3g-3$.

The genus-$3$ curves left out of that count are exactly the hyperelliptic ones, and the count survives them: by the first computation they form a locus of dimension $2(3)-1 = 5$, strictly less than $6$.
So they lie in a proper closed subset, the plane quartics are a dense open subset of an irreducible $\mathcal{M}_3$, and the dimension computed on that open set is the dimension of the whole space.
The two counts use different coordinate-change groups: $\PGL_2$ acts on the branch points in the hyperelliptic count, while $\PGL_3$ acts on the ambient $\PP^2$ in the quartic count.
:::
