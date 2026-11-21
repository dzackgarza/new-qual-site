---
schema: qual/card@1
id: P-I6PEO
kind: problem
title: $1/f$ has bounded variation on $[a,b]$ when $f$ does and $\abs{f}\ge c>0$
classification:
  areas:
  - real-analysis
  topics:
  - Variation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against the Lamport standard and checked. For a partition x_0 < ... < x_n,
    |g(x_i) - g(x_{i-1})| = |f(x_{i-1}) - f(x_i)| / |f(x_i) f(x_{i-1})| <=
    |f(x_i) - f(x_{i-1})| / c^2 because both values have modulus at least c, so every variation sum
    of g is at most c^{-2} times the corresponding sum for f, and taking suprema gives
    V(g) <= c^{-2} V(f) < infinity. The hypothesis |f| >= c is used exactly there, and it cannot be
    weakened to f having no zeros at isolated points without losing uniformity of the bound. The
    card's steps follow this. Not claimed: any quantitative improvement on the constant c^{-2}.
---
::: {.problem}
Let $f$ be a function of bounded variation on $[a,b]$.
Furthermore, assume that for some $c>0$, $\abs{f(x)} \geq c$ on $[a,b]$.
Show that $g(x) = 1/f(x)$ is of bounded variation on $[a,b]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $x, y \in [a,b]$, $\abs{g(x)-g(y)} \le c^{-2}\abs{f(x) - f(y)}$.

::: pf-proof

The lower bound $\abs{f}\geq c>0$ ensures that $g=1/f$ is defined everywhere. For any $x,y\in[a,b]$,
$$
\abs{g(x)-g(y)}=\frac{\abs{f(y)-f(x)}}{\abs{f(x)f(y)}}
\leq c^{-2}\abs{f(y)-f(x)},
$$
since $\abs{f(x)f(y)}\geq c^2$.

:::

:::

::: {.pf-step #s2}

For any partition $a = x_0 < \cdots < x_n = b$, $\sum_{i=1}^n \abs{g(x_i) - g(x_{i-1})} \le c^{-2}\sum_{i=1}^n \abs{f(x_i) - f(x_{i-1})} \le c^{-2}V_{[a,b]}(f)$.

::: pf-proof

Step [](#s1){.pf-ref} applies to each pair $(x_i,x_{i-1})$; summing gives the first inequality. By definition, every partition variation sum of $f$ is bounded above by $V_{[a,b]}(f)$.

:::

:::

::: pf-step

$V_{[a,b]}(g)\leq c^{-2}V_{[a,b]}(f)<\infty$, so $g$ is of bounded variation.

::: pf-proof

$V_{[a,b]}(g)$ is the supremum of the left-hand partition sums in step [](#s2){.pf-ref} over all finite partitions of $[a,b]$. The right-hand bound is independent of the partition and finite because $f$ has bounded variation.

:::

:::

:::

:::
