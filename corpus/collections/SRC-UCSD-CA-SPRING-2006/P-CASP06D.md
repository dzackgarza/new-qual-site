---
schema: qual/card@1
id: P-CASP06D
kind: problem
title: "Finite order entire functions agreeing on a sufficiently dense sequence are equal"
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
    Restructured the prose solution into a Lamport proof and checked it: the order bound
    n_h(r) = O(r^(lambda+delta)) from Jensen and the growth estimate (including the h(0)=0
    reduction), the Stieltjes identity as a Fubini sum with its counting function, the
    exponent arithmetic giving t^(-1-eps/2), and the contradiction with a divergent sum.
    The printed statement omits that the a_n are nonzero, distinct and unbounded; the
    argument uses it and the remark on the card records it with a counterexample (a_n = 0
    for all n). The collection's provenance is the examination paper only, so no retained
    solution set covers the exercise and the argument is the card's own.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    Recorded in a remark, not by rewriting the printed problem: the statement is false
    without |a_n| -> infinity, distinctness and a_n != 0.
---

::: {.problem}
Assume that $f$ and $g$ are entire functions of finite order $\lambda$.
Assume that for a sequence $a_n$, $f(a_n) = g(a_n)$ and $\sum \abs{a_n}^{-(\lambda + \epsilon)} = \infty$ for some $\epsilon > 0$.
Show that $f = g$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
The argument uses that the $a_n$ are distinct, nonzero, and unbounded, as the summands $\abs{a_n}^{-(\lambda+\varepsilon)}$ already presuppose; see the remark on the card.

::: pf

::: {.pf-step}
Suppose $h\coloneqq f-g$ is not identically zero; then the $a_n$ are zeros of $h$.

::: pf-proof
$h$ is entire and $h(a_n)=f(a_n)-g(a_n)=0$ for every $n$.
:::

:::

::: {.pf-step #order}
$h$ has finite order at most $\lambda$, and consequently for every $\delta>0$ there is $C_\delta$ with $n_h(r)\le C_\delta r^{\lambda+\delta}$ for all $r\ge1$, where $n_h(r)$ is the number of zeros of $h$ in $\abs{z}\le r$, counted with multiplicity.

::: pf-proof
The order of a difference of entire functions is at most the larger of their orders, so $h$ has order at most $\lambda$; thus for every $\eta>0$ there are constants $A,B$ with $\abs{h(z)}\le A e^{B\abs{z}^{\lambda+\eta}}$, that is $\log M_h(r)\le\log A+Br^{\lambda+\eta}$. Jensen's formula applied to $h$ with $h(0)\ne0$ gives $n_h(r)\log2\le\log M_h(2r)-\log\abs{h(0)}$, and the growth estimate turns the right side into $O(r^{\lambda+\eta})$; take $\eta=\delta$. When $h(0)=0$ apply the same to $h(z)/z^m$, whose zeros have the same count as those of $h$ for $r\ge1$ and whose order is that of $h$.
:::

:::

::: {.pf-step #stieltjes}
With $s\coloneqq\lambda+\varepsilon$ and $N(t)\coloneqq\#\{n:\ 1\le\abs{a_n}\le t\}$,
$$
\sum_{\abs{a_n}\ge1}\abs{a_n}^{-s}=s\int_1^{\infty}\frac{N(t)}{t^{s+1}}\,dt,
$$
and $N(t)\le n_h(t)$ for every $t\ge1$.

::: pf-proof
Order the listed radii $\abs{a_n}\ge1$ as $1\le r_1\le r_2\le\cdots$, so that $N(t)=\#\{j:r_j\le t\}$. For each $t$ one has $N(t)=\sum_j\mathbf{1}_{r_j\le t}$, and $t\mapsto t^{-s-1}$ is positive, so Fubini's theorem for sums of nonnegative terms gives
$$
s\int_1^{\infty}\frac{N(t)}{t^{s+1}}\,dt=s\sum_j\int_{r_j}^{\infty}t^{-s-1}\,dt=\sum_j r_j^{-s},
$$
which is the stated identity. The inequality $N(t)\le n_h(t)$ holds because the points $a_n$ with $1\le\abs{a_n}\le t$ are distinct zeros of $h$ in $\abs{z}\le t$.
:::

:::

::: {.pf-step #finite}
$\sum_n\abs{a_n}^{-(\lambda+\varepsilon)}<\infty$, that is $\sum_{\abs{a_n}\ge1}\abs{a_n}^{-s}<\infty$.

::: pf-proof
Take $\delta=\varepsilon/2$ in step [](#order){.pf-ref} and use step [](#stieltjes){.pf-ref}:
$$
\frac{N(t)}{t^{s+1}}\le\frac{C_\delta t^{\lambda+\varepsilon/2}}{t^{\lambda+\varepsilon+1}}=C_\delta t^{-1-\varepsilon/2},
$$
which is integrable on $[1,\infty)$. Hence the integral in step [](#stieltjes){.pf-ref} converges, and the sum over the listed points with $\abs{a_n}\ge1$ is finite. The remaining terms, those with $0<\abs{a_n}<1$, are finitely many because $\abs{a_n}\to\infty$, so adding them keeps the total finite.
:::

:::

::: {.pf-step}
$f=g$.

::: pf-proof
The hypothesis gives $\sum_n\abs{a_n}^{-(\lambda+\varepsilon)}=\infty$, which contradicts step [](#finite){.pf-ref} under the assumption of step [](#order){.pf-ref} that $h$ is not identically zero. Hence $h\equiv0$, that is $f=g$.
:::

:::

:::

::: {.remark}
As printed the statement omits the requirement that the $a_n$ be nonzero, distinct and unbounded, which the summands $\abs{a_n}^{-(\lambda+\varepsilon)}$ presuppose; without it the claim is false, since $a_n=0$ for every $n$ makes the sum diverge while $f(0)=g(0)$ holds for unrelated $f$ and $g$.
:::
:::
