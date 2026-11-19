---
schema: qual/card@1
id: E-PKDH7
kind: problem
title: Pointwise boundedness and equicontinuity of four collections
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §47 Exercise 1 (printed p. 292) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the definitions of
    pointwise boundedness and equicontinuity in §45 and §47. (a) is pointwise bounded by |x| + 1 and fails
    equicontinuity at 0, taking x = pi/(2n): then f_n(x) - f_n(0) = pi/(2n) + 1. (b) is nowhere pointwise
    bounded, since g_n(x) = n + sin x is unbounded in n, and is equicontinuous since |sin x - sin y| <= |x - y|
    for all n. (c) is pointwise bounded, lying between 0 and max{1,|x|}, and fails equicontinuity at 0: for any
    delta take 0 < x < min{delta,1} and then n with x^{1/n} > 1/2. (d) is pointwise bounded by |x| and
    equicontinuous since n|sin(x/n) - sin(y/n)| <= |x - y|. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). The AoPS blog post by cinnamon_e, "Topology by
    Munkres Chapter 7 | Day 17" (2025-09-10,
    https://artofproblemsolving.com/community/c3401823h3646977, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day17.md), answers this exercise at its item 1 of
    §47, and the extraction dropped every inline formula, so the answer cannot be transcribed; the
    site answers an automated request with a Cloudflare human check, which is not worked around.
    Murayama's selection stops at Chapter 4, dbFin has no chapter-7 page, and the Math StackExchange
    searches of this pass for these four families, recorded in the COMPLAINTS.md entry for §43--§50,
    returned nothing on them. The card keeps its own proof.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the four determinations already on the card, all of which
    are correct. Added: the choice n > pi/(2 delta) that makes the witness x = pi/(2n) lie
    within delta in (a); the two-sided bound max{1, |x|} for h_n in (c) with the case
    distinction on |x|; the mean value theorem as the reason |sin y - sin x| <= |y - x| in (b)
    and (d); and the convergence x^{1/n} -> 1 that produces the failure in (c). Not claimed: a
    retained solution set; the collection's provenance is the Munkres textbook, whose text is
    not retained here.
---

::: {.exercise}

Which of the following subsets of $\mathcal{C}(\RR, \RR)$ are pointwise bounded?
Which are equicontinuous?

(a) The collection $\theset{f_n}$, where $f_n(x) = x + \sin nx$.

(b) The collection $\theset{g_n}$, where $g_n(x) = n + \sin x$.

(c) The collection $\theset{h_n}$, where $h_n(x) = \abs{x}^{1/n}$.

(d) The collection $\theset{k_n}$, where $k_n(x) = n \sin(x/n)$.
:::

::: {.solution}
Throughout a family $\mathcal{G} \subseteq \mathcal{C}(\RR,\RR)$ is pointwise bounded when for each $x$ the set $\theset{g(x) \mid g \in \mathcal{G}}$ is bounded, and equicontinuous when for each $x$ and each $\varepsilon > 0$ there is $\delta > 0$ with $\abs{g(y) - g(x)} < \varepsilon$ for all $\abs{y - x} < \delta$ and all $g \in \mathcal{G}$. The exercise is Munkres, *Topology* (2000), §47.

::: pf

::: {.pf-step #a-bounded}
(a) The family $f_{n}(x) = x + \sin nx$ is pointwise bounded and not equicontinuous.

::: pf-proof
Boundedness: $\abs{f_{n}(x)} \le \abs{x} + \abs{\sin nx} \le \abs{x} + 1$ for every $n$. Failure of equicontinuity at $0$: take $\varepsilon = 1$ and any $\delta > 0$; choose $n > \pi/(2\delta)$ and $x = \pi/(2n) < \delta$. Then $f_{n}(x) - f_{n}(0) = \frac{\pi}{2n} + \sin\frac{\pi}{2} = \frac{\pi}{2n} + 1 > 1 = \varepsilon$.

:::

:::

::: {.pf-step #b-bounded}
(b) The family $g_{n}(x) = n + \sin x$ is not pointwise bounded and is equicontinuous.

::: pf-proof
At a fixed $x$ one has $g_{n}(x) \ge n - 1$, which is unbounded above, so the family is not pointwise bounded. Equicontinuity: $\abs{g_{n}(y) - g_{n}(x)} = \abs{\sin y - \sin x} \le \abs{y - x}$ by the mean value theorem applied to $\sin$, and the bound does not involve $n$, so $\delta = \varepsilon$ serves at every point.

:::

:::

::: {.pf-step #c-bounded}
(c) The family $h_{n}(x) = \abs{x}^{1/n}$ is pointwise bounded and not equicontinuous.

::: pf-proof
At a fixed $x$: if $\abs{x} \ge 1$ then $\abs{x}^{1/n} \le \abs{x}$ because $t^{1/n} \le t$ for $t \ge 1$ and $n \ge 1$; if $\abs{x} \le 1$ then $\abs{x}^{1/n} \le 1$. So $0 \le h_{n}(x) \le \max\theset{1,\abs{x}}$ for every $n$. Failure of equicontinuity at $0$: given $\delta > 0$ take $0 < x < \min\theset{\delta,1}$; since $x^{1/n} \to 1$ as $n \to \infty$ there is $n$ with $h_{n}(x) > 1/2$, while $h_{n}(0) = 0$, so $\abs{h_{n}(x) - h_{n}(0)} > 1/2$.

:::

:::

::: {.pf-step #d}
(d) The family $k_{n}(x) = n\sin(x/n)$ is pointwise bounded and equicontinuous.

::: pf-proof
Bounded: $\abs{k_{n}(x)} = n\abs{\sin(x/n)} \le n\abs{x/n} = \abs{x}$ using $\abs{\sin t} \le \abs{t}$. Equicontinuous: $\abs{k_{n}(y) - k_{n}(x)} = n\abs{\sin(y/n) - \sin(x/n)} \le n\abs{y/n - x/n} = \abs{y - x}$, again by the mean value theorem, with the factor $n$ cancelling.

:::

:::

::: pf-step
The four answers are: (a) pointwise bounded, not equicontinuous; (b) not pointwise bounded, equicontinuous; (c) pointwise bounded, not equicontinuous; (d) both.

::: pf-proof
Steps [](#a-bounded){.pf-ref}, [](#b-bounded){.pf-ref}, [](#c-bounded){.pf-ref} and [](#d){.pf-ref} settle the four families, each with an explicit bound or an explicit pair witnessing the failure.

:::

:::

:::
:::
