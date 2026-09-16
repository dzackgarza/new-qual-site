---
schema: qual/card@1
id: P-AGXGATHRADICAL
kind: problem
title: Radical of $\gens{x_1^3 - x_2^6,\, x_1x_2 - x_2^3}$ in $\CC[x_1,x_2]$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Radical Ideals
  - Nullstellensatz
  - Vanishing Loci
relations: []
review: draft
---

::: problem
Determine $\sqrt{I}$ for
\[
I\da \gens{x_1^3 - x_2^6,\, x_1 x_2 - x_2^3} \normal \CC[x_1, x_2]
.\]
:::

::: solution
Let $\mci, V$ denote the maps in Hilbert's Nullstellensatz, so that
\[
(\mci \circ V)(I) = \sqrt{I}
.\]

Consider $V(I) \subseteq \AA^2/\CC$, the vanishing locus of these two polynomials, which yields the system
\[
\begin{cases} x^3 - y^6 & = 0 \\ xy - y^3 & = 0. \end{cases}
\]
In the second equation $(x- y^2)y = 0$, and since $\CC[x, y]$ is an integral domain, one term must be zero.

1. If $y=0$, then $x^3 = 0 \implies x= 0$, so the origin is contained in this vanishing locus.

2. Otherwise $x-y^2 = 0$, so $x=y^2$, with no further conditions coming from the first equation.

Combining these conditions,
\[
P\da \ts{(t^2, t) \st t\in \CC} \subset V(I)
.\]
In fact $P = V(I)$, and so taking the ideal of $P$ yields
\[
\qty{\mci \circ V} (I) = \mci(P) = \gens{y-x^2} \normal \CC[x ,y]
,\]
and thus $\sqrt{I} = \gens{y-x^2}$.
:::

::: {.remark}
Erratum: the source's conclusion swaps the variables.
With $x=x_1$ and $y=x_2$, the locus $P=\ts{(t^2,t)}$ is the zero locus of $x-y^2$, so $\mci(P)=\gens{x-y^2}$ and $\sqrt{I}=\gens{x_1-x_2^2}$; the ideal $\gens{y-x^2}$ vanishes on the different parabola $\ts{(t,t^2)}$.
:::
