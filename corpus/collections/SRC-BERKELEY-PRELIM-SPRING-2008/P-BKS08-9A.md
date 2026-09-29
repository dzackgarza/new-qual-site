---
schema: qual/card@1
id: P-BKS08-9A
kind: problem
title: Growth of maximal element orders in symmetric groups
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the disjoint-cycle construction and the resulting
    uniform bound proving the stronger limit n/f(n) tends to zero.
---

::: {.problem}
For $n\ge1$, let $f(n)$ be the maximum order of an element of $S_n$. Show that
$$
\liminf_{n\to\infty}\frac{n}{f(n)}=0.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #order-lower-bound}
For every integer $k\ge1$,
$$
f(2k+1)\ge k(k+1)
$$
and
$$
f(2k+2)\ge k(k+1).
$$

::: pf-proof
In $S_{2k+1}$, take a $k$-cycle and a disjoint $(k+1)$-cycle. Their
product has order
$$
\operatorname{lcm}(k,k+1)=k(k+1),
$$
because consecutive integers are relatively prime. The same
permutation belongs to $S_{2k+2}$ after fixing the remaining point.
Since $f(n)$ is the maximum element order, both inequalities follow.
:::

:::

::: {.pf-step #ratio-bound}
If $n=2k+1$ or $n=2k+2$, then
$$
0\le\frac{n}{f(n)}\le\frac{2}{k}.
$$

::: pf-proof
By step [](#order-lower-bound){.pf-ref},
$$
\frac{n}{f(n)}
\le
\frac{2k+2}{k(k+1)}
=\frac{2}{k}.
$$
Nonnegativity is immediate.
:::

:::

::: {.pf-step #limit-zero}
In fact,
$$
\lim_{n\to\infty}\frac{n}{f(n)}=0.
$$

::: pf-proof
Every $n\ge3$ is either $2k+1$ or $2k+2$ for a unique $k\ge1$, and
$k\to\infty$ as $n\to\infty$. Hence the upper bound $2/k$ in
step [](#ratio-bound){.pf-ref} tends to $0$. The squeeze theorem gives the displayed limit.
:::

:::

::: {.pf-step #liminf-zero}
Consequently
$$
\boxed{
\liminf_{n\to\infty}\frac{n}{f(n)}=0.
}
$$

::: pf-proof
The liminf equals the limit established in step [](#limit-zero){.pf-ref}.
:::

:::

::: pf-qed
Step [](#liminf-zero){.pf-ref} is the required conclusion.
:::

:::

:::
