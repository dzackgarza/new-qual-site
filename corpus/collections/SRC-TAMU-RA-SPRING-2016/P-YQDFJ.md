---
schema: qual/card@1
id: P-YQDFJ
kind: problem
title: A continuous bounded-variation path cannot fill the unit square
classification:
  areas:
  - real-analysis
  topics:
  - Variation
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's proof into numbered steps; the bounded-variation bound, the grid of
    centres, the lower estimate n - 1/n and the contradiction are unchanged, with the equivalence
    of the two norms on R^2 made explicit. Checked: the componentwise variation bound, that
    distinct grid points are at distance at least 1/n, and the count n^2 - 1 of consecutive pairs.
    Not checked against a printed source: the TAMU preliminary examinations are not retained in
    tmp/sources and the card records no page.
---

::: {.problem}
Suppose $f,g:[a,b]\to\RR$ are both continuous and of bounded variation.
Show that the set $\{(f(t),g(t))\in\RR^2 : t\in[a,b]\}$ cannot cover the entire unit square $[0,1]\times[0,1]$.
:::

::: {.solution}

The argument is the card's own: no solution set for this examination is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $f,g:[a,b]\to\RR$ are continuous and of bounded variation, $r(t)=(f(t),g(t))$, and $V$ is a bound for the total variation of $r$, which exists because the variation of $r$ is controlled by those of $f$ and $g$: the $\ell^{2}$ norm is at most $\sqrt2$ times the $\ell^{1}$ norm on $\RR^{2}$.

::: pf

::: {.pf-step #bv}

There is $V<\infty$ with $\sum_{j=1}^{n}\norm{r(t_j)-r(t_{j-1})}_{2}\leq V$ for every partition $a=t_0<\cdots<t_n=b$.

::: pf-proof

For each partition, $\norm{r(t_j)-r(t_{j-1})}_{2}\leq\abs{f(t_j)-f(t_{j-1})}+\abs{g(t_j)-g(t_{j-1})}$, so the sum is at most the sum of the variations of $f$ and of $g$ over that partition, each bounded by the respective total variations, which are finite.

:::

:::

::: {.pf-step #grid}

Suppose the image covers $[0,1]^{2}$; then for each $n$ there are points $s_1<\cdots<s_{n^{2}}$ in $[a,b]$ whose images are distinct points of the grid $\left(\frac{i}{n},\frac{j}{n}\right)$, $1\leq i,j\leq n$.

::: pf-proof

Cover the square by the $n^{2}$ closed subsquares of side $1/n$ with centres $z_{ij}=\left(\frac{i-1/2}{n},\frac{j-1/2}{n}\right)$; each centre lies in the image, so pick $t_{ij}$ with $r(t_{ij})=z_{ij}$, and relabel the chosen arguments in increasing order.

:::

:::

::: {.pf-step #lower}

$\sum_{j=1}^{n^{2}-1}\norm{r(s_{j+1})-r(s_{j})}_{2}\geq\frac{n^{2}-1}{n}=n-\frac1n$.

::: pf-proof

Distinct grid points differ in at least one coordinate by a multiple of $1/n$, hence by at least $1/n$ in absolute value, so each distance between consecutive $s_{j}$ is at least $1/n$; summing $n^{2}-1$ such terms gives the bound.

:::

:::

::: {.pf-step #done}

The image does not cover $[0,1]^{2}$.

::: pf-proof

The left side of step [](#lower){.pf-ref} is a sum over a partition of $[a,b]$, hence at most $V$ by step [](#bv){.pf-ref}, while $n-1/n$ exceeds $V$ for $n$ large; that contradiction refutes the covering supposition of step [](#grid){.pf-ref}.

:::

:::

:::

:::
