---
schema: qual/card@1
id: T-CRVMG
kind: theorem
title: $\mathcal{M}_g$ is irreducible of dimension $3g-3$
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
Fix $g \geq 2$ and $k = \kbar$.
The coarse moduli space $\mathcal{M}_g$ of smooth projective curves of genus $g$ over $k$ is irreducible and quasiprojective of dimension $3g-3$.
:::

::: {.proposition title="Small genus"}
$\mathcal{M}_0$ is a point, $\mathcal{M}_1 \cong \AA^1$ by the $j$-invariant, $\dim \mathcal{M}_2 = 3$, and $\dim \mathcal{M}_3 = 6$.
:::

::: {.remark}
The number to have at hand is $3g-3$, and the infinitesimal statement behind it is the one to give when asked why: first-order deformations of $C$ are $H^1(C, T_C)$, and by Serre duality this is $H^0(C, \omega_C^{\otimes 2})\dual$.
Since $\deg 2K = 4g-4 > 2g-2$ for $g \geq 2$, the divisor $2K$ is nonspecial and Riemann--Roch gives $h^0(\omega^{\otimes 2}) = (4g-4) + 1 - g = 3g-3$ outright.
The hypothesis $g \geq 2$ is doing work in that line, which is why $\mathcal{M}_1$ has to be quoted separately: for $g = 1$ the same count returns $0$, while the actual dimension is $1$, because $T_C \cong \OO_C$ makes $h^1(T_C) = 1$ instead.

Two dimension counts confirm the formula and are the ones an examiner asks to see run.

**Genus $2$, via the hyperelliptic locus.** A hyperelliptic curve of genus $g$ is a double cover of $\PP^1$ branched at $2g+2$ points, and the curve determines that branch set, so the moduli are the configurations of $2g+2$ unordered points of $\PP^1$ modulo $\PGL_2$.
Normalizing three of them to $0, 1, \infty$ uses up the $3$-dimensional group and leaves $2g+2-3 = 2g-1$ parameters, so the hyperelliptic locus is irreducible of dimension $2g-1$.
Every curve of genus $2$ is hyperelliptic, so at $g=2$ that locus is all of $\mathcal{M}_2$ and $\dim \mathcal{M}_2 = 2(2)-1 = 3$, which agrees with $3g-3 = 3$.
This is also the last genus where the two numbers agree: $2g-1 < 3g-3$ exactly when $g > 2$, so for $g \geq 3$ the hyperelliptic curves are a proper closed subvariety and the general curve is not hyperelliptic.

**Genus $3$, via plane quartics.** A non-hyperelliptic curve of genus $3$ is canonically embedded as a smooth plane quartic, and every smooth plane quartic arises this way.
Quartic forms in three variables have $\binom{4+2}{2} = 15$ coefficients, so they are parameterized by $\PP^{14}$, with the smooth ones an open $U$.
Two quartics give isomorphic curves exactly when they differ by $\PGL_3$, which has dimension $8$, and the stabilizers are finite because $\Aut C$ is finite for $g \geq 2$; so the orbits are $8$-dimensional and the image of $U$ in $\mathcal{M}_3$ has dimension $14 - 8 = 6 = 3g-3$.

The genus-$3$ curves left out of that count are exactly the hyperelliptic ones, and the count survives them: by the first computation they form a locus of dimension $2(3)-1 = 5$, strictly less than $6$.
So they lie in a proper closed subset, the plane quartics are a dense open subset of an irreducible $\mathcal{M}_3$, and the dimension computed on that open set is the dimension of the whole space.
Note which group appears where: $\PGL_2$ acts on the branch points in the hyperelliptic count, $\PGL_3$ on the ambient $\PP^2$ in the quartic count, and using one for the other changes the answer by five.
:::
