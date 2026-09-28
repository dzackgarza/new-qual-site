---
schema: qual/card@1
id: P-AGH312DIMLOCAL
kind: problem
title: The local ring at a point satisfies $\dim \mco_P = \dim X$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Local Rings
  - Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the statement and hint with Hartshorne I.3.12. The proof takes an affine open neighborhood of P, observes that the local ring is unchanged, and applies Theorem I.3.2(c); a nonempty open subset of an irreducible variety has the same dimension.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the affine-neighborhood reduction and dimension equalities against two independent published solutions.'
---

::: {.problem}
If $P$ is a point on a variety $X$, show that $\dim \mco_P = \dim X$.
:::

::: {.hint}
Reduce to the affine case and use (3.2c).
:::

::: {.solution}
Choose an affine open neighborhood $U\subseteq X$ of $P$.

<1>1. The local rings of $X$ and $U$ at $P$ are canonically isomorphic:
$$
\mco_{P,X}\cong\mco_{P,U}.
$$

::: {.proof}
A germ of a regular function at $P$ is represented by a regular function on some open neighborhood of $P$.
Intersecting that neighborhood with $U$ does not change the germ, and every open neighborhood of $P$ inside $U$ is also open in $X$ because $U$ is open.
Thus the two germ constructions have the same representatives and the same equivalence relation.
:::

<1>2. The affine open subset $U$ has the same dimension as $X$.

::: {.proof}
The variety $X$ is irreducible, and $U$ is a nonempty open subset.
The function fields are therefore the same:
$$
K(U)=K(X).
$$
For a variety over $k$, dimension equals the transcendence degree of its function field [@Har10a, Chapter I, §1].
Hence
$$
\dim U=\operatorname{trdeg}_k K(U)
=\operatorname{trdeg}_k K(X)=\dim X.
$$
:::

<1>3. The local ring at $P$ has dimension $\dim X$.

::: {.proof}
Since $U$ is affine, Hartshorne's Theorem I.3.2(c) gives
$$
\dim\mco_{P,U}=\dim U.
$$
Combining steps <1>1--<1>2 yields
$$
\dim\mco_{P,X}=\dim\mco_{P,U}=\dim U=\boxed{\dim X}.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required equality.
:::
:::
