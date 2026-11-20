---
schema: qual/card@1
id: E-LIN4R
kind: problem
title: Linear continua in the dictionary order
classification:
  areas:
  - topology
  topics:
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §24 Exercise 5, printed p. 158; the four sets are
    stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 24.5, PDF pp. 4-5. Z+ x [0,1) and [0,1) x [0,1]
    are linear continua, with the least upper bound read off the first coordinate and then
    the fibre; [0,1) x Z+ fails density between 0 x 1 and 0 x 2, and [0,1] x [0,1) fails the
    least upper bound property on the fibre at 1. (tmp/sources/munkres-solutions-positron-
    ch3.pdf).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured and repaired. The card's earlier prose, transcribing positron0802's Chapter 3
    Exercise 24.5, had two defects in its justifications, corrected here against Munkres'
    definitions (§24, printed p. 153, with the exercise on printed p. 158): in (a) the density
    argument offered (x+1) x 0 as the intermediate element when z = x+1, which is not strictly
    between the two points when w = 0, and the correct intermediate x x t is used instead; and
    in (d) the card argued from the fibre {x} x [0,1), which is not bounded above at all when x
    = 1, so it could not witness the failure of the least upper bound property, and the witness
    is now the bounded-above set [0,1) x [0,1), whose upper bounds are exactly {1} x [0,1) and
    have no least element. The four answers are unchanged: (a) and (c) are linear continua, (b)
    and (d) are not. No certificate covers this card, so the correction is recorded as a rewrite
    of the solution rather than as a solution-corrected event.
---

::: {.exercise}

Consider the following sets in the dictionary order.
Which are linear continua?

(a) $\ZZ_+ \times [0, 1)$

(b) $[0, 1) \times \ZZ_+$

(c) $[0, 1) \times [0, 1]$

(d) $[0, 1] \times [0, 1)$
:::

::: {.solution}
A set with the dictionary order is a linear continuum when it has more than one element, has the least upper bound property, and has no consecutive elements: for $x < y$ there is $z$ with $x < z < y$ (Munkres, *Topology* (2000), §24; the exercise is §24 Exercise 5). Elements of a product are written $x \times y$, and $\ZZ_{+} = \theset{1,2,3,\ldots}$.

::: pf

::: {.pf-step #a-density}
(a) $\ZZ_{+} \times [0,1)$ has no consecutive elements.

::: pf-proof
Let $x \times y < z \times w$. If $x = z$ then $y < w$ in $[0,1)$, and $[0,1)$ is dense, so there is $t$ with $y < t < w$, giving $x \times y < x \times t < z \times w$. If $x < z$ then $x + 1 \le z$. When $x + 1 < z$ the element $(x+1)\times 0$ lies strictly between, because $x < x+1 < z$. When $x + 1 = z$ one has $y < 1$, so there is $t$ with $y < t < 1$; then $x \times y < x \times t$ because $y < t$, and $x \times t < (x+1) \times w = z \times w$ because $x < x+1$.

:::

:::

::: {.pf-step #a-lub}
(a) $\ZZ_{+} \times [0,1)$ has the least upper bound property.

::: pf-proof
Let $S$ be nonempty and bounded above by $m \times v$. Every element $x \times y$ of $S$ has $x \le m$, so the set of first coordinates of $S$ is a nonempty subset of the finite set $\theset{1,\ldots,m}$ and has a greatest element $x_{0}$; put $T \coloneqq \theset{y \in [0,1) \mid x_{0} \times y \in S}$, which is nonempty and bounded above by $1$, and let $y_{0} \coloneqq \sup T \in [0,1]$. If $y_{0} < 1$ then $x_{0} \times y_{0}$ is the least upper bound: it dominates every $x \times y \in S$ because $x < x_{0}$ gives $x \times y < x_{0} \times y_{0}$ and $x = x_{0}$ gives $y \le y_{0}$, and no $x' \times y' < x_{0} \times y_{0}$ is an upper bound, since $x' < x_{0}$ is dominated by any element of $S$ with first coordinate $x_{0}$ and $x' = x_{0}$ with $y' < y_{0}$ is dominated by $x_{0} \times y$ for some $y \in T$ with $y' < y \le y_{0}$. If $y_{0} = 1$ then the least upper bound is $(x_{0}+1) \times 0$: it dominates every element of $S$, since those with first coordinate $x_{0}$ have second coordinate $< 1$, and every $x' \times y' < (x_{0}+1)\times 0$ has $x' \le x_{0}$, so it is dominated by an element of $S$ with first coordinate $x_{0}$ when $x' < x_{0}$ and by $x_{0} \times y$ for some $y \in T$ with $y > y'$ when $x' = x_{0}$, the last because $\sup T = 1 \notin T$.

:::

:::

::: {.pf-step #a-verdict}
(a) $\ZZ_{+} \times [0,1)$ is a linear continuum.

::: pf-proof
It has more than one element, and steps [](#a-density){.pf-ref} and [](#a-lub){.pf-ref} supply the two defining properties.

:::

:::

::: {.pf-step #b}
(b) $[0,1) \times \ZZ_{+}$ is not a linear continuum.

::: pf-proof
The elements $0 \times 1$ and $0 \times 2$ satisfy $0 \times 1 < 0 \times 2$, and an element strictly between them would have first coordinate $0$ and second coordinate an integer strictly between $1$ and $2$, which does not exist. So the set has consecutive elements and is not a linear continuum.

:::

:::

::: {.pf-step #c-density}
(c) $[0,1) \times [0,1]$ has no consecutive elements.

::: pf-proof
Let $x \times y < z \times w$. If $x = z$ then $y < w$ and $[0,1]$ is dense, so there is $t$ with $y < t < w$. If $x < z$ then $y < 1$, and $x \times 1$ satisfies $x \times y < x \times 1 < z \times w$, the second inequality because $x < z$.

:::

:::

::: {.pf-step #c-lub}
(c) $[0,1) \times [0,1]$ has the least upper bound property.

::: pf-proof
Let $S$ be nonempty and bounded above, and let $x_{0} \coloneqq \sup\pi_{1}(S) \in [0,1]$, which exists because $[0,1]$ is complete. If $x_{0} \in \pi_{1}(S)$ let $y_{0} \coloneqq \sup\theset{y \mid x_{0} \times y \in S} \in [0,1]$; then $x_{0} \times y_{0}$ is the least upper bound, by the same two checks as in step [](#a-lub){.pf-ref}, the case distinction on the first coordinate being all that is used. If $x_{0} \notin \pi_{1}(S)$ then every element of $S$ has first coordinate $< x_{0}$, so $x_{0} \times 0$ is an upper bound; and for any $x' \times y' < x_{0} \times 0$ one has $x' < x_{0}$, so some element of $S$ has first coordinate $s$ with $x' < s$, and that element exceeds $x' \times y'$, which is therefore not an upper bound.

:::

:::

::: {.pf-step #c-verdict}
(c) $[0,1) \times [0,1]$ is a linear continuum.

::: pf-proof
It has more than one element, has no consecutive elements by step [](#c-density){.pf-ref}, and has the least upper bound property by step [](#c-lub){.pf-ref}.

:::

:::

::: {.pf-step #d}
(d) $[0,1] \times [0,1)$ is not a linear continuum: the subset $S \coloneqq [0,1) \times [0,1)$ is bounded above and has no least upper bound.

::: pf-proof
$S$ is nonempty and is bounded above by $1 \times 0$, since every element of $S$ has first coordinate $< 1$. An element $x' \times y'$ is an upper bound of $S$ exactly when $x' = 1$: if $x' < 1$ there is $s \in (x',1)$, and then $s \times 0 \in S$ exceeds $x' \times y'$. So the set of upper bounds of $S$ is $\theset{1} \times [0,1)$, which has no least element, because $1 \times (y'/2) < 1 \times y'$ is again an upper bound for every $y' \in [0,1)$. Hence $S$ has no least upper bound and $[0,1]\times[0,1)$ fails the least upper bound property.

:::

:::

::: pf-step
Among the four sets, $\boxed{(a)\ \ZZ_{+}\times[0,1) \text{ and } (c)\ [0,1)\times[0,1] \text{ are linear continua, while } (b) \text{ and } (d) \text{ are not}}$.

::: pf-proof
Steps [](#a-verdict){.pf-ref} and [](#c-verdict){.pf-ref} give the two affirmative answers, step [](#b){.pf-ref} the failure of consecutive elements in (b), and step [](#d){.pf-ref} the failure of the least upper bound property in (d).

:::

:::

:::
:::
