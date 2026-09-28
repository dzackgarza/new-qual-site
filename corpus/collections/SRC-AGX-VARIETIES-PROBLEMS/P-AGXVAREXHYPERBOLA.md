---
schema: qual/card@1
id: P-AGXVAREXHYPERBOLA
kind: problem
title: The hyperbola $V(xy-1)$ is not isomorphic to $\AA^1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Coordinate Rings
  - Isomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Exercise 4.2 in the recorded source. It asks only that
    A^1 and the hyperbola xy=1 are not isomorphic.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Removed the imported Hausdorff-connected-components clause, which is not
    in the source and is false over C: the hyperbola is isomorphic as a
    complex manifold to C^times. Removed Connectedness from the topics for
    the corrected problem.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked the coordinate-ring identification with C[x,x^{-1}] and the unit
    obstruction: C[t] has only constant units whereas the hyperbola has the
    nonconstant unit x.
---

::: {.problem}
Show that $\AA^1$ is not isomorphic to $X = V(xy-1)$.
:::

::: {.solution}
<1>1. The coordinate ring of the hyperbola is
$$
\boxed{
\CC[X]\cong\CC[x,x^{-1}].
}
$$

::: {.proof}
One has
$$
\CC[X]
=
\CC[x,y]/(xy-1).
$$
The homomorphism
$$
\CC[x,y]
\longrightarrow
\CC[x,x^{-1}],
\qquad
x\longmapsto x,
\qquad
y\longmapsto x^{-1}
$$
is surjective and has kernel $(xy-1)$. Hence it induces the displayed
isomorphism.
:::

<1>2. The only units in $\CC[t]$ are the nonzero constants:
$$
\CC[t]^\times=\CC^\times.
$$

::: {.proof}
If
$$
f(t)g(t)=1
$$
in $\CC[t]$, then
$$
\deg f+\deg g=0.
$$
Thus both degrees are zero, so both polynomials are nonzero constants.
Conversely every nonzero constant is a unit.
:::

<1>3. The coordinate ring $\CC[X]$ has a nonconstant unit.

::: {.proof}
Under step <1>1,
$$
x\in\CC[x,x^{-1}]
$$
is a unit with inverse $x^{-1}$. It is not constant.
:::

<1>4. There is no $\CC$-algebra isomorphism
$$
\CC[X]\xrightarrow{\sim}\CC[t].
$$

::: {.proof}
Suppose
$$
\varphi:\CC[X]\xrightarrow{\sim}\CC[t]
$$
were a $\CC$-algebra isomorphism. By step <1>3, $x$ is a unit, so
$$
\varphi(x)
$$
is a unit in $\CC[t]$. Step <1>2 gives
$$
\varphi(x)=c
$$
for some $c\in\CC^\times$.

Because $\varphi$ is a $\CC$-algebra map,
$$
\varphi(x-c)=0.
$$
But
$$
x-c\neq0
$$
in $\CC[x,x^{-1}]$, contradicting injectivity of $\varphi$. Therefore no such
isomorphism exists.
:::

<1>5. Hence
$$
\boxed{
\AA^1_\CC\not\cong V(xy-1).
}
$$

::: {.proof}
An isomorphism of affine varieties induces an isomorphism of their coordinate
rings. Step <1>4 shows that the coordinate rings
$$
\CC[t]
\qquad\text{and}\qquad
\CC[x,y]/(xy-1)
$$
are not isomorphic as $\CC$-algebras. Therefore the affine varieties are not
isomorphic.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
