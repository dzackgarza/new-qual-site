---
schema: qual/card@1
id: E-VPZUZ
kind: problem
title: Equicontinuous pointwise limits converge compactly
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Function Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §47 Exercise 5 (printed p. 293) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the definitions of
    pointwise convergence (§46, Theorem 46.1) and compact convergence (§46, Theorem 46.2). Continuity of the
    limit: at x, equicontinuity gives a neighbourhood U on which every f_n moves each point by less than
    eps/3, and passing to the limit in n gives the same bound for f, so f is continuous at x. Uniform
    convergence on a compact set: the Lebesgue-number-free finite subcover of the equicontinuity
    neighbourhoods, the three-term triangle inequality, and finiteness of the cover to choose N. Nothing needed
    correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). The AoPS blog post by cinnamon_e, "Topology by
    Munkres Chapter 7 | Day 17" (2025-09-10,
    https://artofproblemsolving.com/community/c3401823h3646977, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day17.md), answers this exercise at its item 5 of
    §47, and the extraction dropped every inline formula, so the answer cannot be transcribed; the
    site answers an automated request with a Cloudflare human check, which is not worked around.
    Murayama's selection stops at Chapter 4, dbFin has no chapter-7 page, and the Math StackExchange
    searches of this pass, recorded in the COMPLAINTS.md entry for §43--§50, returned nothing on the
    continuity of a pointwise limit of an equicontinuous sequence. The card keeps its own proof.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the argument already on the card, which is correct.
    Added: the triangle inequality written out in the continuity step, including the observation
    that the limit of the middle term is bounded by the fixed epsilon/3 rather than killed; the
    separate step recording that the equicontinuity neighbourhood gives the same bound for f
    simultaneously, which the compactness step uses for its third term; and the attribution of
    the exercise to §47 of the book. Not claimed: a retained solution set; the argument is the
    card's own, and the card's earlier audit records the search.
---

::: {.exercise}

Let $(Y, d)$ be a metric space; let $f_n: X \to Y$ be a sequence of continuous functions; let $f: X \to Y$ be a function (not necessarily continuous).
Suppose $f_n$ converges to $f$ in the topology of pointwise convergence.
Show that if $\theset{f_n}$ is equicontinuous, then $f$ is continuous and $f_n$ converges to $f$ in the topology of compact convergence.
:::

::: {.solution}
Throughout $(Y,d)$ is a metric space, $X$ is a topological space, $f_{n}\colon X \to Y$ are continuous and $f\colon X \to Y$ satisfies $f_{n}(x) \to f(x)$ for every $x \in X$; the family $\theset{f_{n}}$ is equicontinuous, meaning that for each $x$ and each $\varepsilon > 0$ there is a neighbourhood $U$ of $x$ with $d\bigl(f_{n}(y),f_{n}(x)\bigr) < \varepsilon$ for every $y \in U$ and every $n$. Convergence in the topology of compact convergence means uniform convergence on every compact subspace of $X$. The exercise is Munkres, *Topology* (2000), §47.

::: pf

::: {.pf-step #point-continuity}
$f$ is continuous.

::: pf-proof
Fix $x \in X$ and $\varepsilon > 0$. Equicontinuity gives a neighbourhood $U$ of $x$ with $d(f_{n}(y),f_{n}(x)) < \varepsilon/3$ for all $y \in U$ and all $n$. For such $y$, $d(f(y),f(x)) \le d(f(y),f_{n}(y)) + d(f_{n}(y),f_{n}(x)) + d(f_{n}(x),f(x))$, and letting $n \to \infty$ kills the first and last terms by pointwise convergence while the middle stays below $\varepsilon/3$; hence $d(f(y),f(x)) \le \varepsilon/3 < \varepsilon$ for every $y \in U$, which is continuity of $f$ at $x$.

:::

:::

::: {.pf-step #same-bound}
For every $x \in X$ and $\varepsilon > 0$ there is a neighbourhood $U$ of $x$ with $d(f(y),f(x)) \le \varepsilon/3$ for all $y \in U$, simultaneously with $d(f_{n}(y),f_{n}(x)) < \varepsilon/3$ for all $n$.

::: pf-proof
Take the neighbourhood given by equicontinuity at $x$ for $\varepsilon/3$; the bound for $f$ follows from it by the same passage to the limit as in step [](#point-continuity){.pf-ref}, with the middle term now bounded by the fixed $\varepsilon/3$ instead of being killed.

:::

:::

::: {.pf-step #compact}
For every compact $K \subseteq X$ the sequence $f_{n}$ converges to $f$ uniformly on $K$.

::: pf-proof
Fix $\varepsilon > 0$. For each $x \in K$ let $U_{x}$ be the neighbourhood supplied by step [](#same-bound){.pf-ref}; the $U_{x}$ cover $K$, so compactness gives $x_{1},\ldots,x_{r}$ with $K \subseteq U_{x_{1}} \cup \cdots \cup U_{x_{r}}$. For each $i$ pointwise convergence gives $N_{i}$ with $d(f_{n}(x_{i}),f(x_{i})) < \varepsilon/3$ for $n \ge N_{i}$; let $N \coloneqq \max_{i}N_{i}$. For $y \in K$ and $n \ge N$ choose $i$ with $y \in U_{x_{i}}$; then $d(f_{n}(y),f(y)) \le d(f_{n}(y),f_{n}(x_{i})) + d(f_{n}(x_{i}),f(x_{i})) + d(f(x_{i}),f(y)) < \varepsilon/3 + \varepsilon/3 + \varepsilon/3 = \varepsilon$. The bound is uniform in $y \in K$, which is uniform convergence on $K$.

:::

:::

::: pf-step
$f$ is continuous and $f_{n} \to f$ in the topology of compact convergence.

::: pf-proof
Continuity is step [](#point-continuity){.pf-ref}, and step [](#compact){.pf-ref} gives uniform convergence on each compact subspace, which is convergence in the topology of compact convergence. The conclusion does not require $X$ to be anything more than a topological space, and $f$ need not be assumed continuous in advance.

:::

:::

:::
:::
