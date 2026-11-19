---
schema: qual/card@1
id: P-PRACT20-W4-11
kind: problem
title: Possible dimensions of the intersection of two subspaces
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
  - Subspaces
  - Dimension
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. The two bounds are proved (intersection
    contained in each factor; dimension formula plus V + W contained in R^n), giving 0..2 for the
    4-space and 1..4 for the 7-space, and every intermediate value is exhibited by coordinate
    subspaces. Checked the (b) witnesses: W_k = span(e_1..e_k) + span(e_5..e_{8-k}) has
    k + (4 - k) = 4 vectors for k = 1, 2, 3, 4 and lies in R^7 because 8 - k <= 7, and its
    intersection with span(e_1..e_4) is span(e_1..e_k). Statement unchanged; the card says the
    argument is its own.
---

::: {.problem}
(a) If $V, W$ are $2$-dimensional subspaces of $\RR^{4}$, what are the possible dimensions of $V \cap W$?

(b) What if $V, W$ are $4$-dimensional subspaces of $\RR^{7}$?
:::

::: {.solution}
Both parts are the two bounds on the dimension of an intersection: $\dim V\cap W\le\min(\dim V,\dim W)$ because the intersection lies in both, and $\dim V\cap W\ge\dim V+\dim W-n$ by the dimension formula inside an ambient space of dimension $n$; then every intermediate value is realised by coordinate subspaces. The argument is this card's own: no retained solution set covers this problem.

::: pf

::: {.pf-step #upper}
For subspaces $V,W\le\RR^n$, $\dim(V\cap W)\le\min(\dim V,\dim W)$.

::: pf-proof
$V\cap W\subseteq V$ and $V\cap W\subseteq W$, and the dimension of a subspace is at most that of any space containing it, so $\dim(V\cap W)\le\dim V$ and $\dim(V\cap W)\le\dim W$.
:::

:::


::: {.pf-step #lower}
$\dim(V\cap W)\ge\dim V+\dim W-n$.

::: pf-proof
The dimension formula for subspaces, $\dim(V+W)=\dim V+\dim W-\dim(V\cap W)$, holds for finite-dimensional $V,W$; and $V+W\subseteq\RR^n$ gives $\dim(V+W)\le n$. Substituting, $\dim V+\dim W-\dim(V\cap W)\le n$, which is the display.
:::

:::


::: {.pf-step #parta}
(a) For $2$-dimensional $V,W\le\RR^4$ the possible values of $\dim(V\cap W)$ are $0,1,2$, and all occur.

::: pf-proof
With $n=4$ and $\dim V=\dim W=2$, step [](#upper){.pf-ref} gives $\dim(V\cap W)\le2$ and step [](#lower){.pf-ref} gives $\dim(V\cap W)\ge2+2-4=0$, so the value lies in $\{0,1,2\}$. All three occur: $\operatorname{span}(e_1,e_2)\cap\operatorname{span}(e_3,e_4)=\{0\}$; $\operatorname{span}(e_1,e_2)\cap\operatorname{span}(e_1,e_4)=\operatorname{span}(e_1)$; and $V\cap V=V$.
:::

:::


::: {.pf-step #partb}
(b) For $4$-dimensional $V,W\le\RR^7$ the possible values are $1,2,3,4$, and all occur.

::: pf-proof
With $n=7$ and both dimensions $4$, step [](#upper){.pf-ref} gives at most $4$ and step [](#lower){.pf-ref} gives at least $4+4-7=1$. For occurrence, let $V=\operatorname{span}(e_1,e_2,e_3,e_4)$ and, for $k=1,2,3,4$, let $W_k=\operatorname{span}(e_1,\dots,e_k)\oplus\operatorname{span}(e_5,\dots,e_{8-k})$, whose second summand has $8-k-4=4-k$ vectors among $e_5,\dots,e_7$, so $\dim W_k=k+(4-k)=4$ and $W_k\le\RR^7$ since $8-k\le7$ for $k\ge1$. Then $W_k\cap V=\operatorname{span}(e_1,\dots,e_k)$ has dimension $k$.
:::

:::


::: {.pf-step #conclusion}
Every value between the bounds occurs, in both cases, and no value outside them does.

::: pf-proof
Steps [](#parta){.pf-ref} and [](#partb){.pf-ref} give the ranges and the examples attaining each value in the range, using the two bounds of steps [](#upper){.pf-ref} and [](#lower){.pf-ref}.
:::

:::

:::
:::
