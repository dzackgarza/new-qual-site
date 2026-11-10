---
schema: qual/card@1
id: P-AGH45QUADSURFBIR
kind: problem
title: The quadric surface $xy = zw$ is birational but not isomorphic to $\PP^2$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Birational Geometry
  - Quadric Surfaces
  - Projective Varieties
relations:
- kind: uses
  target: P-AGH215QUADRIC
- kind: uses
  target: P-AGH37HYPMEETS
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the statement and its reference to I.2.15 with Hartshorne I.4.5. The quadric has a dense affine-plane chart, while I.2.15 supplies disjoint ruling lines; I.3.7 rules out their images under an isomorphism to P^2.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked both arguments against Hartshorne and modern lecture notes: the dense chart gives an explicit birational equivalence, and the nonisomorphism uses only incidence of closed irreducible curves.'
---

::: {.problem}
Show that the quadric surface $Q: xy = zw$ in $\PP^3$ is birational to $\PP^2$, but is not isomorphic to $\PP^2$ (cf. Ex. 2.15).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The open subset
$$
U=Q\cap D_+(w)
$$
is isomorphic to $\AA^2$.

::: pf-proof

On $D_+(w)$ normalize $w=1$.
The equation of $Q$ becomes
$$
z=xy.
$$
Hence every point of $U$ has a unique form
$$
[x:y:xy:1].
$$
The maps
$$
\AA^2\longrightarrow U,
\qquad
(a,b)\longmapsto[a:b:ab:1],
$$
and
$$
U\longrightarrow\AA^2,
\qquad
[x:y:z:w]\longmapsto\left(\frac{x}{w},\frac{y}{w}\right)
$$
are morphisms and are inverse to one another.
Thus $U\cong\AA^2$.

:::

:::

::: {.pf-step #s2}

The surface $Q$ is birational to $\PP^2$.

::: pf-proof

The quadric $Q$ is irreducible by [[P-AGH215QUADRIC]], so its nonempty open subset $U$ is dense.
The standard open subset
$$
V=D_+(X_2)\subseteq\PP^2
$$
is likewise dense and isomorphic to $\AA^2$ via
$$
[X_0:X_1:X_2]\longmapsto
\left(\frac{X_0}{X_2},\frac{X_1}{X_2}\right).
$$
Composing the two affine-chart isomorphisms gives an isomorphism
$$
U\xrightarrow{\sim}V.
$$
An isomorphism between dense open subsets is a birational equivalence, so
$$
Q\dashrightarrow\PP^2
$$
is birational.

:::

:::

::: {.pf-step #s3}

The surface $Q$ contains two disjoint projective lines.

::: pf-proof

By [[P-AGH215QUADRIC]], one ruling consists of the pairwise disjoint lines
$$
L_{[a:b]}
=
\{[ac:bd:ad:bc]:[c:d]\in\PP^1\}.
$$
In particular,
$$
L_{[1:0]}\cap L_{[0:1]}=\varnothing.
$$
Each is a closed irreducible curve on $Q$.

:::

:::

::: {.pf-step #s4}

The surface $Q$ is not isomorphic to $\PP^2$.

::: pf-proof

Suppose an isomorphism
$$
\alpha:Q\xrightarrow{\sim}\PP^2
$$
existed.
An isomorphism preserves closedness, irreducibility, intersections, and dimension.
Therefore
$$
\alpha(L_{[1:0]})
\quad\text{and}\quad
\alpha(L_{[0:1]})
$$
would be two disjoint curves in $\PP^2$.
But [[P-AGH37HYPMEETS]] proves that any two curves in $\PP^2$ have nonempty intersection.
This contradiction shows that no such isomorphism exists.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves birationality, and step [](#s4){.pf-ref} proves nonisomorphism.

:::

:::

:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 4.5, PDF p. 6: the open subset $w\ne0$ of $Q$ is isomorphic to $\AA^2$ by $(w:x:y:z)\mapsto(x/w,y/w)$ with inverse $(x,y)\mapsto(1:x:y:xy)$, so $Q$ is birational to $\AA^2$ and hence to $\PP^2$; and $Q\cong\PP^1\times\PP^1$ contains two disjoint one-dimensional closed subvarieties, which $\PP^2$ does not.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), gives no solution to 4.5.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.4.5, PDF p. 40: "see V.4.1 to see birational, and compute the canonicals to see they are not isomorphic", a forward reference to Chapter V rather than an argument within Chapter I.
The proof above follows Borcherds: the affine chart $w\ne0$ for birationality and, for nonisomorphism, the two disjoint ruling lines with Exercise I.3.7; Egbert's route needs the canonical class of Chapter V.
Agree with Borcherds.
:::
