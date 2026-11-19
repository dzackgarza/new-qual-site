---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-01
kind: problem
title: Uniqueness of lifts into a covering space
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: the equaliser $A$ is nonempty because
    $f(y_0)=g(y_0)$; at a point of $A$ the two values lie in the same sheet, on which $p$ is
    injective, so $f=g$ near the point; at a point outside $A$ the values lie in distinct sheets over
    an evenly covered neighbourhood, which are disjoint, so $f\ne g$ near the point. A nonempty
    clopen subset of a connected space is everything. Added: the shrinking of the neighbourhood to
    one on which $f$ and $g$ stay in the sheets of $f(y)$ and $g(y)$, which the prose performed in
    one clause, and the disjointness of distinct sheets as the reason the inequality persists. No
    defect found in the statement (Wisconsin January 1998). The collection's provenance is the
    worksheet, so no retained solution set covers the item.
---

::: {.problem}
(Wisconsin Jan ’98) Let $p:\widetilde X\to X$ be a cover.
Suppose that $f,g:Y\to\widetilde X$ are maps such that $p\circ f$ and $p\circ g$ are equal and assume that $f$ and $g$ agree at $y_0\in Y$.
Show that if $Y$ is connected, then $f=g$.
:::

::: {.solution}
No retained solution set covers this item, the collection's provenance being the worksheet, so the argument is the card's own; it is the standard clopen-set argument for uniqueness of lifts.

::: pf

::: {.pf-step #equal-set}
Put $h=p\circ f=p\circ g$ and $A=\{y\in Y:f(y)=g(y)\}$. Then $A$ contains $y_0$, so it is not empty.

::: pf-proof
By hypothesis $f(y_0)=g(y_0)$; and $h$ is well defined because the two composites agree.
:::

:::

::: {.pf-step #open}
$A$ is open.

::: pf-proof
Let $y\in A$ and set $\tilde x=f(y)=g(y)$. Choose an evenly covered neighbourhood $U$ of $h(y)$, so that $p^{-1}(U)=\bigsqcup_\lambda V_\lambda$ with each $p\restriction_{V_\lambda}$ a homeomorphism onto $U$. The sheets are open, so by continuity of $f$ and $g$ there is a neighbourhood $W$ of $y$ with $f(W)$ inside the sheet containing $f(y)$ and $g(W)$ inside the sheet containing $g(y)$, and with $h(W)\subseteq U$. Since $f(y)=g(y)$, these are the same sheet $V$; on $V$ the map $p$ is injective, and $p\circ f=p\circ g$ on $W$ gives $f(w)=g(w)$ for $w\in W$. Hence $W\subseteq A$ and $A$ is open.
:::

:::

::: {.pf-step #closed}
$Y\setminus A$ is open.

::: pf-proof
Let $y\in Y\setminus A$, so $f(y)\ne g(y)$. Choose $U$ evenly covered as above and a neighbourhood $W$ of $y$ with $h(W)\subseteq U$, $f(W)$ in the sheet $V_1$ containing $f(y)$ and $g(W)$ in the sheet $V_2$ containing $g(y)$. Since $f(y)\ne g(y)$ and the sheets are the fibres of $p$ over $U$, $V_1\ne V_2$ are disjoint; hence $f(w)\ne g(w)$ for every $w\in W$, that is $W\subseteq Y\setminus A$, which is therefore open.
:::

:::

::: {.pf-step}
$f=g$.

::: pf-proof
Steps [](#open){.pf-ref} and [](#closed){.pf-ref} make $A$ a clopen subset of $Y$, and step [](#equal-set){.pf-ref} makes it nonempty. A connected space has no nonempty proper clopen subset, so $A=Y$, that is $f(y)=g(y)$ for every $y\in Y$.
:::

:::

:::
:::
