---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-14
kind: problem
title: Use an epsilon–delta proof for a quotient of convergent sequences
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
(January 2008 #6b) Suppose that $\lim_{n\to\infty}s_n=s$ and $\lim_{n\to\infty}t_n=t$ with $s\ne t$ and $s_n\ne t_n$ for all $n$.
Use an $\varepsilon$-$\delta$ proof to show that
$$
\lim_{n\to\infty}\frac{s_n+t_n}{s_n-t_n}=\frac{s+t}{s-t}.
$$
:::

::: {.solution}
Put $d=\abs{s-t}>0$.

::: pf

::: {.pf-step #s1}

There is $N_0$ such that $\abs{s_n-t_n}\geq d/2$ for all $n\geq N_0$.

::: pf-proof

Convergence supplies $N_0$ such that $\abs{s_n-s}<d/4$ and $\abs{t_n-t}<d/4$ whenever $n\geq N_0$. The reverse triangle inequality then gives
$$
\abs{s_n-t_n}\geq \abs{s-t}-\abs{s_n-s}-\abs{t_n-t}>d/2.
$$

:::

:::

::: pf-step

For each $\varepsilon>0$, there exists $N$ such that, whenever $n\geq N$,
$$
\abs{\frac{s_n+t_n}{s_n-t_n}-\frac{s+t}{s-t}}<\varepsilon;
$$
that is, $\frac{s_n+t_n}{s_n-t_n}\to\frac{s+t}{s-t}$.

::: pf-proof

Fix $\varepsilon>0$ and set $\eta=\varepsilon d^2/(8(\abs{s}+\abs{t}+1))$. Choose $N\geq N_0$ such that $\abs{s_n-s}<\eta$ and $\abs{t_n-t}<\eta$ whenever $n\geq N$. A common-denominator calculation gives
$$
\frac{s_n+t_n}{s_n-t_n}-\frac{s+t}{s-t}
=\frac{2(s(t_n-t)-t(s_n-s))}{(s_n-t_n)(s-t)}.
$$
By step [](#s1){.pf-ref}, the absolute value is at most
$$
\frac{4(\abs{s}\abs{t_n-t}+\abs{t}\abs{s_n-s})}{d^2}
<\frac{4(\abs{s}+\abs{t})\eta}{d^2}<\varepsilon.
$$

:::

:::

:::

:::
