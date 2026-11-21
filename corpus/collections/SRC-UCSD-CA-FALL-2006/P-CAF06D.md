---
schema: qual/card@1
id: P-CAF06D
kind: problem
title: "Growth estimate for entire functions in terms of their zeros"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Replaced the prose solution with a Lamport proof. The prose chose R = 2|a_k|
    outright, where a zero can sit on the circle and Jensen's formula does not apply;
    the proof now runs Jensen on the admissible radii R = 2|a_k| - delta and passes to
    the limit, and records that no zero of f is 0 because f(0) = 1. Checked: Jensen
    with log|f(0)| = 0, the count of the first k zeros inside R, the termwise bound by
    log(2 - delta/|a_k|), monotonicity of M, and density of the admissible radii. The
    collection's provenance is the examination paper only, so no retained solution set
    covers the exercise and the argument is the card's own.
---

::: {.problem}
Assume that $f$ is an entire function.
Let $M(r) = \sup_{\abs{z}=r} \abs{f(z)}$.
Assume that the discrete sequence $\{a_n\}$ are zeros of $f$, indexed so that
$\abs{a_1}\le \abs{a_2}\le\cdots$, and $f(0) = 1$.
Show that $$k\log 2 \leq \log(M(2\abs{a_k})).$$
:::

::: {.remark}
The Fall 2006 source does not state the ordering of $\{a_n\}$. The displayed
inequality requires the standard convention that the zeros are indexed by
nondecreasing modulus; without it, an arbitrary re-enumeration makes the claim
false.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #nonzero}
No zero of $f$ is $0$, so $\abs{a_j}>0$ for every $j$; in particular $\abs{a_k}>0$ and every logarithm $\log\abs{a_j}$ below is defined.

::: pf-proof
$f(0)=1\ne0$, and each $a_j$ is a zero of $f$.
:::

:::

::: {.pf-step #jensen}
For every $R>0$ with no zero of $f$ on the circle $\abs{z}=R$,
$$
\sum_{\abs{a_j}<R}\log\frac{R}{\abs{a_j}}
=\frac{1}{2\pi}\int_0^{2\pi}\log\abs{f(Re^{it})}\,dt
\le\log M(R),
$$
the sum being taken over the listed zeros lying inside the circle.

::: pf-proof
Jensen's formula reads
$$
\log\abs{f(0)}+\sum_{\abs{a_j}<R}\log\frac{R}{\abs{a_j}}=\frac{1}{2\pi}\int_0^{2\pi}\log\abs{f(Re^{it})}\,dt,
$$
and $\log\abs{f(0)}=\log1=0$. For each $t$ the integrand satisfies $\log\abs{f(Re^{it})}\le\log M(R)$, because $M(R)$ is the supremum of $\abs{f}$ on that circle, so the integral is at most $\log M(R)$.
:::

:::

::: {.pf-step #counted}
If $0<\delta<\abs{a_k}$ and $R\coloneqq2\abs{a_k}-\delta$, then every listed zero $a_j$ with $j\le k$ satisfies $\abs{a_j}<R$.

::: pf-proof
The ordering gives $\abs{a_j}\le\abs{a_k}$ for $j\le k$, and $0<\delta<\abs{a_k}$ gives $\abs{a_k}<2\abs{a_k}-\delta=R$, so $\abs{a_j}\le\abs{a_k}<R$.
:::

:::

::: {.pf-step #delta}
For every $\delta$ with $0<\delta<\abs{a_k}$ for which no zero of $f$ lies on the circle $\abs{z}=2\abs{a_k}-\delta$,
$$
k\log\left(2-\frac{\delta}{\abs{a_k}}\right)\le\log M(2\abs{a_k}).
$$

::: pf-proof
Put $R\coloneqq2\abs{a_k}-\delta$, which is positive by step [](#nonzero){.pf-ref}. Every term of the sum in step [](#jensen){.pf-ref} is nonnegative, since $\abs{a_j}<R$ gives $R/\abs{a_j}>1$. By step [](#counted){.pf-ref} the $k$ listed zeros $a_1,\ldots,a_k$ occur in that sum, so
$$
\sum_{\abs{a_j}<R}\log\frac{R}{\abs{a_j}}
\ge\sum_{j=1}^{k}\log\frac{R}{\abs{a_j}}
\ge\sum_{j=1}^{k}\log\frac{R}{\abs{a_k}}
=k\log\left(2-\frac{\delta}{\abs{a_k}}\right),
$$
the second inequality using $\abs{a_j}\le\abs{a_k}$ and monotonicity of the logarithm. Step [](#jensen){.pf-ref} bounds the left side by $\log M(R)$, and $R<2\abs{a_k}$ with $M$ nondecreasing gives $\log M(R)\le\log M(2\abs{a_k})$.
:::

:::

::: {.pf-step #small-deltas}
There are admissible $\delta$ as in step [](#delta){.pf-ref} tending to $0$.

::: pf-proof
The set of radii $r>0$ whose circle carries a zero of $f$ is $\{\abs{a_j}\}$, countable because it is the image of the discrete sequence $(a_j)$. A countable subset of the interval $(0,\abs{a_k})$ cannot contain an interval, so for every $n$ there is $\delta\in(0,\min\{\abs{a_k},1/n\})$ with no zero on the circle $\abs{z}=2\abs{a_k}-\delta$; these $\delta$ tend to $0$.
:::

:::

::: {.pf-step}
$k\log2\le\log M(2\abs{a_k})$.

::: pf-proof
By steps [](#delta){.pf-ref} and [](#small-deltas){.pf-ref} the inequality
$$
k\log\left(2-\frac{\delta}{\abs{a_k}}\right)\le\log M(2\abs{a_k})
$$
holds along a sequence $\delta\to0$. Its left side tends to $k\log2$, the logarithm being continuous and $\abs{a_k}>0$ by step [](#nonzero){.pf-ref}, so the limit gives $k\log2\le\log M(2\abs{a_k})$.
:::

:::

:::
:::
