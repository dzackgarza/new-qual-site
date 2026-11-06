---
schema: qual/card@1
id: P-PRACT20-W6-08
kind: problem
title: Continuous surjections and bijections between $(0,1)$ and $[0,1]$
classification:
  areas:
  - prelim
  topics:
  - Continuity
  - Compactness
  - Intermediate Value Theorem
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
    on the card: the three existence questions were each settled: one by an explicit continuous surjection onto the closed interval, one by compactness, one by monotonicity of continuous injections
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. An explicit surjection for (A), a compactness obstruction for (B), and strict monotonicity for (C)
---

::: {.problem}
Which of the following exist?

(A) A continuous function from $(0, 1)$ onto $[0, 1]$

(B) A continuous function from $[0, 1]$ onto $(0, 1)$

(C) A continuous bijection from $(0, 1)$ to $[0, 1]$
:::

::: {.solution}

A continuous function on $(0,1)$ has connected image, an interval; the
question is whether that interval can be $[0,1]$ or $(0,1)$.

::: pf

::: {.pf-step #onto}

(A) exists: for instance $f(x)=\abs{\sin(2\pi x)}$ maps $(0,1)$ continuously
onto $[0,1]$.

::: pf-proof

$\sin(2\pi x)$ attains $0$ at $x=\frac12$ and $\pm1$ at $x=\frac14,\frac34$,
all interior points of $(0,1)$, and its absolute value is continuous with
values in $[0,1]$; every value in $[0,1]$ is attained, by the intermediate
value theorem applied on $[\frac14,\frac12]$ and on $[\frac12,\frac34]$. So
the image is exactly $[0,1]$, and the function is continuous on $(0,1)$.

:::

:::

::: {.pf-step #fromcompact}

(B) does not exist: a continuous image of the compact set $[0,1]$ is compact,
and $(0,1)$ is not compact.

::: pf-proof

$[0,1]$ is compact and a continuous image of a compact space is compact, so
$f([0,1])$ is a compact subset of $\RR$. But $(0,1)$ is not compact: the cover
by the open sets $(1/n,1)$, $n\ge2$, has no finite subcover, since any finite
subcollection is contained in $(1/N,1)$ for the largest $N$ used and misses
$1/(N+1)$. Hence no continuous $f$ maps $[0,1]$ onto $(0,1)$, and (B) does not
exist.

:::

:::

::: {.pf-step #bijection}

(C) does not exist: a continuous injection on an interval is strictly
monotone, so its image of $(0,1)$ cannot be the closed interval $[0,1]$.

::: pf-proof

If $f$ is continuous and injective on the interval $(0,1)$, then it is
strictly monotone: for $a<b<c$, injectivity and the intermediate value theorem
force $f(b)$ to lie strictly between $f(a)$ and $f(c)$, and the sign of the
differences is then constant. A strictly monotone continuous function on
$(0,1)$ has image $\big(\lim_{x\to0^+}f(x),\lim_{x\to1^-}f(x)\big)$, an
interval with open or infinite endpoints; in particular both endpoints of the
interval $\{f(x):x\in(0,1)\}$ are not attained, so the image is never the
closed interval $[0,1]$. So a continuous bijection $(0,1)\to[0,1]$ does not
exist.

:::

:::

:::


:::
