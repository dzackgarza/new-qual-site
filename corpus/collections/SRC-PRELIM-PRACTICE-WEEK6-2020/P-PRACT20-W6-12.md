---
schema: qual/card@1
id: P-PRACT20-W6-12
kind: problem
title: The discrete metric on $\RR$
classification:
  areas:
  - prelim
  topics:
  - Metric Spaces
  - Discrete Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the arrow lost from choice (D) and separated the choices, checked against Week6_solns.pdf (Problem 12).
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the arrow lost from the identity map in the solution, checked against Week6_solns.pdf (Problem 12).
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    No source document is retained for this card. The collection
    SRC-PRELIM-PRACTICE-WEEK6-2020 has an empty provenance list, and the only
    retained pages of the practice sheet are the three page images
    assets/attachments/prelim-practice-week6-2020/page-4.png, page-5.png and
    page-11.png, none of which carries this problem; so there is no printed page
    to compare the statement with. What was checked is the statement as it stands
    on the card: the four assertions were each checked against the discrete metric, whose balls of radius 1/2 are singletons
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. The openness of singletons, the consequence that every subset is open and closed, the continuity of every map out of a discrete space, and the failure of continuity into it via the singleton 0
---

::: {.problem}
Let $d(x, y) = \begin{cases} 0, & x = y, \\ 1, & x \neq y. \end{cases}$ Which of the following hold in the metric space $(\RR, d)$?

(A) $\{x\}$ is open for each $x \in \RR$.

(B) Every subset of $\RR$ is closed.

(C) If $d'$ is the ordinary metric on $\RR$, then the identity map $(\RR, d) \to (\RR, d')$ is continuous.

(D) If $d'$ is the ordinary metric on $\RR$, then the identity map $(\RR, d') \to (\RR, d)$ is continuous.
:::

::: {.solution}

Let $d(x,y)=0$ for $x=y$ and $d(x,y)=1$ for $x\ne y$, and let
$d'(x,y)=\abs{x-y}$ be the ordinary metric.

::: pf

::: {.pf-step #opensets}

(A) holds: $\{x\}$ is open for every $x$; and (B) holds: every subset is
closed.

::: pf-proof

In $(X,d)$ the ball of radius $\frac12$ about $x$ is $\{x\}$ itself, since
$d(x,y)<\frac12$ forces $y=x$; so each singleton is open. An arbitrary union
of singletons is a union of open sets, hence open, so every subset is open;
taking complements, every subset is also closed, which is (B).

:::

:::

::: {.pf-step #identity}

(C) holds and (D) fails.

::: pf-proof

(C): a map out of $(X,d)$ is continuous as soon as every subset of the source
is open, which holds by step [](#opensets){.pf-ref}; so the identity to
$(\RR,d')$ is continuous. (D): the identity from $(\RR,d')$ to $(\RR,d)$ would
need the preimage of every $d$-open set to be $d'$-open, and the $d$-open set
$\{0\}$ has preimage $\{0\}$, which is not open in the ordinary topology. So
(D) fails.

:::

:::

::: {.pf-step #conclusion}

(A), (B) and (C) hold in $(\RR,d)$ and (D) does not.

::: pf-proof

Steps [](#opensets){.pf-ref} and [](#identity){.pf-ref} settle all four items.
The point is that the discrete metric makes every set open, so the space is
disconnected and the identity map out of it is continuous, while a map into it
is continuous only when the source is discrete.

:::

:::

:::


:::
