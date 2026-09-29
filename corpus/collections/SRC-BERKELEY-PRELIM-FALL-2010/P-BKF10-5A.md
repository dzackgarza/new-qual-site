---
schema: qual/card@1
id: P-BKF10-5A
kind: problem
title: Uniform convergence of $\sum\sin(x/n^2)$ on bounded intervals
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 5A of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the global bound |sin t|<=|t| and the resulting summable
    majorant on an arbitrary bounded interval.
---

::: {.problem}
Show that the series
$$
\sum_{n=1}^{\infty}\sin\frac{x}{n^2}
$$
converges uniformly on every bounded interval in $\RR$.
:::

::: {.solution}
Let $I\subseteq\RR$ be a bounded interval.

::: pf

::: {.pf-step #s1}

There exists $B>0$ such that
$$
\abs{x}\le B
$$
for every $x\in I$.

::: pf-proof

This is exactly the boundedness of the interval $I$.

:::

:::

::: {.pf-step #s2}

For every real $t$,
$$
\abs{\sin t}\le\abs{t}.
$$

::: pf-proof

For $t\ge0$,
$$
\sin t=\int_0^t\cos s\,ds,
$$
so
$$
\abs{\sin t}
\le\int_0^t\abs{\cos s}\,ds
\le t.
$$
For $t<0$, apply the same estimate to $-t$ and use that sine is odd.

:::

:::

::: {.pf-step #s3}

For every $x\in I$ and every $n\ge1$,
$$
\abs{\sin(x/n^2)}\le\frac{B}{n^2}.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
\abs{\sin(x/n^2)}
\le\frac{\abs{x}}{n^2},
$$
and step [](#s1){.pf-ref} gives $\abs{x}\le B$.

:::

:::

::: {.pf-step #s4}

The series
$$
\sum_{n=1}^{\infty}\sin\frac{x}{n^2}
$$
converges uniformly on $I$.

::: pf-proof

The numerical series
$$
\sum_{n=1}^{\infty}\frac{B}{n^2}
$$
converges. Step [](#s3){.pf-ref} therefore gives a summable bound independent of
$x\in I$. The Weierstrass $M$-test proves uniform convergence on $I$.

:::

:::

::: pf-qed

Since $I$ was an arbitrary bounded interval, step [](#s4){.pf-ref} proves the
required statement.

:::

:::

:::
