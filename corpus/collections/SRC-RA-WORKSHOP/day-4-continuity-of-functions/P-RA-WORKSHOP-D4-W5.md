---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-W5
kind: problem
title: A liminf-limsup bound for real sequences
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
A useful lemma: Let $\{x_n\}$ be a real sequence with $\liminf_{n\to\infty}x_n$, $\limsup_{n\to\infty}x_n\in\RR$.
Show that for any $\varepsilon>0$ there exists some $N\in\NN$ so that
$$
\left(\liminf_{n\to\infty}x_n\right)-\varepsilon<x_n<
\left(\limsup_{n\to\infty}x_n\right)+\varepsilon
\qquad\text{for all }n\ge N.
$$
What does this result imply if $\limsup_{n\to\infty}x_n<L$?
:::

::: {.solution}
Write $\ell=\liminf_{n\to\infty}x_n$ and $u=\limsup_{n\to\infty}x_n$, both finite by hypothesis.

::: pf

::: {.pf-step #s1}

For every $\varepsilon>0$, there exists $N_1$ such that $x_n<u+\varepsilon$ whenever $n\geq N_1$.

::: pf-proof

By definition, $u=\inf_{N\geq1}\sup_{n\geq N}x_n$. The infimum property supplies $N_1$ with $\sup_{n\geq N_1}x_n<u+\varepsilon$. Every term of this tail is bounded above by its supremum, giving the assertion.

:::

:::

::: {.pf-step #s2}

For every $\varepsilon>0$, there exists $N_2$ such that $x_n>\ell-\varepsilon$ whenever $n\geq N_2$.

::: pf-proof

By definition, $\ell=\sup_{N\geq1}\inf_{n\geq N}x_n$. The supremum property supplies $N_2$ with $\inf_{n\geq N_2}x_n>\ell-\varepsilon$. Every term of this tail is at least its infimum.

:::

:::

::: pf-step

For every $\varepsilon>0$, there exists $N$ such that
$$
\ell-\varepsilon<x_n<u+\varepsilon\qquad(n\geq N).
$$

::: pf-proof

Choose $N=\max(N_1,N_2)$ with the indices from steps [](#s1){.pf-ref} and [](#s2){.pf-ref} for the same $\varepsilon$.

:::

:::

::: pf-step

If $\limsup x_n<L$, then $\boxed{x_n<L\text{ for every sufficiently large }n}$.

::: pf-proof

Set $\varepsilon=L-u>0$. Step [](#s1){.pf-ref} gives an index $N$ such that $x_n<u+\varepsilon=L$ for every $n\geq N$.

:::

:::

:::

:::
