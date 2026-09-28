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
Show that $\RR$ and $\RR^2$ (with their usual topologies) are not homeomorphic.
:::

::: {.solution}
<1>1. For every $c\in\RR$, the punctured line $\RR\setminus\{c\}$ is disconnected.

::: {.proof}
It is the disjoint union $\RR\setminus\{c\}=(-\infty,c)\sqcup(c,\infty)$.
Both pieces are nonempty and open in the subspace $\RR\setminus\{c\}$.
Hence they form a separation.
:::

<1>2. For every $a\in\RR^2$, the punctured plane $\RR^2\setminus\{a\}$ is path-connected.

::: {.proof}
Translation by $-a$ is a homeomorphism from $\RR^2\setminus\{a\}$ to $\RR^2\setminus\{0\}$, so it suffices to prove the latter is path-connected.

Take $x,y\in\RR^2\setminus\{0\}$.
Choose a point $z\in\RR^2\setminus\bigl(\operatorname{span}(x)\cup\operatorname{span}(y)\bigr)$.
Such a $z$ exists because the union of two lines through the origin is not all of $\RR^2$.

The line segment from $x$ to $z$ does not contain the origin: if $(1-t)x+tz=0$ for some $0<t<1$, then $z=-\frac{1-t}{t}x\in\operatorname{span}(x)$, contrary to the choice of $z$.
The same argument shows that the line segment from $z$ to $y$ avoids the origin.
Concatenating these two line segments gives a path from $x$ to $y$ in $\RR^2\setminus\{0\}$.
:::

<1>3. There is no homeomorphism $h\colon\RR\to\RR^2$.

::: {.proof}
Assume such an $h$ exists, choose $c\in\RR$, and put $a=h(c)$.
The restriction $h|_{\RR\setminus\{c\}}\colon\RR\setminus\{c\}\to\RR^2\setminus\{a\}$ is a bijection whose inverse is the corresponding restriction of $h^{-1}$, so it is a homeomorphism.
By step <1>1 its domain is disconnected, while by step <1>2 its codomain is path-connected and hence connected.
A homeomorphic image of a disconnected space is disconnected, a contradiction.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 shows that $\RR$ and $\RR^2$ are not homeomorphic.
:::
:::
