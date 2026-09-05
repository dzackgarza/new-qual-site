---
schema: qual/card@1
id: P-4WCFE
kind: problem
title: $\RR$ and $\RR^2$ are not homeomorphic
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Connectedness
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked the statement against Section A, problem A5 of the January 18, 2002 topology qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Used the point-deletion invariant: R minus a point is disconnected, whereas
    R^2 minus a point is path-connected. The latter is proved by an explicit
    two-segment polygonal path avoiding the deleted point.
---

::: {.problem}
Show that $\mathbb{R}$ and $\mathbb{R}^2$ (with their usual topologies) are not homeomorphic.
:::

::: {.solution}
<1>1. For every $c\in\mathbb R$, the punctured line $\mathbb R\setminus\{c\}$ is disconnected.
::: {.proof}
It is the disjoint union
\[
\mathbb R\setminus\{c\}
=(-\infty,c)\sqcup(c,\infty).
\]
Both pieces are nonempty and open in the subspace $\mathbb R\setminus\{c\}$.
Hence they form a separation.
:::

<1>2. For every $a\in\mathbb R^2$, the punctured plane $\mathbb R^2\setminus\{a\}$ is path-connected.
::: {.proof}
Translation by $-a$ is a homeomorphism from $\mathbb R^2\setminus\{a\}$ to $\mathbb R^2\setminus\{0\}$, so it suffices to prove the latter is path-connected.

Take $x,y\in\mathbb R^2\setminus\{0\}$.
Choose a point
\[
z\in\mathbb R^2
\setminus
\bigl(\operatorname{span}(x)\cup\operatorname{span}(y)\bigr).
\]
Such a $z$ exists because one or two lines through the origin do not fill the plane.

The line segment from $x$ to $z$ does not contain the origin: if
\[
(1-t)x+tz=0
\]
for some $0<t<1$, then
\[
z=-\frac{1-t}{t}x\in\operatorname{span}(x),
\]
contrary to the choice of $z$.
The same argument shows that the line segment from $z$ to $y$ avoids the origin.
Concatenating these two line segments gives a path from $x$ to $y$ in $\mathbb R^2\setminus\{0\}$.
Thus the punctured plane is path-connected.
:::

<1>3. A homeomorphism $h:\mathbb R\to\mathbb R^2$ would induce a homeomorphism between a disconnected space and a connected space.
::: {.proof}
Assume such an $h$ exists, choose $c\in\mathbb R$, and put $a=h(c)$.
Restricting $h$ gives a bijection
\[
h|_{\mathbb R\setminus\{c\}}:
\mathbb R\setminus\{c\}
\longrightarrow
\mathbb R^2\setminus\{a\}.
\]
Its inverse is the corresponding restriction of $h^{-1}$, so this restriction is a homeomorphism.
But by <1>1 its domain is disconnected, while by <1>2 its codomain is path-connected and hence connected.
Connectedness is preserved by homeomorphisms, a contradiction.
:::

<1>4. Therefore $\mathbb R$ and $\mathbb R^2$ are not homeomorphic.
::: {.proof}
The assumed homeomorphism in <1>3 cannot exist.
:::
:::
