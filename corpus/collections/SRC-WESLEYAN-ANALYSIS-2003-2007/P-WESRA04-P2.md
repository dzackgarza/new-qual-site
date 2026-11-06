---
schema: qual/card@1
id: P-WESRA04-P2
kind: problem
title: Total variation is lower semicontinuous under pointwise convergence
classification:
  areas: [real-analysis]
  topics: [Bounded Variation]
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the Wesleyan Preliminary Examination, Analysis, August 2, 2004,
    Real Analysis section 2.3 problem 2 (assets/attachments/analysis_2003-2007.pdf,
    PDF page 35, printed page 3), from the checked-in MinerU extraction and a
    100 dpi render of the page. The printed problem supposes a sequence
    converging pointwise to f on [a,b] and asks for T_a^b(f) <= liminf
    T_a^b(f_n), where T denotes total variation. The card states exactly this,
    so no repair was needed; the extraction's garbled limit sign is the liminf of
    the render.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The proof is
    derived here, by testing the supremum over partitions against one partition
    at a time.
---

::: {.problem}
Let $(f_n)$ be a sequence of functions on $[a,b]$ converging pointwise to $f$.
If $T_a^b(h)$ denotes the total variation of $h$ on $[a,b]$, prove that
$$
T_a^b(f)\le \liminf_{n\to\infty}T_a^b(f_n).
$$
:::

::: {.solution}

Let $f_n,f\colon[a,b]\to\RR$ with $f_n\to f$ pointwise, and for
$h\colon[a,b]\to\RR$ let $T_a^b(h)=\sup_PV_P(h)$ over partitions $P\colon
a=x_0<x_1<\dots<x_m=b$, where $V_P(h)=\sum_{j=1}^m\abs{h(x_j)-h(x_{j-1})}$,
both allowed to be $+\infty$.

::: pf

::: {.pf-step #partition}

For each fixed partition $P$, $V_P(f_n)\to V_P(f)$.

::: pf-proof

$P$ has finitely many points $x_0,\dots,x_m$, and $f_n(x_j)\to f(x_j)$ at each
of them. Each term $\abs{f_n(x_j)-f_n(x_{j-1})}$ is a continuous function of
the pair $(f_n(x_j),f_n(x_{j-1}))$, so the finitely many terms converge to
$\abs{f(x_j)-f(x_{j-1})}$; a finite sum of convergent sequences converges to
the sum of the limits, which is $V_P(f)$.

:::

:::

::: {.pf-step #bound}

$V_P(f)\le\liminf_nT_a^b(f_n)$ for every partition $P$.

::: pf-proof

For every $n$ we have $V_P(f_n)\le T_a^b(f_n)$, since $T_a^b$ is the supremum
over all partitions including this one. If $a_n\le b_n$ for all $n$ then
$\liminf a_n\le\liminf b_n$: a subsequence realizing the liminf of $a$ gives
$\liminf b\ge\liminf a$. Applying this with $a_n=V_P(f_n)$ and
$b_n=T_a^b(f_n)$, and using step [](#partition){.pf-ref} to replace $\liminf
a_n$ by $\lim a_n=V_P(f)$, gives the claim.

:::

:::

::: {.pf-step #supremum}

$T_a^b(f)\le\liminf_nT_a^b(f_n)$.

::: pf-proof

Step [](#bound){.pf-ref} says the number $L=\liminf_nT_a^b(f_n)\in[0,\infty]$
dominates $V_P(f)$ for every partition $P$; hence it dominates the supremum
over $P$, which is $T_a^b(f)$ by definition. So the total variation is lower
semicontinuous with respect to pointwise convergence, which is the assertion;
the inequality can be strict, as when $f_n$ alternates rapidly with bounded
variation tending to infinity while $f\equiv0$.

:::

:::

:::


:::
