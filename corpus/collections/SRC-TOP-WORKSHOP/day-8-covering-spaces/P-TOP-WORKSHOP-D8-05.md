---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-05
kind: problem
title: A pathwise continuity criterion for a lift into a cover
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. The two hypotheses are now separated
    and each shown to be used: p o g continuous puts h^{-1}(U) open around y_0 and makes s o h
    available, while g o gamma continuous makes g o gamma a path to which uniqueness of lifting
    applies; local path-connectedness supplies a path-connected W inside h^{-1}(U). The agreement
    step lists both lifts and their common initial value, and the conclusion notes that continuity
    is local, so g is continuous everywhere. The card's argument was already correct; what the
    steps add is where each hypothesis enters. Statement unchanged; the card says the argument is
    its own.
---

::: {.problem}
(Purdue Aug ’09) Let $p:E\to B$ be a covering map.
Let $Y$ be locally path-connected.
Let $g:Y\to E$ be a function such that

- $p\circ g$ is continuous;

- $g\circ\gamma$ is continuous for every path $\gamma$ in $Y$.

Prove that $g$ is continuous.
:::

::: {.solution}
Write $h=p\circ g$, which is continuous. Near a point $y_0$ pick an evenly covered neighbourhood $U$ of $h(y_0)$ and the sheet $V_0\ni g(y_0)$, with inverse $s$ of $p$ on $V_0$. On a path-connected neighbourhood $W\subseteq h^{-1}(U)$ of $y_0$, the path $g\circ\gamma$ and the path $s\circ h\circ\gamma$ are two lifts of $h\circ\gamma$ starting at the same point, so they coincide; hence $g=s\circ h$ on $W$, which is continuous. The two hypotheses are used exactly here: $p\circ g$ continuous to make $s\circ h$ defined and continuous, and $g\circ\gamma$ continuous to make $g\circ\gamma$ a legitimate lift. The argument is this card's own: no retained solution set covers this workshop problem.

::: pf

::: {.pf-step #setup}
Let $h=p\circ g$, which is continuous. Fix $y_0\in Y$ and choose an evenly covered neighbourhood $U$ of $h(y_0)$; let $V_0$ be the sheet over $U$ containing $g(y_0)$, and $s\colon U\to V_0$ the inverse of $p\restrictionof{V_0}$.

::: pf-proof
By hypothesis $h=p\circ g$ is continuous, so $h(y_0)$ is a point of $B$; a covering map has an evenly covered neighbourhood at each point of the base, so there is an open $U\ni h(y_0)$ whose preimage is a disjoint union of sheets, each mapped homeomorphically onto $U$. The point $g(y_0)$ lies in $p^{-1}(U)$, hence in exactly one sheet, $V_0$; on $V_0$ the restriction of $p$ is a homeomorphism onto $U$, and $s$ denotes its inverse, which is continuous.
:::

:::


::: {.pf-step #neighbourhood}
There is a path-connected open neighbourhood $W$ of $y_0$ with $W\subseteq h^{-1}(U)$.

::: pf-proof
$h^{-1}(U)$ is open and contains $y_0$, since $h$ is continuous and $h(y_0)\in U$. A locally path-connected space has a base of path-connected open sets, so there is a path-connected open $W$ with $y_0\in W\subseteq h^{-1}(U)$.
:::

:::


::: {.pf-step #agree}
For $y\in W$ and any path $\gamma\colon[0,1]\to W$ from $y_0$ to $y$, the paths $g\circ\gamma$ and $s\circ h\circ\gamma$ coincide, so $g(y)=s(h(y))$.

::: pf-proof
Both are continuous maps $[0,1]\to E$: $g\circ\gamma$ by hypothesis, and $s\circ h\circ\gamma$ as a composite of continuous maps. Both are lifts of $h\circ\gamma$, because $p\circ(g\circ\gamma)=(p\circ g)\circ\gamma=h\circ\gamma$ and $p\circ s\circ h\circ\gamma=h\circ\gamma$ (as $p\circ s=\mathrm{id}_U$ and $h\circ\gamma$ takes values in $U$). They agree at $0$: $(g\circ\gamma)(0)=g(y_0)=s(h(y_0))$, the last equality because $s$ is the inverse of $p$ on the sheet containing $g(y_0)$ and $h(y_0)=p(g(y_0))$. By uniqueness of lifts of a path in a covering space, the two coincide on $[0,1]$, and evaluating at $1$ gives $g(y)=s(h(y))$.
:::

:::


::: {.pf-step #continuity}
$g\restrictionof{W}=s\circ h\restrictionof{W}$, which is continuous; hence $g$ is continuous at $y_0$, and since $y_0$ was arbitrary, on $Y$.

::: pf-proof
Step [](#agree){.pf-ref} gives the identity on $W$: for every $y\in W$ there is a path in $W$ from $y_0$ to $y$ because $W$ is path-connected. The composite $s\circ h$ is continuous on $h^{-1}(U)\supseteq W$, so $g$ agrees on the open neighbourhood $W$ of $y_0$ with a continuous function, which is continuity of $g$ at $y_0$. Continuity is a local property, so $g$ is continuous.
:::

:::


::: {.pf-step #conclusion}
$g$ is continuous.

::: pf-proof
Steps [](#setup){.pf-ref} to [](#continuity){.pf-ref} prove it at an arbitrary point. Note where each hypothesis enters: $p\circ g$ continuous makes $s\circ h$ available, and $g\circ\gamma$ continuous makes $g\circ\gamma$ a path to which uniqueness of lifting applies; local path-connectedness of $Y$ supplies $W$.
:::

:::

:::
:::
