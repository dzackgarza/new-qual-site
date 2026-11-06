---
schema: qual/card@1
id: P-PRACT20-W6-03
kind: problem
title: Candidate metrics on $\RR$
classification:
  areas:
  - prelim
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
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
    on the card: each of the five options was checked against the three metric axioms, and the failure of the triangle inequality for option (E) verified on the points 0, 1, 2
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. The three axioms checked option by option, with the triangle inequality for the bounded metrics and the explicit failure for (x-y)^2
---

::: {.problem}
Which of the following does not define a metric on $\RR$?

(A) $\delta(x, y) = \begin{cases} 0, & x = y, \\ 2, & x \neq y. \end{cases}$

(B) $\rho(x, y) = \min\{\abs{x - y}, 1\}$

(C) $\sigma(x, y) = \dfrac{\abs{x - y}}{3}$

(D) $\tau(x, y) = \dfrac{\abs{x - y}}{\abs{x - y} + 1}$

(E) $\omega(x, y) = (x - y)^{2}$
:::

::: {.solution}

Let $d$ be one of the five displayed functions on $\RR$. The axioms are
$d(x,y)\ge0$ with equality iff $x=y$, symmetry, and the triangle inequality.

::: pf

::: {.pf-step #fourmetrics}

(A), (B), (C) and (D) each define a metric on $\RR$.

::: pf-proof

(A) The discrete metric with value $2$: nonnegativity and symmetry are clear,
$d(x,y)=0$ iff $x=y$, and the triangle inequality holds because the left side
is at most $2$ and the right side is $0$ when $x=y=z$ and at least $2$
otherwise. (B) $\min\{\abs{x-y},1\}$ is nonnegative, symmetric and vanishes
only on the diagonal; for the triangle inequality,
$\min\{a+b,1\}\le\min\{a,1\}+\min\{b,1\}$ for $a,b\ge0$: if both $a,b\le1$
this is $a+b$ on both sides, and if say $a>1$ the left side is at most
$1\le\min\{a,1\}$. (C) $\abs{x-y}/3$ is a positive multiple of a metric, hence
a metric. (D) $\abs{x-y}/(\abs{x-y}+1)=g(\abs{x-y})$ where $g(t)=t/(1+t)$, and
$g$ is increasing with $g(a+b)\le g(a)+g(b)$ for $a,b\ge0$, which is the
triangle inequality; the other axioms are immediate.

:::

:::

::: {.pf-step #notmetric}

(E) $\omega(x,y)=(x-y)^2$ is not a metric.

::: pf-proof

$\omega(0,2)=4$ while $\omega(0,1)+\omega(1,2)=1+1=2$, so the triangle
inequality fails; equivalently the quantity is not homogeneous. Hence (E) is
the one that does not define a metric.

:::

:::

:::


:::
