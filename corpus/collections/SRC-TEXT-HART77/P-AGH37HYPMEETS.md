---
schema: qual/card@1
id: P-AGH37HYPMEETS
kind: problem
title: A positive-dimensional projective variety meets every hypersurface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Varieties
  - Hypersurfaces
  - Intersections
relations:
- kind: uses
  target: P-AGH35COMPLHYP
- kind: uses
  target: P-AGH28HYPERSURFACE
- kind: uses
  target: P-AGH31CONICS
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared both parts and the hint with Hartshorne I.3.7. Part (b) is proved by placing a disjoint projective variety inside the affine hypersurface complement, and part (a) reduces a plane curve to a hypersurface by I.2.8.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the affine/projective contradiction and the plane-curve reduction against published solutions and the already banked I.2.8 and I.3.1(e) cards.'
---

::: {.problem}
(a) Show that any two curves in $\PP^2$ have a nonempty intersection.

(b) More generally, show that if $Y \subseteq \PP^n$ is a projective variety of dimension $\geq 1$ and $H$ is a hypersurface, then $Y \intersect H \neq \emptyset$.
:::

::: {.hint}
Use (Ex. 3.5) and (Ex. 3.1e). See (7.2) for a generalization.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $Y\subseteq\PP^n$ is projective with $\dim Y\ge1$ and $H\subseteq\PP^n$ is a hypersurface, then $Y\cap H\ne\varnothing$.

::: pf-proof

Suppose instead that $Y\cap H=\varnothing$.
Then
$$
Y\subseteq\PP^n\setminus H.
$$
By [[P-AGH35COMPLHYP]], the hypersurface complement $\PP^n\setminus H$ is affine.
Since $Y$ is closed in $\PP^n$, it is also closed in the open subspace $\PP^n\setminus H$.
Therefore $Y$ is a closed subvariety of an affine variety and hence is affine.

But $Y$ is projective as well.
Part (e) of [[P-AGH31CONICS]] shows that a variety which is both affine and projective consists of a single point.
That would give $\dim Y=0$, contradicting $\dim Y\ge1$.
Thus $Y\cap H\ne\varnothing$, proving (b).

:::

:::

::: {.pf-step #s2}

Any two curves in $\PP^2$ have a nonempty intersection.

::: pf-proof

Let $C,D\subseteq\PP^2$ be curves.
Each has dimension one.
By [[P-AGH28HYPERSURFACE]], a projective variety of dimension $2-1=1$ in $\PP^2$ is a hypersurface.
Apply step [](#s1){.pf-ref} with $Y=C$ and $H=D$.
It gives
$$
C\cap D\ne\varnothing,
$$
which proves (a).

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves (b), and step [](#s2){.pf-ref} proves (a).

:::

:::

:::
